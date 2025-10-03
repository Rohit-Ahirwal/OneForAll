---
sidebar_position: 1
---

# Getting Started with OneForAll

Welcome to **OneForAll** - the industry-grade Python GUI framework that lets you build desktop applications using pure Python and web technologies.

## What is OneForAll?

OneForAll is a modern Python GUI framework inspired by Electron, but designed specifically for Python developers. It combines the power of Python with the flexibility of web technologies to create beautiful, responsive desktop applications.

### Key Features

- **Pure Python Development**: Write your entire application in Python - no JavaScript, HTML, or CSS required
- **React-like Components**: Familiar component-based architecture with built-in components like `Text`, `Button`, `Container`, and `Image`
- **Reactive State Management**: Automatic dependency tracking and partial UI updates for optimal performance
- **Tailwind CSS Support**: Built-in styling with Tailwind CSS utilities
- **Hot Reload**: Fast development with automatic reloading during development
- **Multiple Windows**: Support for multiple application windows
- **CLI Tools**: Powerful command-line tools for project scaffolding, development, and building

## Quick Start

### Installation

Install OneForAll using pip:

```bash
pip install oneforall
```

### Create Your First App

1. **Initialize a new project:**

```bash
oneforall init my_app
cd my_app
```

2. **Run the development server:**

```bash
oneforall dev
```

3. **Your first OneForAll app:**

```python
from oneforall import App, Window, Text, Button

# Create the main app
app = App()

# Create a window
with Window(title="My First OneForAll App", size=(800, 600)) as window:
    # Add components
    window.add_child(Text("Hello from OneForAll!", className="text-2xl font-bold"))
    
    def handle_click(payload):
        print("Button clicked!", payload)
    
    window.add_child(Button("Click Me", on_click=handle_click))

# Add window to app
app.append(window)

# Run the application
if __name__ == "__main__":
    app.run(dev_mode=True)
```

## Core Concepts

### Components

OneForAll provides several built-in components:

- **Text**: Display text content
- **Button**: Interactive buttons with click handlers
- **Container**: Group and layout other components
- **Image**: Display images

### State Management

OneForAll features automatic reactive state management:

```python
from oneforall import App, Window, Text, Button

app = App()

# Use state
count = app.use_state("count", 0)

def increment():
    app.set_state("count", count + 1)

with Window(title="Counter App") as window:
    window.add_child(Text(f"Count: {count}"))
    window.add_child(Button("Increment", on_click=increment))

app.append(window)
app.run()
```

### Windows

Create multiple windows for complex applications:

```python
from oneforall import App, Window, Text

app = App()

# Main window
with Window(title="Main Window", size=(800, 600)) as main_window:
    main_window.add_child(Text("This is the main window"))

# Settings window
with Window(title="Settings", size=(400, 300)) as settings_window:
    settings_window.add_child(Text("Application Settings"))

app.append(main_window)
app.append(settings_window)
app.run()
```

## CLI Commands

OneForAll provides several CLI commands to help with development:

- `oneforall init <name>` - Create a new OneForAll project
- `oneforall dev <file>` - Run development server with hot reload
- `oneforall build <file>` - Build standalone executable
- `oneforall generate <name> <type>` - Generate component templates

## Next Steps

- [Learn about Components](./tutorial-basics/components)
- [Explore State Management](./tutorial-basics/state-management)
- [Check out the API Reference](./api/app)
- [See Examples](./examples)

## Need Help?

- [GitHub Issues](https://github.com/oneforall/oneforall/issues)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/oneforall)
- [Discord Community](https://discord.gg/oneforall)

---

Ready to build amazing desktop applications with Python? Let's get started! 🚀
