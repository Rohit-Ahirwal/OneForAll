---
sidebar_position: 2
---

# Window API Reference

The `Window` class represents an individual application window in OneForAll. It manages the window's content, properties, and lifecycle.

:::info Alpha Version
The Window API is stable in OneForAll **alpha** (v0.1.0a3) with full functionality for desktop application development.
:::

## Class: Window

Windows are created through the `App.create_window()` method and cannot be instantiated directly.

```python
from oneforall import App

app = App()
window = app.create_window("My Window", (800, 600))
```

### Properties

#### title

The window's title displayed in the title bar.

```python
window.title = "New Window Title"
print(window.title)  # Output: "New Window Title"
```

**Type:** `str`

#### size

The window's dimensions as a tuple of (width, height) in pixels.

```python
window.size = (1000, 700)
print(window.size)  # Output: (1000, 700)
```

**Type:** `tuple[int, int]`

#### position

The window's position as a tuple of (x, y) coordinates.

```python
window.position = (100, 50)
print(window.position)  # Output: (100, 50)
```

**Type:** `tuple[int, int]`

#### resizable

Whether the window can be resized by the user.

```python
window.resizable = False  # Disable resizing
print(window.resizable)  # Output: False
```

**Type:** `bool`

#### minimizable

Whether the window can be minimized.

```python
window.minimizable = False  # Disable minimize button
print(window.minimizable)  # Output: False
```

**Type:** `bool`

#### maximizable

Whether the window can be maximized.

```python
window.maximizable = False  # Disable maximize button
print(window.maximizable)  # Output: False
```

**Type:** `bool`

#### on_top

Whether the window stays on top of other windows.

```python
window.on_top = True  # Keep window on top
print(window.on_top)  # Output: True
```

**Type:** `bool`

### Methods

#### add_child()

Adds a component to the window as the root content.

```python
from oneforall import Container, Text

container = Container(className="p-6")
container.add(Text("Hello World"))

window.add_child(container)
```

**Parameters:**
- `component` (Component): The root component to add to the window

**Returns:**
- None

**Note:** Each window can have only one root component. Adding a new child replaces the previous one.

#### remove_child()

Removes the current root component from the window.

```python
window.remove_child()
```

**Parameters:**
- None

**Returns:**
- None

#### render()

Renders the window's content to HTML. This method is called automatically by the framework.

```python
html_content = window.render()
```

**Parameters:**
- None

**Returns:**
- `str`: The rendered HTML content

#### show()

Shows the window if it's hidden.

```python
window.show()
```

**Parameters:**
- None

**Returns:**
- None

#### hide()

Hides the window without closing it.

```python
window.hide()
```

**Parameters:**
- None

**Returns:**
- None

#### close()

Closes the window and removes it from the application.

```python
window.close()
```

**Parameters:**
- None

**Returns:**
- None

**Note:** Once closed, the window cannot be reopened.

#### focus()

Brings the window to the front and gives it focus.

```python
window.focus()
```

**Parameters:**
- None

**Returns:**
- None

#### minimize()

Minimizes the window (if minimizable).

```python
window.minimize()
```

**Parameters:**
- None

**Returns:**
- None

#### maximize()

Maximizes the window (if maximizable).

```python
window.maximize()
```

**Parameters:**
- None

**Returns:**
- None

#### restore()

Restores the window from minimized or maximized state.

```python
window.restore()
```

**Parameters:**
- None

**Returns:**
- None

## Usage Examples

### Basic Window Setup

```python
from oneforall import App, Container, Text, Button

app = App()

# Create a basic window
window = app.create_window(
    title="Basic Window",
    size=(600, 400),
    position=(200, 150)
)

# Create content
container = Container(className="p-6")
container.add(Text("Welcome to OneForAll", className="text-2xl font-bold mb-4"))
container.add(Text("This is a basic window example.", className="text-gray-600 mb-4"))
container.add(Button("Click Me", className="px-4 py-2 bg-blue-500 text-white rounded"))

# Add content to window
window.add_child(container)

app.run()
```

### Window Configuration

```python
from oneforall import App, Container, Text

app = App()

# Create a configured window
window = app.create_window(
    title="Configured Window",
    size=(500, 300),
    position=(300, 200),
    resizable=False,      # Fixed size
    minimizable=True,     # Can be minimized
    maximizable=False,    # Cannot be maximized
    on_top=True          # Always on top
)

# Build content
content = Container(className="p-6 text-center")
content.add(Text("Fixed Size Window", className="text-xl font-bold mb-2"))
content.add(Text("This window cannot be resized or maximized.", className="text-gray-600"))

window.add_child(content)

app.run()
```

### Dynamic Window Properties

```python
from oneforall import App, Container, Text, Button

class DynamicWindow:
    def __init__(self):
        self.app = App()
        self.window = self.app.create_window("Dynamic Window", (600, 400))
        self.setup_ui()
    
    def setup_ui(self):
        container = Container(className="p-6")
        
        # Title
        container.add(Text("Dynamic Window Properties", className="text-xl font-bold mb-4"))
        
        # Current properties display
        self.properties_display = Container(className="mb-4 p-4 bg-gray-100 rounded")
        self.update_properties_display()
        container.add(self.properties_display)
        
        # Control buttons
        controls = Container(className="space-y-2")
        
        controls.add(Button(
            "Toggle Resizable", 
            className="w-full px-4 py-2 bg-blue-500 text-white rounded",
            onclick=self.toggle_resizable
        ))
        
        controls.add(Button(
            "Toggle On Top", 
            className="w-full px-4 py-2 bg-green-500 text-white rounded",
            onclick=self.toggle_on_top
        ))
        
        controls.add(Button(
            "Change Title", 
            className="w-full px-4 py-2 bg-purple-500 text-white rounded",
            onclick=self.change_title
        ))
        
        controls.add(Button(
            "Resize Window", 
            className="w-full px-4 py-2 bg-orange-500 text-white rounded",
            onclick=self.resize_window
        ))
        
        container.add(controls)
        self.window.add_child(container)
    
    def update_properties_display(self):
        """Update the properties display"""
        self.properties_display.children.clear()
        
        props = [
            f"Title: {self.window.title}",
            f"Size: {self.window.size[0]}x{self.window.size[1]}",
            f"Position: ({self.window.position[0]}, {self.window.position[1]})",
            f"Resizable: {self.window.resizable}",
            f"On Top: {self.window.on_top}"
        ]
        
        for prop in props:
            self.properties_display.add(Text(prop, className="text-sm text-gray-700"))
    
    def toggle_resizable(self):
        """Toggle window resizable property"""
        self.window.resizable = not self.window.resizable
        self.update_properties_display()
    
    def toggle_on_top(self):
        """Toggle window on top property"""
        self.window.on_top = not self.window.on_top
        self.update_properties_display()
    
    def change_title(self):
        """Change window title"""
        import random
        titles = ["Dynamic Window", "Updated Title", "New Window Name", "OneForAll App"]
        self.window.title = random.choice(titles)
        self.update_properties_display()
    
    def resize_window(self):
        """Resize the window"""
        import random
        sizes = [(600, 400), (800, 500), (500, 350), (700, 450)]
        self.window.size = random.choice(sizes)
        self.update_properties_display()
    
    def run(self):
        self.app.run()

# Usage
app = DynamicWindow()
app.run()
```

### Multi-Window Management

```python
from oneforall import App, Container, Text, Button

class MultiWindowManager:
    def __init__(self):
        self.app = App()
        self.windows = {}
        self.window_counter = 0
        self.setup_main_window()
    
    def setup_main_window(self):
        """Setup the main control window"""
        self.main_window = self.app.create_window(
            title="Window Manager",
            size=(400, 500),
            position=(100, 100)
        )
        
        container = Container(className="p-6")
        container.add(Text("Window Manager", className="text-xl font-bold mb-4"))
        
        # Window creation controls
        creation_controls = Container(className="mb-6 space-y-2")
        creation_controls.add(Button(
            "Create Normal Window",
            className="w-full px-4 py-2 bg-blue-500 text-white rounded",
            onclick=self.create_normal_window
        ))
        
        creation_controls.add(Button(
            "Create Dialog Window",
            className="w-full px-4 py-2 bg-green-500 text-white rounded",
            onclick=self.create_dialog_window
        ))
        
        creation_controls.add(Button(
            "Create Tool Window",
            className="w-full px-4 py-2 bg-purple-500 text-white rounded",
            onclick=self.create_tool_window
        ))
        
        container.add(creation_controls)
        
        # Window list
        container.add(Text("Active Windows:", className="font-semibold mb-2"))
        self.window_list = Container(className="space-y-1")
        self.update_window_list()
        container.add(self.window_list)
        
        self.main_window.add_child(container)
    
    def create_normal_window(self):
        """Create a normal window"""
        self.window_counter += 1
        window_id = f"normal_{self.window_counter}"
        
        window = self.app.create_window(
            title=f"Normal Window {self.window_counter}",
            size=(500, 350),
            position=(200 + self.window_counter * 30, 150 + self.window_counter * 30)
        )
        
        content = Container(className="p-6")
        content.add(Text(f"Normal Window {self.window_counter}", className="text-lg font-bold mb-2"))
        content.add(Text("This is a normal resizable window.", className="text-gray-600 mb-4"))
        content.add(Button(
            "Close This Window",
            className="px-4 py-2 bg-red-500 text-white rounded",
            onclick=lambda: self.close_window(window_id)
        ))
        
        window.add_child(content)
        self.windows[window_id] = window
        self.update_window_list()
    
    def create_dialog_window(self):
        """Create a dialog window"""
        self.window_counter += 1
        window_id = f"dialog_{self.window_counter}"
        
        window = self.app.create_window(
            title=f"Dialog {self.window_counter}",
            size=(300, 200),
            position=(350, 250),
            resizable=False,
            maximizable=False,
            on_top=True
        )
        
        content = Container(className="p-6 text-center")
        content.add(Text(f"Dialog {self.window_counter}", className="text-lg font-bold mb-2"))
        content.add(Text("This is a modal dialog.", className="text-gray-600 mb-4"))
        
        buttons = Container(className="flex space-x-2 justify-center")
        buttons.add(Button("OK", className="px-4 py-2 bg-blue-500 text-white rounded"))
        buttons.add(Button(
            "Cancel",
            className="px-4 py-2 bg-gray-300 rounded",
            onclick=lambda: self.close_window(window_id)
        ))
        
        content.add(buttons)
        window.add_child(content)
        self.windows[window_id] = window
        self.update_window_list()
    
    def create_tool_window(self):
        """Create a tool window"""
        self.window_counter += 1
        window_id = f"tool_{self.window_counter}"
        
        window = self.app.create_window(
            title=f"Tools {self.window_counter}",
            size=(200, 400),
            position=(50, 150),
            maximizable=False
        )
        
        content = Container(className="p-4")
        content.add(Text(f"Tool Palette {self.window_counter}", className="text-sm font-bold mb-3"))
        
        tools = Container(className="space-y-1")
        for i in range(5):
            tools.add(Button(
                f"Tool {i+1}",
                className="w-full px-2 py-1 bg-gray-200 rounded text-xs"
            ))
        
        content.add(tools)
        window.add_child(content)
        self.windows[window_id] = window
        self.update_window_list()
    
    def close_window(self, window_id):
        """Close a specific window"""
        if window_id in self.windows:
            self.windows[window_id].close()
            del self.windows[window_id]
            self.update_window_list()
    
    def update_window_list(self):
        """Update the window list display"""
        self.window_list.children.clear()
        
        if not self.windows:
            self.window_list.add(Text("No additional windows", className="text-sm text-gray-500"))
        else:
            for window_id, window in self.windows.items():
                window_info = Container(className="flex justify-between items-center p-2 bg-gray-100 rounded")
                window_info.add(Text(window.title, className="text-sm"))
                window_info.add(Button(
                    "Close",
                    className="px-2 py-1 bg-red-500 text-white rounded text-xs",
                    onclick=lambda wid=window_id: self.close_window(wid)
                ))
                self.window_list.add(window_info)
    
    def run(self):
        self.app.run()

# Usage
manager = MultiWindowManager()
manager.run()
```

## Window Lifecycle

### Creation and Initialization

```python
from oneforall import App, Container, Text

# 1. Create app
app = App()

# 2. Create window
window = app.create_window("My App", (600, 400))

# 3. Build content
content = Container(className="p-6")
content.add(Text("Window Content"))

# 4. Add content to window
window.add_child(content)

# 5. Run app (shows all windows)
app.run()
```

### Window States

```python
# Show/Hide
window.show()    # Make window visible
window.hide()    # Hide window (but keep in memory)

# Focus Management
window.focus()   # Bring window to front

# Size States
window.minimize()  # Minimize window
window.maximize()  # Maximize window (if maximizable)
window.restore()   # Restore from minimized/maximized

# Final State
window.close()     # Close and destroy window
```

## Best Practices

### Window Configuration

```python
# ✅ Good: Configure windows appropriately for their purpose
main_window = app.create_window(
    title="Main Application",
    size=(1000, 700),
    resizable=True,
    minimizable=True,
    maximizable=True
)

dialog_window = app.create_window(
    title="Settings",
    size=(400, 300),
    resizable=False,
    maximizable=False,
    on_top=True
)

tool_window = app.create_window(
    title="Tools",
    size=(200, 500),
    maximizable=False
)
```

### Content Management

```python
# ✅ Good: Use a single root container
root_container = Container(className="flex flex-col h-full")

# Add sections to root container
header = Container(className="bg-gray-100 p-4")
content = Container(className="flex-1 p-6")
footer = Container(className="bg-gray-200 p-2")

root_container.add(header)
root_container.add(content)
root_container.add(footer)

window.add_child(root_container)

# ❌ Avoid: Multiple root components (only the last one will be used)
window.add_child(header)   # This will be replaced
window.add_child(content)  # This will be replaced
window.add_child(footer)   # Only this will be shown
```

### Memory Management

```python
class WindowManager:
    def __init__(self):
        self.app = App()
        self.active_windows = {}
    
    def create_window(self, window_id, title, size):
        """Create and track a window"""
        if window_id in self.active_windows:
            # Window already exists, focus it instead
            self.active_windows[window_id].focus()
            return self.active_windows[window_id]
        
        window = self.app.create_window(title, size)
        self.active_windows[window_id] = window
        return window
    
    def close_window(self, window_id):
        """Close and cleanup a window"""
        if window_id in self.active_windows:
            self.active_windows[window_id].close()
            del self.active_windows[window_id]
    
    def cleanup_all(self):
        """Close all managed windows"""
        for window_id in list(self.active_windows.keys()):
            self.close_window(window_id)
```

## Related APIs

- [App API](./app) - Application management and window creation
- [Components API](./components) - UI components for window content
- [CLI API](./cli) - Command-line tools for development

## Examples

See the [Multiple Windows Tutorial](../tutorial-basics/multiple-windows) for comprehensive examples and patterns.

---

The Window class provides complete control over individual application windows, enabling you to create sophisticated multi-window desktop applications with OneForAll.