---
sidebar_position: 2
---

# Window

The `Window` class represents an application window in OneForAll. Each window can contain components and has its own properties like title, size, and position.

## Constructor

```python
from oneforall import Window

window = Window(
    title="My Window",
    size=(800, 600),
    position=(100, 100),
    resizable=True,
    minimizable=True,
    maximizable=True
)
```

**Parameters:**
- `title` (str, optional): Window title. Defaults to `"OneForAll App"`
- `size` (tuple, optional): Window size as `(width, height)`. Defaults to `(800, 600)`
- `position` (tuple, optional): Window position as `(x, y)`. Defaults to `(100, 100)`
- `resizable` (bool, optional): Whether window can be resized. Defaults to `True`
- `minimizable` (bool, optional): Whether window can be minimized. Defaults to `True`
- `maximizable` (bool, optional): Whether window can be maximized. Defaults to `True`

## Methods

### `add_child(component)`

Adds a component to the window.

**Parameters:**
- `component` (Component): The component to add to the window

**Example:**
```python
from oneforall import Window, Text

window = Window(title="Hello World")
text = Text("Hello, OneForAll!")
window.add_child(text)
```

### `remove_child(component)`

Removes a component from the window.

**Parameters:**
- `component` (Component): The component to remove from the window

**Example:**
```python
window.remove_child(text)
```

### `clear_children()`

Removes all components from the window.

**Example:**
```python
window.clear_children()
```

### `refresh()`

Manually triggers a refresh of the window and all its components.

**Example:**
```python
window.refresh()
```

### `close()`

Closes the window.

**Example:**
```python
window.close()
```

### `show()`

Shows the window if it's hidden.

**Example:**
```python
window.show()
```

### `hide()`

Hides the window.

**Example:**
```python
window.hide()
```

### `minimize()`

Minimizes the window.

**Example:**
```python
window.minimize()
```

### `maximize()`

Maximizes the window.

**Example:**
```python
window.maximize()
```

### `restore()`

Restores the window from minimized or maximized state.

**Example:**
```python
window.restore()
```

## Properties

### `title`

The window title.

**Type:** `str`

```python
window.title = "New Title"
print(window.title)  # "New Title"
```

### `size`

The window size as a tuple `(width, height)`.

**Type:** `tuple`

```python
window.size = (1024, 768)
print(window.size)  # (1024, 768)
```

### `position`

The window position as a tuple `(x, y)`.

**Type:** `tuple`

```python
window.position = (200, 150)
print(window.position)  # (200, 150)
```

### `children`

List of all components in the window.

**Type:** `List[Component]`

```python
print(len(window.children))  # Number of components
```

### `webview`

The underlying pywebview window instance.

**Type:** `webview.Window`

## Context Manager Usage

Windows can be used as context managers for cleaner code:

```python
from oneforall import App, Window, Text, Container

app = App()

with Window(title="Context Manager Example", size=(600, 400)) as window:
    container = Container(className="p-4")
    container.add(Text("This window was created using a context manager!"))
    window.add_child(container)

app.append(window)
app.run()
```

## Multiple Windows Example

```python
from oneforall import App, Window, Text, Button

app = App()

# Main window
main_window = Window(title="Main Window", size=(400, 300))
main_window.add_child(Text("This is the main window", className="text-center p-4"))

def open_second_window():
    # Create second window
    second_window = Window(title="Second Window", size=(300, 200), position=(450, 150))
    second_window.add_child(Text("This is a second window!", className="text-center p-4"))
    
    # Add to app
    app.append(second_window)

# Button to open second window
open_btn = Button("Open Second Window", on_click=open_second_window)
main_window.add_child(open_btn)

app.append(main_window)
app.run()
```

## Window Events

You can handle window events by accessing the underlying webview:

```python
def on_window_close():
    print("Window is closing!")
    # Perform cleanup here

window.webview.events.closing += on_window_close
```

## Responsive Layout Example

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Create responsive window
window = Window(
    title="Responsive Layout",
    size=(800, 600),
    resizable=True
)

# Main container with responsive classes
main_container = Container(className="h-full flex flex-col")

# Header
header = Container(className="bg-blue-500 text-white p-4")
header.add(Text("OneForAll App", className="text-2xl font-bold"))
main_container.add(header)

# Content area
content = Container(className="flex-1 p-4 overflow-auto")
content.add(Text("Main content area", className="text-lg"))
main_container.add(content)

# Footer
footer = Container(className="bg-gray-200 p-2 text-center")
footer.add(Text("© 2024 OneForAll", className="text-sm"))
main_container.add(footer)

window.add_child(main_container)
app.append(window)
app.run()
```

## See Also

- [App](./app) - Main application class
- [Components](./components) - Available UI components
- [Layout Tutorial](../tutorial-basics/creating-layouts) - Learn about creating layouts