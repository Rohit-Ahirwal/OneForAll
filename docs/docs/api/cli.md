---
sidebar_position: 5
---

# CLI Commands

OneForAll provides a command-line interface (CLI) for creating, developing, and building applications. The CLI helps streamline the development workflow with commands for project initialization, development server, building, and code generation.

## Installation

After installing OneForAll, the CLI is available as `oneforall`:

```bash
pip install oneforall
oneforall --help
```

## Commands

### `init`

Creates a new OneForAll application with a basic project structure.

```bash
oneforall init [project_name]
```

**Arguments:**
- `project_name` (optional): Name of the project directory. If not provided, creates files in the current directory.

**Example:**
```bash
# Create new project in current directory
oneforall init

# Create new project in specific directory
oneforall init my-app
cd my-app
```

**Generated Structure:**
```
my-app/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── assets/            # Static assets (images, etc.)
├── components/        # Custom components
└── README.md          # Project documentation
```

**Generated `app.py`:**
```python
from oneforall import App, Window, Text, Button, Container

# Create application
app = App()

# Initialize state
app.use_state("message", "Welcome to OneForAll!")

# Create main window
window = Window(title="OneForAll App", size=(600, 400))

# Create UI
container = Container(className="p-8 text-center space-y-4")
container.add(Text(app.use_state("message"), className="text-2xl font-bold"))

def change_message():
    app.set_state("message", "Hello from OneForAll!")

container.add(Button(
    "Click Me", 
    on_click=change_message,
    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
))

window.add_child(container)
app.append(window)

# Run the application
if __name__ == "__main__":
    app.run()
```

### `dev`

Starts the development server with hot reload functionality.

```bash
oneforall dev [file]
```

**Arguments:**
- `file` (optional): Python file to run. Defaults to `app.py`

**Options:**
- `--port`: Port for the development server (default: 8000)
- `--host`: Host address (default: localhost)
- `--no-reload`: Disable hot reload
- `--dev-tools`: Enable browser developer tools

**Example:**
```bash
# Start development server
oneforall dev

# Start with specific file
oneforall dev main.py

# Start with custom port and dev tools
oneforall dev --port 3000 --dev-tools

# Start without hot reload
oneforall dev --no-reload
```

**Features:**
- **Hot Reload**: Automatically restarts the app when Python files change
- **Live Refresh**: Updates the UI when code changes are detected
- **Error Display**: Shows Python errors in the UI for quick debugging
- **Development Tools**: Optional browser dev tools for debugging

### `build`

Builds a standalone executable using PyInstaller.

```bash
oneforall build [file]
```

**Arguments:**
- `file` (optional): Python file to build. Defaults to `app.py`

**Options:**
- `--name`: Name of the executable (default: based on file name)
- `--icon`: Path to icon file (.ico on Windows, .icns on macOS)
- `--onefile`: Create a single executable file
- `--windowed`: Hide console window (GUI only)
- `--add-data`: Additional data files to include
- `--hidden-import`: Hidden imports to include

**Example:**
```bash
# Basic build
oneforall build

# Build with custom name and icon
oneforall build --name "My App" --icon assets/icon.ico

# Build single file executable
oneforall build --onefile --windowed

# Build with additional data
oneforall build --add-data "assets:assets" --add-data "config.json:."
```

**Output:**
- `dist/` directory containing the executable
- `build/` directory with build artifacts
- `.spec` file for PyInstaller configuration

### `generate`

Generates code templates for components, windows, or other structures.

```bash
oneforall generate <type> <name>
```

**Types:**
- `component`: Generate a custom component
- `window`: Generate a window class
- `page`: Generate a complete page with components

**Example:**
```bash
# Generate a custom component
oneforall generate component UserCard

# Generate a window
oneforall generate window SettingsWindow

# Generate a complete page
oneforall generate page Dashboard
```

**Generated Component Example:**
```python
# components/user_card.py
from oneforall import Component, Container, Text, Button

class UserCard(Component):
    def __init__(self, app, user_data, className=""):
        super().__init__(className=className)
        self.app = app
        self.user_data = user_data
        
        # Create UI structure
        self.container = Container(className="bg-white shadow rounded-lg p-4")
        
        # User name
        self.container.add(Text(
            user_data.get("name", "Unknown User"),
            className="text-xl font-bold"
        ))
        
        # User email
        self.container.add(Text(
            user_data.get("email", ""),
            className="text-gray-600"
        ))
        
        # Action button
        self.container.add(Button(
            "View Profile",
            on_click=self.view_profile,
            className="mt-2 bg-blue-500 text-white px-4 py-2 rounded"
        ))
    
    def view_profile(self):
        # Handle profile view
        print(f"Viewing profile for {self.user_data.get('name')}")
    
    def render(self):
        return self.container.render()
```

## Configuration

### Project Configuration

Create a `oneforall.config.json` file in your project root for custom configuration:

```json
{
  "dev": {
    "port": 8000,
    "host": "localhost",
    "auto_reload": true,
    "dev_tools": false
  },
  "build": {
    "name": "MyApp",
    "icon": "assets/icon.ico",
    "onefile": true,
    "windowed": true,
    "additional_data": [
      "assets:assets",
      "config.json:."
    ],
    "hidden_imports": [
      "requests",
      "json"
    ]
  },
  "generate": {
    "component_template": "templates/component.py.tpl",
    "window_template": "templates/window.py.tpl"
  }
}
```

### Environment Variables

OneForAll CLI respects these environment variables:

- `ONEFORALL_DEV_PORT`: Default development server port
- `ONEFORALL_DEV_HOST`: Default development server host
- `ONEFORALL_BUILD_DIR`: Default build output directory
- `ONEFORALL_TEMPLATES_DIR`: Custom templates directory

## Development Workflow

### Typical Development Process

1. **Initialize Project**
   ```bash
   oneforall init my-app
   cd my-app
   ```

2. **Start Development**
   ```bash
   oneforall dev
   ```

3. **Develop and Test**
   - Edit `app.py` and other files
   - Changes are automatically reloaded
   - Test functionality in the app window

4. **Generate Components**
   ```bash
   oneforall generate component MyComponent
   ```

5. **Build for Production**
   ```bash
   oneforall build --onefile --windowed
   ```

### Hot Reload

The development server watches for changes in:
- Python files (`.py`)
- Template files (`.tpl`)
- Configuration files (`.json`, `.yaml`)

When changes are detected:
1. The application is automatically restarted
2. State is preserved when possible
3. The UI refreshes to show changes
4. Errors are displayed in the application window

### Debugging

Enable developer tools for debugging:

```bash
oneforall dev --dev-tools
```

This provides:
- Browser developer console
- Network inspection
- Element inspection
- JavaScript debugging

## Custom Templates

You can create custom templates for code generation:

### Component Template

Create `templates/component.py.tpl`:

```python
from oneforall import Component, Container, Text

class {{ component_name }}(Component):
    def __init__(self, app, className=""):
        super().__init__(className=className)
        self.app = app
        
        # Initialize component state
        self.state_key = f"{{ component_name.lower() }}_{id(self)}"
        app.use_state(self.state_key, {})
        
        # Create UI
        self.container = Container(className="p-4")
        self.container.add(Text("{{ component_name }} Component"))
    
    def render(self):
        return self.container.render()
```

### Window Template

Create `templates/window.py.tpl`:

```python
from oneforall import Window, Container, Text

class {{ window_name }}(Window):
    def __init__(self, app, title="{{ window_name }}", size=(800, 600)):
        super().__init__(title=title, size=size)
        self.app = app
        
        # Create main container
        main_container = Container(className="p-4")
        main_container.add(Text(f"Welcome to {title}"))
        
        self.add_child(main_container)
```

## Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Use different port
oneforall dev --port 3001
```

**Build Fails**
```bash
# Check dependencies
pip install pyinstaller

# Build with verbose output
oneforall build --verbose
```

**Hot Reload Not Working**
```bash
# Disable and re-enable
oneforall dev --no-reload
# Then restart with reload
oneforall dev
```

**Import Errors in Built App**
```bash
# Add hidden imports
oneforall build --hidden-import requests --hidden-import json
```

### Getting Help

```bash
# General help
oneforall --help

# Command-specific help
oneforall dev --help
oneforall build --help
oneforall generate --help
```

## See Also

- [Getting Started](../intro) - Basic OneForAll tutorial
- [App](./app) - Main application class
- [Components](./components) - Available UI components
- [Development Guide](../tutorial-basics/development-setup) - Setting up your development environment