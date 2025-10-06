import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Optional, no_type_check

import typer
from jinja2 import Template
from watchdog.events import FileModifiedEvent, FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from .logger import logger

cli = typer.Typer(help="OneForAll CLI - build and run apps easily")


@no_type_check
@cli.command()
def init(name: str = "my_app") -> None:
    """Scaffold a new OneForAll app"""
    os.makedirs(name, exist_ok=True)
    main_py = os.path.join(name, "example_basic.py")
    if not os.path.exists(main_py):
        with open(main_py, "w", encoding="utf-8") as f:
            f.write(
                """from oneforall import App, Text, Button

app = App(title="My First OneForAll App")
app.add(Text("Hello from OneForAll!"))

def handle_click(payload):
    print("Button clicked!", payload)

app.add(Button("Click Me", on_click=handle_click))

if __name__ == "__main__":
    app.run(dev_mode=True)
"""
            )
    logger.info(f"✅ Project '{name}' created.")


class ReloadHandler(FileSystemEventHandler):
    """Watchdog handler to reload app on Python changes"""

    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.process: Optional[subprocess.Popen] = None
        self.start_process()

    def start_process(self) -> None:
        """Start or restart the subprocess"""
        if self.process:
            self.process.kill()
        logger.info(f"Starting app: {self.file_path}")
        self.process = subprocess.Popen([sys.executable, self.file_path])

    def on_modified(self, event: FileSystemEvent) -> None:
        path = event.src_path
        if isinstance(path, bytes):
            path = path.decode("utf-8")
        if isinstance(event, FileModifiedEvent) and path.endswith(".py"):
            logger.info(f"Detected change in {path}, reloading...")
            self.start_process()


@no_type_check
@cli.command()
def dev(file: str = "example_basic.py") -> None:
    """Run a OneForAll app in dev mode with live reload"""
    logger.info("Running in dev mode with live reload...")
    event_handler = ReloadHandler(file)
    observer = Observer()
    folder = os.path.dirname(os.path.abspath(file)) or "."
    observer.schedule(event_handler, path=folder, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


@no_type_check
@cli.command()
def css(
    inputcss: str = "input.css",
    output: str = "assets/tailwind.css",
) -> None:
    """
    Scan all .py files for Tailwind classes,
    build CSS via Tailwind CLI, and clean temp files.
    """
    logger.info("🔍 Scanning for Tailwind classes...")

    # Collect all .py files
    py_files = list(Path(".").rglob("*.py"))
    all_classes = set()

    # Regex pattern for detecting Tailwind-like classes inside quotes
    class_pattern = re.compile(
        r'["\']([^"\']*(?:bg-|text-|border-|flex|grid|p-|m-|w-|h-|rounded|shadow)[^"\']*)["\']'
    )

    for file in py_files:
        try:
            content = file.read_text(encoding="utf-8")
            matches = class_pattern.findall(content)
            for match in matches:
                # Split by whitespace to catch multiple classes in one string
                all_classes.update(match.split())
        except Exception:
            continue

    if not all_classes:
        logger.error("⚠️ No Tailwind classes found in project.")
        raise typer.Exit()

    logger.info(f"✅ Found {len(all_classes)} unique Tailwind classes.")

    # Generate temporary HTML
    temp_html = Path("oneforall_temp.html")
    html_content = (
        "<html><body>\n"
        + "\n".join([f'<div class="{" ".join(all_classes)}"></div>'])
        + "\n</body></html>"
    )

    temp_html.write_text(html_content, encoding="utf-8")

    logger.debug(f"📄 Created temporary file: {temp_html}")

    # Ensure assets directory
    # os.makedirs(os.path.dirname(output), exist_ok=True)

    # Run Tailwind CLI build command
    logger.debug("⚙️ Generating Tailwind CSS...")

    cmd: List[str] = [
        "npx",
        "@tailwindcss/cli",
        "-i",
        str(Path.cwd() / inputcss),
        "-o",
        f"./{output}",
        "--minify",
    ]

    subprocess.run(cmd, check=True, shell=True)

    logger.info(f"✅ CSS generated successfully → {output}")

    # Cleanup
    try:
        temp_html.unlink()
        logger.debug("🧹 Temporary file deleted.")
    except Exception:
        logger.error(f"⚠️ Could not delete temp file: {temp_html}")

    logger.info("🎉 CSS build complete!")


@no_type_check
@cli.command()
def build(
    file: str = "example_basic.py",
    name: str = "OneForAllApp",
    tailwind: str = "assets/tailwind.css",
) -> None:
    """
    Build a standalone app using PyInstaller.
    Includes Tailwind CSS + assets.
    """
    logger.info("Building app with PyInstaller...")

    dist_dir = os.path.join(os.getcwd(), "dist")
    build_dir = os.path.join(os.getcwd(), "build")

    # Ensure clean build (cross-platform)
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    # Determine PyInstaller path separator for --add-data
    sep = ";" if sys.platform.startswith("win") else ":"

    # Prepare --add-data entries
    add_data_list = [f"{os.path.abspath('assets')}{sep}oneforall/assets"]

    if tailwind and not os.path.abspath(tailwind).startswith(os.path.abspath("assets")):
        add_data_list.append(f"{os.path.abspath(tailwind)}{sep}oneforall/assets")

    # Build the PyInstaller command
    cmd = [
        "pyinstaller",
        "--name",
        name,
        "--onefile",
        "--noconfirm",
        "--windowed",
        "--clean",
    ]

    # Add each --add-data separately
    for item in add_data_list:
        cmd.extend(["--add-data", item])

    # Hidden imports
    cmd.extend(["--hidden-import", "typer", "--hidden-import", "watchdog"])

    # Script file
    cmd.append(file)

    logger.info(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    logger.info(f"✅ Build complete! Binary in ./dist/{name}")


@no_type_check
@cli.command()
def generate(name: str, type: str = "button") -> None:
    """
    Generate a prebuilt OneForAll component from template.
    """
    templates_dir = os.path.join(os.path.dirname(__file__), "templates")
    template_file = os.path.join(templates_dir, f"{type}.py.tpl")

    if not os.path.exists(template_file):
        typer.echo(f"No template found for {type}")
        raise typer.Exit()

    with open(template_file, "r", encoding="utf-8") as f:
        tpl_content = f.read()

    template = Template(tpl_content)
    rendered = template.render(name=name)

    components_dir = os.path.join(os.getcwd(), "components")
    os.makedirs(components_dir, exist_ok=True)
    output_file = os.path.join(components_dir, f"{type}.py")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered)

    typer.echo(f"✅ Component {name} generated at {output_file}")


if __name__ == "__main__":
    cli()
