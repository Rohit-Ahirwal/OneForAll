---
sidebar_position: 1
---

# Getting Started with OneForAll

Welcome to **OneForAll** - a lightweight Python GUI framework that lets you build modern desktop applications using Python and Tailwind CSS. 

:::info Alpha Version
OneForAll is currently in **alpha** stage (v0.1.0a3). While the core functionality is stable, the API may change in future releases. We recommend using it for prototyping and experimental projects.
:::

## What is OneForAll?

OneForAll combines the power of `pywebview` with a React-like component system and built-in state management to create beautiful desktop applications entirely in Python. No need to learn JavaScript, HTML, or CSS - just pure Python with modern styling capabilities.

### Key Features

- 🐍 **Pure Python** - Write your entire app in Python
- 🎨 **Tailwind CSS Integration** - Modern, utility-first styling out of the box
- ⚡ **Hot Reload** - Live reload during development for faster iteration
- 🧩 **Component-Based** - Reusable UI components with React-like patterns
- 📱 **Reactive State Management** - Built-in state system with automatic UI updates
- 🔧 **CLI Tools** - Scaffold, develop, and build apps easily
- 📦 **Build Ready** - Generate standalone executables with PyInstaller
- 🪟 **Multi-Window Support** - Create complex applications with multiple windows

## Quick Start

### Installation

Install OneForAll using pip:

```bash
pip install oneforall-gui
```

### Create Your First App

1. **Initialize a new project:**

```bash
oneforall init my_app
cd my_app
```

2. **Run the development server:**

```bash
oneforall dev example_basic.py
```

3. **Your first OneForAll app:**

```python
from oneforall import App, Text, Button, Container

# Create the main app
app = App()

# Create a window
window = app.create_window(title="My First OneForAll App", size=(800, 600))

# Create components with Tailwind CSS classes
container = Container(className="p-8 space-y-4 bg-gray-50 min-h-screen")
title = Text("Hello, OneForAll! 🚀", className="text-3xl font-bold text-blue-600")

# State management
counter_state = app.use_state('counter', 0)

def increment():
    current = app.get_state('counter')
    app.set_state('counter', current + 1)

counter_text = Text(f"Count: {counter_state}", className="text-xl text-gray-700")
button = Button(
    "Increment", 
    on_click=increment, 
    className="px-6 py-3 bg-blue-500 hover:bg-blue-600 text-white rounded-lg font-medium transition-colors"
)

# Build UI hierarchy
container.add(title)
container.add(counter_text)
container.add(button)
window.add_child(container)

# Run the application
if __name__ == "__main__":
    app.run(dev_mode=True)
```

## Core Concepts

### 1. App & Windows

The `App` is the main entry point for your OneForAll application. You can create multiple windows for complex applications:

```python
from oneforall import App

app = App()
main_window = app.create_window(title="Main Window", size=(800, 600))
settings_window = app.create_window(title="Settings", size=(400, 300))
```

### 2. Components

OneForAll provides several built-in components that you can use to build your UI:

- **Text**: Display text content with styling
- **Button**: Interactive buttons with click handlers
- **Container**: Group and layout other components
- **Image**: Display images with automatic embedding

### 3. State Management

OneForAll includes built-in reactive state management that automatically updates your UI when state changes:

```python
# Initialize state
count = app.use_state('count', 0)

# Update state (triggers automatic UI refresh)
def increment():
    current = app.get_state('count')
    app.set_state('count', current + 1)

# Use state in components
counter_display = Text(f"Count: {count}")
```

### 4. Styling with Tailwind CSS

OneForAll comes with Tailwind CSS built-in, allowing you to style your components with utility classes:

```python
# Modern card-like container
card = Container(className="bg-white rounded-lg shadow-lg p-6 max-w-md mx-auto")

# Styled button with hover effects
button = Button(
    "Click Me", 
    className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white font-bold py-2 px-4 rounded-full transition-all duration-300"
)
```

## CLI Commands

OneForAll includes a powerful CLI for development and deployment:

### Project Management
- `oneforall init <name>` - Create a new OneForAll project
- `oneforall dev <file>` - Run development server with hot reload
- `oneforall build <file>` - Build standalone executable

### Development Tools
- `oneforall css` - Build custom Tailwind CSS
- `oneforall generate <name> <type>` - Generate component templates

## Alpha Version Notes

As OneForAll is in alpha, please keep in mind:

- **API Stability**: The API may change in future releases
- **Documentation**: Some advanced features may not be fully documented yet
- **Community**: We're building our community - your feedback is valuable!
- **Production Use**: Recommended for prototyping and experimental projects

## What's Next?

- [Learn about Components](./tutorial-basics/components) - Dive into the component system
- [Explore State Management](./tutorial-basics/state-management) - Master reactive state
- [Check out the API Reference](./api/app) - Complete API documentation
- [See Examples](./examples) - Real-world examples and patterns

## Need Help?

- [GitHub Issues](https://github.com/Rohit-Ahirwal/oneforall/issues) - Report bugs or request features
- [GitHub Discussions](https://github.com/Rohit-Ahirwal/oneforall/discussions) - Ask questions and share ideas

---

Ready to build amazing desktop applications with Python? Let's get started! 🚀