# OneForAll

Build desktop apps with Python and Tailwind CSS.

## Installation

```bash
pip install oneforall
```

## Quick Start

Create a new app:
```bash
oneforall init my_app
cd my_app
oneforall dev example_basic.py
```

## Basic Example

```python
from oneforall import App, Window
from oneforall.components import Container, Text, Button

# Create app and window
app = App()
window = Window(title="My App", size=(600, 400))

# Create container
container = Container(className="p-8 space-y-4")

# Add text
title = Text("Hello, World!", className="text-2xl font-bold text-blue-600")
container.add(title)

# Add button with click handler
def handle_click():
    title.text = "Button was clicked!"

button = Button(
    "Click Me", 
    on_click=handle_click,
    className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
)
container.add(button)

# Add container to window and run
window.add_child(container)
app.windows.append(window)

if __name__ == "__main__":
    app.run(dev_mode=True)
```

## Components

### Text
```python
text = Text("Hello", className="text-lg font-bold")
```

### Button
```python
def click_handler():
    print("Clicked!")

button = Button("Click Me", on_click=click_handler, className="px-4 py-2 bg-blue-500 text-white rounded")
```

### Container
```python
container = Container(className="p-4 space-y-2")
container.add(text)
container.add(button)
```

## Styling

OneForAll uses [Tailwind CSS](https://tailwindcss.com/) for styling. All Tailwind classes work:

```python
# Flexbox layout
container = Container(className="flex items-center justify-center h-screen")

# Styling text
title = Text("Welcome", className="text-3xl font-bold text-gray-800")

# Button variants
primary_btn = Button("Primary", className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded")
danger_btn = Button("Delete", className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded")
```

## State Management

Use built-in state for dynamic UIs:

```python
app = App()

# Initialize state
counter = app.use_state('counter', 0)

# Create UI
count_text = Text(f"Count: {counter}", className="text-xl")

def increment():
    current = app.use_state('counter', 0)
    app.set_state('counter', current + 1)

button = Button("Increment", on_click=increment)
```

## CLI Commands

### Development
```bash
oneforall dev example_basic.py          # Run with hot reload
```

### Project Setup
```bash
oneforall init my_project      # Create new project
```

### Build
```bash
oneforall build example_basic.py        # Create executable
```

## Example Apps

### Counter App
```python
from oneforall import App, Window
from oneforall.components import Container, Text, Button

app = App()
window = Window(title="Counter", size=(300, 200))
container = Container(className="p-8 text-center space-y-4")

count = app.use_state('count', 0)
count_display = Text(f"Count: {count}", className="text-2xl font-bold")

def increment():
    current = app.use_state('count', 0)
    app.set_state('count', current + 1)

def decrement():
    current = app.use_state('count', 0)
    app.set_state('count', current - 1)

container.add(count_display)
container.add(Button("+", on_click=increment, className="mx-2 px-4 py-2 bg-green-500 text-white rounded"))
container.add(Button("-", on_click=decrement, className="mx-2 px-4 py-2 bg-red-500 text-white rounded"))

window.add_child(container)
app.windows.append(window)

if __name__ == "__main__":
    app.run(dev_mode=True)
```

### Todo List
```python
from oneforall import App, Window
from oneforall.components import Container, Text, Button

app = App()
window = Window(title="Todo App", size=(400, 500))
container = Container(className="p-6 space-y-4")

todos = app.use_state('todos', ["Learn OneForAll", "Build awesome app"])

# Display todos
for i, todo in enumerate(todos):
    todo_container = Container(className="flex justify-between items-center p-2 bg-gray-100 rounded")
    todo_container.add(Text(todo, className="flex-1"))
    
    def remove_todo(index=i):
        current_todos = app.use_state('todos', [])
        new_todos = current_todos[:index] + current_todos[index+1:]
        app.set_state('todos', new_todos)
    
    todo_container.add(Button("Remove", on_click=remove_todo, className="px-2 py-1 bg-red-500 text-white rounded text-sm"))
    container.add(todo_container)

window.add_child(container)
app.windows.append(window)

if __name__ == "__main__":
    app.run(dev_mode=True)
```

## Custom Components

Create reusable components:

```python
# components/card.py
from oneforall.components import Container, Text

def Card(title, content, className=""):
    card = Container(className=f"p-6 bg-white rounded-lg shadow-md {className}")
    card.add(Text(title, className="text-xl font-bold mb-2"))
    card.add(Text(content, className="text-gray-600"))
    return card

# Use it
from components.card import Card

card = Card(
    title="Welcome", 
    content="This is a custom card component",
    className="max-w-sm mx-auto"
)
```

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/Rohit-Ahirwal/oneforall/issues)
- **Email**: lucifer@codewithlucifer.com
- **Tailwind CSS**: [Documentation](https://tailwindcss.com/docs)

## License

This project is licensed under the [Apache License 2.0](./LICENSE).

You are free to use this framework in commercial and non-commercial projects.  
Apps built with this framework can be proprietary or open-source.  
The project name and branding are owned by Rohit Ahirwal and may not be used  
to imply official affiliation without permission.


---

**Built by [Rohit Ahirwal](https://github.com/rohitahirwal)**
