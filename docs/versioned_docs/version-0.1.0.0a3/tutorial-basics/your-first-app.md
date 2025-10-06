---
sidebar_position: 1
---

# Your First OneForAll App

Let's build your first desktop application with OneForAll! This tutorial will guide you through creating a simple counter app that demonstrates the core concepts of the framework.

:::info Alpha Version
OneForAll is currently in **alpha** (v0.1.0a3). The API is stable for basic usage but may evolve in future releases.
:::

## Prerequisites

Before we start, make sure you have:

- Python 3.9 or higher installed
- Basic knowledge of Python programming
- A code editor of your choice

## Installation

First, install OneForAll using pip:

```bash
pip install oneforall-gui
```

## Project Setup

Create a new directory for your project and initialize it:

```bash
mkdir my-first-app
cd my-first-app
oneforall init .
```

This creates a basic project structure with an example file.

## Building the Counter App

Let's create a simple counter application step by step.

### Step 1: Import Required Components

Create a new file called `counter_app.py` and start with the imports:

```python
from oneforall import App, Text, Button, Container
```

### Step 2: Create the App Instance

```python
from oneforall import App, Text, Button, Container

# Create the main application instance
app = App()
```

### Step 3: Create a Window

```python
from oneforall import App, Text, Button, Container

app = App()

# Create a window with title and size
window = app.create_window(
    title="My Counter App", 
    size=(400, 300)
)
```

### Step 4: Add Components with Styling

Now let's add our UI components with Tailwind CSS styling:

```python
from oneforall import App, Text, Button, Container

app = App()
window = app.create_window(title="My Counter App", size=(400, 300))

# Create a main container with padding and background
main_container = Container(className="p-8 bg-gray-50 min-h-screen flex flex-col items-center justify-center space-y-6")

# Add a title
title = Text(
    "Counter App", 
    className="text-3xl font-bold text-gray-800 mb-4"
)

# Initialize counter state
counter_value = app.use_state('counter', 0)

# Display current counter value
counter_display = Text(
    f"Count: {counter_value}", 
    className="text-2xl font-semibold text-blue-600"
)
```

### Step 5: Add Interactive Functionality

Let's add buttons to increment and decrement the counter:

```python
from oneforall import App, Text, Button, Container

app = App()
window = app.create_window(title="My Counter App", size=(400, 300))

main_container = Container(className="p-8 bg-gray-50 min-h-screen flex flex-col items-center justify-center space-y-6")

title = Text("Counter App", className="text-3xl font-bold text-gray-800 mb-4")

counter_value = app.use_state('counter', 0)
counter_display = Text(f"Count: {counter_value}", className="text-2xl font-semibold text-blue-600")

# Define event handlers
def increment():
    current = app.get_state('counter')
    app.set_state('counter', current + 1)

def decrement():
    current = app.get_state('counter')
    app.set_state('counter', current - 1)

def reset():
    app.set_state('counter', 0)

# Create buttons
increment_btn = Button(
    "Increment", 
    on_click=increment,
    className="px-6 py-3 bg-green-500 hover:bg-green-600 text-white rounded-lg font-medium transition-colors"
)

decrement_btn = Button(
    "Decrement", 
    on_click=decrement,
    className="px-6 py-3 bg-red-500 hover:bg-red-600 text-white rounded-lg font-medium transition-colors"
)

reset_btn = Button(
    "Reset", 
    on_click=reset,
    className="px-6 py-3 bg-gray-500 hover:bg-gray-600 text-white rounded-lg font-medium transition-colors"
)

# Create button container
button_container = Container(className="flex space-x-4")
button_container.add(decrement_btn)
button_container.add(increment_btn)
button_container.add(reset_btn)
```

### Step 6: Build the UI Hierarchy

Now let's assemble all components:

```python
# Add components to main container
main_container.add(title)
main_container.add(counter_display)
main_container.add(button_container)

# Add main container to window
window.add_child(main_container)
```

### Step 7: Run the Application

Finally, add the code to run the app:

```python
# Run the application
if __name__ == "__main__":
    app.run(dev_mode=True)
```

## Complete Code

Here's the complete `counter_app.py` file:

```python
from oneforall import App, Text, Button, Container

# Create the main application instance
app = App()

# Create a window
window = app.create_window(title="My Counter App", size=(400, 300))

# Create main container
main_container = Container(className="p-8 bg-gray-50 min-h-screen flex flex-col items-center justify-center space-y-6")

# Add title
title = Text("Counter App", className="text-3xl font-bold text-gray-800 mb-4")

# Initialize and display counter
counter_value = app.use_state('counter', 0)
counter_display = Text(f"Count: {counter_value}", className="text-2xl font-semibold text-blue-600")

# Event handlers
def increment():
    current = app.get_state('counter')
    app.set_state('counter', current + 1)

def decrement():
    current = app.get_state('counter')
    app.set_state('counter', current - 1)

def reset():
    app.set_state('counter', 0)

# Create buttons
increment_btn = Button(
    "Increment", 
    on_click=increment,
    className="px-6 py-3 bg-green-500 hover:bg-green-600 text-white rounded-lg font-medium transition-colors"
)

decrement_btn = Button(
    "Decrement", 
    on_click=decrement,
    className="px-6 py-3 bg-red-500 hover:bg-red-600 text-white rounded-lg font-medium transition-colors"
)

reset_btn = Button(
    "Reset", 
    on_click=reset,
    className="px-6 py-3 bg-gray-500 hover:bg-gray-600 text-white rounded-lg font-medium transition-colors"
)

# Button container
button_container = Container(className="flex space-x-4")
button_container.add(decrement_btn)
button_container.add(increment_btn)
button_container.add(reset_btn)

# Build UI hierarchy
main_container.add(title)
main_container.add(counter_display)
main_container.add(button_container)
window.add_child(main_container)

# Run the application
if __name__ == "__main__":
    app.run(dev_mode=True)
```

## Running Your App

To run your counter app:

```bash
# Run directly
python counter_app.py

# Or use OneForAll CLI with hot reload
oneforall dev counter_app.py
```

The CLI version will automatically reload your app when you make changes to the code, making development faster and more efficient.

## What You've Learned

In this tutorial, you've learned:

1. **App Structure**: How to create an app and window
2. **Components**: Using Text, Button, and Container components
3. **State Management**: Using `use_state()`, `get_state()`, and `set_state()`
4. **Event Handling**: Creating click handlers for buttons
5. **Styling**: Using Tailwind CSS classes for modern UI design
6. **UI Hierarchy**: Building component trees and layouts

## Next Steps

Now that you've built your first app, you can:

- [Learn more about Components](./components) - Explore all available components
- [Master State Management](./state-management) - Advanced state patterns
- [Create Beautiful Layouts](./creating-layouts) - Layout techniques and patterns
- [Style with Tailwind](./styling) - Advanced styling techniques

## Troubleshooting

### Common Issues

**App doesn't start**: Make sure you have Python 3.9+ and all dependencies installed.

**Hot reload not working**: Ensure you're using `oneforall dev` command and the file path is correct.

**Styling not applied**: Verify your Tailwind CSS classes are correct and properly formatted.

---

Congratulations! You've successfully built your first OneForAll application. The counter app demonstrates the core concepts you'll use in more complex applications.