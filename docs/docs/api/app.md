---
sidebar_position: 1
---

# App

The `App` class is the main entry point for OneForAll applications. It manages windows, state, and the overall application lifecycle.

## Constructor

```python
from oneforall import App

app = App()
```

Creates a new OneForAll application instance.

## Methods

### `append(window)`

Adds a window to the application.

**Parameters:**
- `window` (Window): The window instance to add to the application

**Example:**
```python
from oneforall import App, Window

app = App()
window = Window(title="My Window")
app.append(window)
```

### `run(dev_mode=True, dev_tool=False)`

Starts the application and displays all registered windows.

**Parameters:**
- `dev_mode` (bool, optional): Enable development mode with hot reload. Defaults to `True`
- `dev_tool` (bool, optional): Enable developer tools in webview. Defaults to `False`

**Example:**
```python
app.run(dev_mode=True, dev_tool=True)
```

### `use_state(key, default=None)`

Creates or retrieves a state variable.

**Parameters:**
- `key` (str): The state key identifier
- `default` (any, optional): Default value if state doesn't exist. Defaults to `None`

**Returns:**
- The current value of the state variable

**Example:**
```python
count = app.use_state("count", 0)
user_name = app.use_state("user_name", "Anonymous")
```

### `set_state(key, value)`

Updates a state variable and triggers reactive updates.

**Parameters:**
- `key` (str): The state key to update
- `value` (any): The new value for the state

**Example:**
```python
app.set_state("count", 42)
app.set_state("user_name", "John Doe")
```

### `use_effect(key, callback)`

Registers an effect callback that runs when specified state changes.

**Parameters:**
- `key` (str or list): State key(s) to watch for changes
- `callback` (function): Function to call when state changes

**Example:**
```python
def on_count_change():
    print(f"Count changed to: {app.use_state('count')}")

app.use_effect("count", on_count_change)

# Watch multiple keys
app.use_effect(["count", "user_name"], on_count_change)
```

### `refresh()`

Manually triggers a refresh of all windows and their components.

**Example:**
```python
app.refresh()
```

## Properties

### `windows`

A list of all windows registered with the application.

**Type:** `List[Window]`

### `state`

The state manager instance for this application.

**Type:** `StateManager`

### `bridge`

The bridge instance for handling Python ↔ JavaScript communication.

**Type:** `OneForAllBridge`

## Complete Example

```python
from oneforall import App, Window, Text, Button, Container

# Create application
app = App()

# Initialize state
app.use_state("counter", 0)
app.use_state("message", "Hello OneForAll!")

# Create main window
with Window(title="Counter App", size=(400, 300)) as window:
    # Add container for layout
    container = Container(className="p-4 space-y-4")
    
    # Add message text
    container.add(Text(
        app.use_state("message"), 
        className="text-xl font-bold text-center"
    ))
    
    # Add counter display
    container.add(Text(
        f"Count: {app.use_state('counter')}", 
        className="text-lg text-center"
    ))
    
    # Add increment button
    def increment():
        current = app.use_state("counter")
        app.set_state("counter", current + 1)
    
    container.add(Button(
        "Increment", 
        on_click=increment,
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    ))
    
    # Add reset button
    def reset():
        app.set_state("counter", 0)
    
    container.add(Button(
        "Reset", 
        on_click=reset,
        className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
    ))
    
    window.add_child(container)

# Add window to app
app.append(window)

# Set up effect to log counter changes
def log_counter_change():
    count = app.use_state("counter")
    print(f"Counter is now: {count}")

app.use_effect("counter", log_counter_change)

# Run the application
if __name__ == "__main__":
    app.run(dev_mode=True)
```

## See Also

- [Window](./window) - Create and manage application windows
- [State Management](../tutorial-basics/state-management) - Learn about reactive state
- [Components](./components) - Available UI components