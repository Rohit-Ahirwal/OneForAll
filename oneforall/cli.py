import os
import subprocess
import sys
import time

import typer
from jinja2 import Template
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from .logger import logger

cli = typer.Typer(help="OneForAll CLI - build and run apps easily")


@cli.command()
def init(name: str = "my_app"):
    """Scaffold a new OneForAll app"""
    os.makedirs(name, exist_ok=True)
    main_py = os.path.join(name, "example_basic.py")
    if not os.path.exists(main_py):
        with open(main_py, "w") as f:
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

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.kill()
        logger.info(f"Starting app: {self.file_path}")
        self.process = subprocess.Popen([sys.executable, self.file_path])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            logger.info(f"Detected change in {event.src_path}, reloading...")
            self.start_process()


@cli.command()
def dev(file: str = "example_basic.py"):
    """Run a OneForAll app"""
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


@cli.command()
def build(
    file: str = "example_basic.py",
    name: str = "OneForAllApp",
    tailwind: str = "assets/tailwind.css",
):
    """
    Build a standalone app using PyInstaller.
    Includes Tailwind CSS + assets.
    """
    logger.info("Building app with PyInstaller...")

    dist_dir = os.path.join(os.getcwd(), "dist")
    build_dir = os.path.join(os.getcwd(), "build")

    # Ensure clean build
    if os.path.exists(dist_dir):
        subprocess.run(["rm", "-rf", dist_dir])
    if os.path.exists(build_dir):
        subprocess.run(["rm", "-rf", build_dir])

    cmd = [
        "pyinstaller",
        "--name",
        name,
        "--onefile",  # single binary
        "--noconfirm",
        "--clean",
        "--add-data",
        f"{tailwind}{os.pathsep}oneforall/assets",
        "--hidden-import",
        "typer",
        "--hidden-import",
        "watchdog",
        file,
    ]

    logger.info(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    logger.info(f"✅ Build complete! Binary in ./dist/{name}")


@cli.command()
def generate(
    name: str,
    type: str = "button",
):
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

    rendered = template.render(
        name=name,
    )

    # Create output directory in user project
    components_dir = os.path.join(os.getcwd(), "components")
    os.makedirs(components_dir, exist_ok=True)
    output_file = os.path.join(components_dir, f"{type}.py")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered)

    typer.echo(f"✅ Component {name} generated at {output_file}")


if __name__ == "__main__":
    cli()
