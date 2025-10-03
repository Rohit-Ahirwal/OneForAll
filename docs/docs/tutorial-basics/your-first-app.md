---
sidebar_position: 1
---

# Your First App

Let's create your first OneForAll application! In this tutorial, you'll build a simple counter app that demonstrates the core concepts of OneForAll development.

## Prerequisites

Make sure you have OneForAll installed:

```bash
pip install oneforall
```

## Creating the Project

First, let's create a new OneForAll project:

```bash
oneforall init my-first-app
cd my-first-app
```

This creates a basic project structure with an `app.py` file.

## Understanding the Basic Structure

Let's look at the generated `app.py`:

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

## Key Concepts

### 1. App Instance

```python
app = App()
```

The `App` class is the main entry point. It manages windows, state, and the application lifecycle.

### 2. State Management

```python
app.use_state("message", "Welcome to OneForAll!")
```

State variables hold your application's data. When state changes, the UI automatically updates.

### 3. Windows

```python
window = Window(title="OneForAll App", size=(600, 400))
```

Windows are containers for your UI components. You can have multiple windows in one app.

### 4. Components

```python
container = Container(className="p-8 text-center space-y-4")
text = Text(app.use_state("message"), className="text-2xl font-bold")
button = Button("Click Me", on_click=change_message)
```

Components are the building blocks of your UI. OneForAll provides built-in components like `Text`, `Button`, and `Container`.

### 5. Event Handling

```python
def change_message():
    app.set_state("message", "Hello from OneForAll!")

button = Button("Click Me", on_click=change_message)
```

Event handlers are functions that respond to user interactions. They typically update state to trigger UI changes.

## Building a Counter App

Let's modify the app to create a counter:

```python
from oneforall import App, Window, Text, Button, Container

# Create application
app = App()

# Initialize counter state
app.use_state("counter", 0)

# Create main window
window = Window(title="Counter App", size=(400, 300))

# Create UI container
container = Container(className="p-8 text-center space-y-6")

# Add title
container.add(Text("Counter App", className="text-3xl font-bold text-gray-800"))

# Add counter display
counter_display = Text(
    f"Count: {app.use_state('counter')}", 
    className="text-2xl font-mono bg-gray-100 px-4 py-2 rounded"
)
container.add(counter_display)

# Button container
button_container = Container(className="flex space-x-4 justify-center")

# Decrement button
def decrement():
    current = app.use_state("counter")
    app.set_state("counter", current - 1)

button_container.add(Button(
    "−", 
    on_click=decrement,
    className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-6 rounded text-xl"
))

# Reset button
def reset():
    app.set_state("counter", 0)

button_container.add(Button(
    "Reset", 
    on_click=reset,
    className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
))

# Increment button
def increment():
    current = app.use_state("counter")
    app.set_state("counter", current + 1)

button_container.add(Button(
    "+", 
    on_click=increment,
    className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-6 rounded text-xl"
))

container.add(button_container)

# Add window to app
window.add_child(container)
app.append(window)

# Run the application
if __name__ == "__main__":
    app.run()
```

## Running Your App

Start the development server:

```bash
oneforall dev
```

This starts your app with hot reload enabled. Any changes you make to the code will automatically refresh the app.

## What's Happening?

1. **State Initialization**: We create a `counter` state variable with initial value `0`
2. **UI Creation**: We build a hierarchy of components (Container → Text, Buttons)
3. **Event Handlers**: Button clicks call functions that update the counter state
4. **Reactive Updates**: When state changes, components that use that state automatically re-render

## Adding More Features

Let's add a feature to track the number of button clicks:

```python
# Add to your state initialization
app.use_state("counter", 0)
app.use_state("total_clicks", 0)

# Modify your event handlers
def decrement():
    current = app.use_state("counter")
    clicks = app.use_state("total_clicks")
    app.set_state("counter", current - 1)
    app.set_state("total_clicks", clicks + 1)

def increment():
    current = app.use_state("counter")
    clicks = app.use_state("total_clicks")
    app.set_state("counter", current + 1)
    app.set_state("total_clicks", clicks + 1)

def reset():
    app.set_state("counter", 0)
    # Don't reset total_clicks to keep the history

# Add a clicks display
container.add(Text(
    f"Total clicks: {app.use_state('total_clicks')}", 
    className="text-sm text-gray-600"
))
```

## Styling with Tailwind CSS

OneForAll includes Tailwind CSS for styling. You can use any Tailwind classes:

```python
# Gradient background
container = Container(className="p-8 text-center space-y-6 bg-gradient-to-br from-blue-400 to-purple-600 min-h-screen")

# Styled counter display
counter_display = Text(
    f"Count: {app.use_state('counter')}", 
    className="text-4xl font-bold text-white bg-black bg-opacity-20 px-6 py-3 rounded-lg shadow-lg"
)

# Modern buttons
increment_btn = Button(
    "+", 
    on_click=increment,
    className="bg-white text-purple-600 hover:bg-purple-50 font-bold py-3 px-8 rounded-full shadow-lg transform hover:scale-105 transition-all duration-200 text-2xl"
)
```

## Next Steps

Congratulations! You've built your first OneForAll app. Here's what you learned:

- ✅ How to create an app with `App()` and `Window()`
- ✅ How to manage state with `use_state()` and `set_state()`
- ✅ How to create UI with components like `Text`, `Button`, and `Container`
- ✅ How to handle user interactions with event handlers
- ✅ How to style components with Tailwind CSS

## What's Next?

- [State Management](./state-management) - Learn advanced state patterns
- [Creating Layouts](./creating-layouts) - Build complex UI layouts
- [Styling Guide](./styling) - Master Tailwind CSS styling
- [Multiple Windows](./multiple-windows) - Work with multiple windows

## Complete Code

Here's the complete counter app code:

```python
from oneforall import App, Window, Text, Button, Container

# Create application
app = App()

# Initialize state
app.use_state("counter", 0)
app.use_state("total_clicks", 0)

# Create main window
window = Window(title="Counter App", size=(400, 350))

# Create UI container
container = Container(className="p-8 text-center space-y-6 bg-gradient-to-br from-blue-400 to-purple-600 min-h-full")

# Add title
container.add(Text("Counter App", className="text-3xl font-bold text-white"))

# Add counter display
counter_display = Text(
    f"Count: {app.use_state('counter')}", 
    className="text-4xl font-bold text-white bg-black bg-opacity-20 px-6 py-3 rounded-lg shadow-lg"
)
container.add(counter_display)

# Button container
button_container = Container(className="flex space-x-4 justify-center")

# Decrement button
def decrement():
    current = app.use_state("counter")
    clicks = app.use_state("total_clicks")
    app.set_state("counter", current - 1)
    app.set_state("total_clicks", clicks + 1)

button_container.add(Button(
    "−", 
    on_click=decrement,
    className="bg-red-500 hover:bg-red-600 text-white font-bold py-3 px-6 rounded-full shadow-lg transform hover:scale-105 transition-all duration-200 text-xl"
))

# Reset button
def reset():
    app.set_state("counter", 0)

button_container.add(Button(
    "Reset", 
    on_click=reset,
    className="bg-gray-600 hover:bg-gray-700 text-white font-bold py-3 px-4 rounded-full shadow-lg transform hover:scale-105 transition-all duration-200"
))

# Increment button
def increment():
    current = app.use_state("counter")
    clicks = app.use_state("total_clicks")
    app.set_state("counter", current + 1)
    app.set_state("total_clicks", clicks + 1)

button_container.add(Button(
    "+", 
    on_click=increment,
    className="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-full shadow-lg transform hover:scale-105 transition-all duration-200 text-xl"
))

container.add(button_container)

# Add clicks counter
container.add(Text(
    f"Total clicks: {app.use_state('total_clicks')}", 
    className="text-sm text-white opacity-80"
))

# Add window to app
window.add_child(container)
app.append(window)

# Run the application
if __name__ == "__main__":
    app.run()
```