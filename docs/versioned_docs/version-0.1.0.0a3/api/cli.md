---
sidebar_position: 5
---

# CLI API Reference

OneForAll provides a command-line interface (CLI) for creating, developing, and building desktop applications. The CLI is built with Typer and offers several commands to streamline your development workflow.

:::info Alpha Version
The CLI is stable in OneForAll **alpha** (v0.1.0a3) with full functionality for project scaffolding, development, and CSS generation.
:::

## Installation and Usage

The CLI is automatically available when you install OneForAll:

```bash
pip install oneforall
```

Access the CLI using the `oneforall` command:

```bash
oneforall --help
```

## Commands

### init

Creates a new OneForAll application with a basic project structure.

```bash
oneforall init [PROJECT_NAME] [OPTIONS]
```

**Arguments:**
- `PROJECT_NAME` (optional): Name of the project directory to create. Defaults to current directory if not specified.

**Options:**
- `--template TEXT`: Template to use for the project (default: "basic")
- `--help`: Show help message

**Examples:**

```bash
# Create a new project in current directory
oneforall init

# Create a new project with specific name
oneforall init my-desktop-app

# Create project with template (when templates are available)
oneforall init my-app --template advanced
```

**Generated Project Structure:**

```
my-desktop-app/
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
├── assets/             # Static assets (images, icons, etc.)
├── components/         # Custom components (optional)
├── styles/            # Custom CSS files (optional)
└── README.md          # Project documentation
```

**Generated main.py:**

```python
from oneforall import App, Container, Text, Button

def main():
    # Create the application
    app = App()
    
    # Create the main window
    window = app.create_window(
        title="My OneForAll App",
        size=(800, 600)
    )
    
    # Create the UI
    container = Container(className="p-8 text-center")
    
    # Add components
    container.add(Text(
        "Welcome to OneForAll!",
        className="text-3xl font-bold mb-6 text-blue-600"
    ))
    
    container.add(Text(
        "Your desktop app is ready to go.",
        className="text-lg text-gray-600 mb-8"
    ))
    
    container.add(Button(
        "Get Started",
        className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors",
        onclick=lambda: print("Button clicked!")
    ))
    
    # Add container to window
    window.add_child(container)
    
    # Run the application
    app.run()

if __name__ == "__main__":
    main()
```

### dev

Starts the development server with hot reload functionality. Watches for file changes and automatically restarts the application.

```bash
oneforall dev [FILE] [OPTIONS]
```

**Arguments:**
- `FILE` (optional): Python file to run. Defaults to "main.py"

**Options:**
- `--watch-dir TEXT`: Additional directories to watch for changes (can be used multiple times)
- `--ignore-pattern TEXT`: File patterns to ignore during watching (can be used multiple times)
- `--no-reload`: Disable hot reload functionality
- `--help`: Show help message

**Examples:**

```bash
# Start development server with default file (main.py)
oneforall dev

# Start with specific file
oneforall dev app.py

# Watch additional directories
oneforall dev --watch-dir components --watch-dir assets

# Ignore specific patterns
oneforall dev --ignore-pattern "*.tmp" --ignore-pattern "__pycache__"

# Run without hot reload
oneforall dev --no-reload
```

**Features:**

- **Hot Reload**: Automatically restarts the application when Python files change
- **File Watching**: Monitors the current directory and specified watch directories
- **Smart Ignoring**: Ignores common non-essential files (`.git`, `__pycache__`, `.pyc`, etc.)
- **Fast Restart**: Optimized restart process for quick development cycles

**Watched File Types:**
- `.py` - Python source files
- `.css` - CSS stylesheets
- `.js` - JavaScript files
- `.html` - HTML templates
- `.json` - Configuration files

**Default Ignored Patterns:**
- `__pycache__/`
- `*.pyc`
- `*.pyo`
- `.git/`
- `.vscode/`
- `.idea/`
- `node_modules/`
- `*.tmp`
- `*.log`

### css

Scans Python files for Tailwind CSS classes and generates the corresponding CSS file. This command is essential for ensuring that all Tailwind classes used in your components are included in the final CSS bundle.

```bash
oneforall css [OPTIONS]
```

**Options:**
- `--input-dir TEXT`: Directory to scan for Python files (default: current directory)
- `--output-file TEXT`: Output CSS file path (default: "styles.css")
- `--config-file TEXT`: Tailwind config file path (optional)
- `--watch`: Watch for changes and regenerate CSS automatically
- `--minify`: Minify the generated CSS
- `--help`: Show help message

**Examples:**

```bash
# Generate CSS from current directory
oneforall css

# Specify input directory and output file
oneforall css --input-dir src --output-file assets/styles.css

# Watch for changes and auto-regenerate
oneforall css --watch

# Generate minified CSS
oneforall css --minify

# Use custom Tailwind config
oneforall css --config-file tailwind.config.js
```

**How it Works:**

1. **Scanning**: Recursively scans all `.py` files in the specified directory
2. **Extraction**: Uses regex patterns to find Tailwind classes in `className` attributes
3. **Generation**: Generates CSS using Tailwind's JIT (Just-In-Time) compiler
4. **Output**: Writes the generated CSS to the specified output file

**Supported Class Patterns:**

```python
# Direct className usage
Text("Hello", className="text-blue-500 font-bold")
Button("Click", className="px-4 py-2 bg-green-500 rounded")

# Multi-line className
Container(className="""
    flex flex-col items-center
    p-6 bg-white rounded-lg shadow-md
    hover:shadow-lg transition-shadow
""")

# Dynamic className (basic detection)
button_classes = "px-4 py-2 bg-blue-500 text-white rounded"
Button("Submit", className=button_classes)

# Conditional className
className = "text-red-500" if error else "text-green-500"
Text(message, className=className)
```

**Generated CSS Structure:**

```css
/* Base Tailwind styles */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Generated utility classes */
.text-blue-500 { color: rgb(59 130 246); }
.font-bold { font-weight: 700; }
.px-4 { padding-left: 1rem; padding-right: 1rem; }
.py-2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
/* ... more classes as needed */
```

## CLI Configuration

### Global Configuration

Create a `.oneforall.json` file in your project root to configure CLI behavior:

```json
{
  "dev": {
    "defaultFile": "app.py",
    "watchDirs": ["components", "assets"],
    "ignorePatterns": ["*.tmp", "test_*"],
    "autoReload": true
  },
  "css": {
    "inputDir": "src",
    "outputFile": "assets/styles.css",
    "watch": false,
    "minify": false,
    "configFile": "tailwind.config.js"
  },
  "init": {
    "defaultTemplate": "basic",
    "author": "Your Name",
    "license": "MIT"
  }
}
```

### Environment Variables

Configure CLI behavior using environment variables:

```bash
# Development settings
export ONEFORALL_DEV_FILE=app.py
export ONEFORALL_DEV_WATCH_DIRS=components,assets
export ONEFORALL_DEV_AUTO_RELOAD=true

# CSS generation settings
export ONEFORALL_CSS_INPUT_DIR=src
export ONEFORALL_CSS_OUTPUT_FILE=dist/styles.css
export ONEFORALL_CSS_MINIFY=true

# General settings
export ONEFORALL_LOG_LEVEL=INFO
```

## Development Workflow

### Typical Development Session

```bash
# 1. Create a new project
oneforall init my-app
cd my-app

# 2. Start development server
oneforall dev

# 3. In another terminal, watch CSS changes
oneforall css --watch

# 4. Edit your Python files - the app will auto-reload
# 5. Add new Tailwind classes - CSS will auto-regenerate
```

### Project Structure Best Practices

```
my-app/
├── main.py                 # Application entry point
├── components/            # Custom components
│   ├── __init__.py
│   ├── header.py
│   ├── sidebar.py
│   └── footer.py
├── pages/                 # Application pages/views
│   ├── __init__.py
│   ├── home.py
│   ├── settings.py
│   └── about.py
├── assets/               # Static assets
│   ├── images/
│   ├── icons/
│   └── styles.css        # Generated CSS
├── utils/               # Utility functions
│   ├── __init__.py
│   ├── helpers.py
│   └── constants.py
├── requirements.txt     # Dependencies
├── .oneforall.json     # CLI configuration
└── README.md           # Documentation
```

### Advanced Development Setup

```bash
# Create project with custom structure
oneforall init advanced-app
cd advanced-app

# Setup development with multiple watch directories
oneforall dev main.py \
  --watch-dir components \
  --watch-dir pages \
  --watch-dir utils \
  --ignore-pattern "test_*" \
  --ignore-pattern "*.backup"

# Setup CSS generation with custom config
oneforall css \
  --input-dir . \
  --output-file assets/dist/styles.css \
  --config-file tailwind.config.js \
  --watch \
  --minify
```

## Integration with Build Tools

### Using with PyInstaller

```bash
# Generate CSS before building
oneforall css --minify --output-file dist/styles.css

# Build executable
pyinstaller --onefile \
  --add-data "dist/styles.css;." \
  --add-data "assets;assets" \
  main.py
```

### Using with Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Generate CSS
RUN oneforall css --minify --output-file assets/styles.css

# Run the application
CMD ["python", "main.py"]
```

### CI/CD Integration

```yaml
# GitHub Actions example
name: Build OneForAll App

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Generate CSS
      run: |
        oneforall css --minify --output-file dist/styles.css
    
    - name: Run tests
      run: |
        python -m pytest
    
    - name: Build executable
      run: |
        pyinstaller --onefile main.py
```

## Troubleshooting

### Common Issues

**1. Command not found**
```bash
# Error: oneforall: command not found
# Solution: Ensure OneForAll is installed and in PATH
pip install oneforall
# or
python -m oneforall --help
```

**2. Hot reload not working**
```bash
# Check if files are being watched
oneforall dev --watch-dir . --ignore-pattern ""

# Try running without reload to test basic functionality
oneforall dev --no-reload
```

**3. CSS not generating**
```bash
# Check if Python files contain className attributes
grep -r "className" .

# Run with verbose output
oneforall css --input-dir . --output-file debug.css
```

**4. Permission errors**
```bash
# On Windows, run as administrator if needed
# On Unix systems, check file permissions
chmod +x main.py
```

### Debug Mode

Enable debug logging for troubleshooting:

```bash
# Set log level
export ONEFORALL_LOG_LEVEL=DEBUG

# Run commands with debug output
oneforall dev --help
oneforall css --help
```

### Getting Help

```bash
# General help
oneforall --help

# Command-specific help
oneforall init --help
oneforall dev --help
oneforall css --help

# Version information
oneforall --version
```

## Related APIs

- [App API](./app) - Application management
- [Components API](./components) - UI components that use Tailwind classes
- [Window API](./window) - Window management

## Examples

See the [Your First App Tutorial](../tutorial-basics/your-first-app) for a complete example of using the CLI to create and develop a OneForAll application.

---

The CLI provides essential tools for OneForAll development, from project creation to hot reload development and CSS generation, making it easy to build and maintain desktop applications.