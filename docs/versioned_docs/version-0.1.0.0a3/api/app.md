---
sidebar_position: 1
---

# App API Reference

The `App` class is the main entry point for OneForAll applications. It manages the application lifecycle, windows, and global state.

:::info Alpha Version
The App API is stable in OneForAll **alpha** (v0.1.0a3) but may receive additional features in future releases.
:::

## Class: App

### Constructor

```python
from oneforall import App

app = App()
```

Creates a new OneForAll application instance.

**Parameters:**
- None

**Returns:**
- `App` instance

### Methods

#### create_window()

Creates a new application window.

```python
window = app.create_window(
    title="My Application",
    size=(800, 600),
    position=(100, 100),
    resizable=True,
    minimizable=True,
    maximizable=True,
    on_top=False
)
```

**Parameters:**
- `title` (str): Window title displayed in the title bar
- `size` (tuple): Window dimensions as (width, height) in pixels
- `position` (tuple, optional): Window position as (x, y) coordinates. Defaults to system placement
- `resizable` (bool, optional): Whether the window can be resized. Defaults to `True`
- `minimizable` (bool, optional): Whether the window can be minimized. Defaults to `True`
- `maximizable` (bool, optional): Whether the window can be maximized. Defaults to `True`
- `on_top` (bool, optional): Whether the window stays on top of other windows. Defaults to `False`

**Returns:**
- `Window` instance

**Example:**
```python
# Basic window
main_window = app.create_window("Main App", (1000, 700))

# Dialog window
dialog = app.create_window(
    title="Settings",
    size=(400, 300),
    resizable=False,
    on_top=True
)

# Tool window
tools = app.create_window(
    title="Tools",
    size=(200, 500),
    position=(50, 100),
    maximizable=False
)
```

#### run()

Starts the application event loop and displays all created windows.

```python
app.run()
```

**Parameters:**
- None

**Returns:**
- None

**Note:** This method blocks until the application is closed.

**Example:**
```python
from oneforall import App, Container, Text

app = App()
window = app.create_window("Hello World", (400, 300))

container = Container()
container.add(Text("Hello, OneForAll!"))
window.add_child(container)

app.run()  # Blocks until app is closed
```

### Properties

#### windows

Read-only list of all windows created by this application.

```python
windows = app.windows
```

**Type:** `list[Window]`

**Example:**
```python
app = App()
window1 = app.create_window("Window 1", (400, 300))
window2 = app.create_window("Window 2", (500, 400))

print(f"Total windows: {len(app.windows)}")  # Output: Total windows: 2

for i, window in enumerate(app.windows):
    print(f"Window {i+1}: {window.title}")
```

## Usage Patterns

### Single Window Application

```python
from oneforall import App, Container, Text, Button

def create_single_window_app():
    app = App()
    
    # Create main window
    window = app.create_window(
        title="Single Window App",
        size=(600, 400),
        position=(200, 150)
    )
    
    # Build UI
    container = Container(className="p-6")
    container.add(Text("Welcome to OneForAll", className="text-2xl font-bold mb-4"))
    container.add(Button("Click Me", className="px-4 py-2 bg-blue-500 text-white rounded"))
    
    window.add_child(container)
    
    return app

# Usage
app = create_single_window_app()
app.run()
```

### Multi-Window Application

```python
from oneforall import App, Container, Text, Button

def create_multi_window_app():
    app = App()
    
    # Main application window
    main_window = app.create_window(
        title="Main Application",
        size=(800, 600),
        position=(100, 100)
    )
    
    # Settings window
    settings_window = app.create_window(
        title="Settings",
        size=(400, 500),
        position=(950, 100),
        resizable=False
    )
    
    # Tool palette
    tools_window = app.create_window(
        title="Tools",
        size=(200, 400),
        position=(50, 100),
        maximizable=False
    )
    
    # Build main window
    main_container = Container(className="p-6")
    main_container.add(Text("Main Application", className="text-2xl font-bold mb-4"))
    main_container.add(Text("This is the main workspace.", className="text-gray-600 mb-4"))
    
    window_controls = Container(className="flex space-x-2")
    window_controls.add(Button("Open Settings", className="px-3 py-2 bg-blue-500 text-white rounded"))
    window_controls.add(Button("Show Tools", className="px-3 py-2 bg-green-500 text-white rounded"))
    
    main_container.add(window_controls)
    main_window.add_child(main_container)
    
    # Build settings window
    settings_container = Container(className="p-6")
    settings_container.add(Text("Application Settings", className="text-xl font-bold mb-4"))
    settings_container.add(Text("Configure your application here.", className="text-gray-600"))
    settings_window.add_child(settings_container)
    
    # Build tools window
    tools_container = Container(className="p-4")
    tools_container.add(Text("Tool Palette", className="text-lg font-bold mb-3"))
    
    tools_list = Container(className="space-y-2")
    tools_list.add(Button("Tool 1", className="w-full px-3 py-2 bg-gray-200 rounded text-sm"))
    tools_list.add(Button("Tool 2", className="w-full px-3 py-2 bg-gray-200 rounded text-sm"))
    tools_list.add(Button("Tool 3", className="w-full px-3 py-2 bg-gray-200 rounded text-sm"))
    
    tools_container.add(tools_list)
    tools_window.add_child(tools_container)
    
    return app

# Usage
app = create_multi_window_app()
app.run()
```

### Application with Shared State

```python
from oneforall import App, Container, Text, Button

class SharedStateApp:
    def __init__(self):
        self.app = App()
        
        # Shared application state
        self.state = {
            'user_name': 'John Doe',
            'theme': 'light',
            'notifications_enabled': True
        }
        
        self.setup_windows()
    
    def setup_windows(self):
        # Main window
        self.main_window = self.app.create_window(
            title="Shared State App",
            size=(600, 400)
        )
        
        # Settings window
        self.settings_window = self.app.create_window(
            title="Settings",
            size=(400, 300)
        )
        
        self.build_main_window()
        self.build_settings_window()
    
    def build_main_window(self):
        container = Container(className="p-6")
        
        # Display current state
        container.add(Text(f"Welcome, {self.state['user_name']}", className="text-xl font-bold mb-4"))
        container.add(Text(f"Theme: {self.state['theme']}", className="text-gray-600 mb-2"))
        container.add(Text(f"Notifications: {'On' if self.state['notifications_enabled'] else 'Off'}", className="text-gray-600 mb-4"))
        
        # Controls
        container.add(Button("Open Settings", className="px-4 py-2 bg-blue-500 text-white rounded"))
        
        self.main_window.add_child(container)
    
    def build_settings_window(self):
        container = Container(className="p-6")
        
        container.add(Text("Settings", className="text-xl font-bold mb-4"))
        
        # Settings controls (in a real app, these would update the shared state)
        settings_list = Container(className="space-y-3")
        settings_list.add(Button("Toggle Theme", className="w-full px-4 py-2 bg-gray-200 rounded"))
        settings_list.add(Button("Toggle Notifications", className="w-full px-4 py-2 bg-gray-200 rounded"))
        settings_list.add(Button("Change User Name", className="w-full px-4 py-2 bg-blue-500 text-white rounded"))
        
        container.add(settings_list)
        self.settings_window.add_child(container)
    
    def run(self):
        self.app.run()

# Usage
app = SharedStateApp()
app.run()
```

## Best Practices

### Application Lifecycle

```python
class ManagedApp:
    def __init__(self):
        self.app = App()
        self.is_initialized = False
        self.windows = {}
    
    def initialize(self):
        """Initialize the application"""
        if self.is_initialized:
            return
        
        # Create main window
        self.windows['main'] = self.app.create_window(
            title="Managed Application",
            size=(800, 600)
        )
        
        # Setup UI
        self.setup_ui()
        
        self.is_initialized = True
    
    def setup_ui(self):
        """Setup the user interface"""
        container = Container(className="p-6")
        container.add(Text("Managed Application", className="text-2xl font-bold"))
        
        self.windows['main'].add_child(container)
    
    def run(self):
        """Run the application"""
        if not self.is_initialized:
            self.initialize()
        
        self.app.run()
    
    def cleanup(self):
        """Cleanup resources (called before app closes)"""
        # Perform cleanup operations
        pass

# Usage
app = ManagedApp()
try:
    app.run()
finally:
    app.cleanup()
```

### Error Handling

```python
from oneforall import App, Container, Text

def create_robust_app():
    try:
        app = App()
        
        # Create window with error handling
        try:
            window = app.create_window("Robust App", (600, 400))
        except Exception as e:
            print(f"Failed to create window: {e}")
            return None
        
        # Build UI with error handling
        try:
            container = Container(className="p-6")
            container.add(Text("Application loaded successfully", className="text-green-600"))
            window.add_child(container)
        except Exception as e:
            print(f"Failed to build UI: {e}")
            return None
        
        return app
        
    except Exception as e:
        print(f"Failed to create application: {e}")
        return None

# Usage
app = create_robust_app()
if app:
    try:
        app.run()
    except KeyboardInterrupt:
        print("Application interrupted by user")
    except Exception as e:
        print(f"Application error: {e}")
else:
    print("Failed to start application")
```

## Related APIs

- [Window API](./window) - Window management and configuration
- [Components API](./components) - UI components for building interfaces
- [State Management API](./state-management) - Managing application state

## Examples

See the [Tutorial - Basics](../tutorial-basics/your-first-app) section for complete examples and step-by-step guides.

---

The App class provides the foundation for all OneForAll applications, offering simple yet powerful window management and application lifecycle control.