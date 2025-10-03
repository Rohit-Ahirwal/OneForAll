# OneForAll 🚀

**OneForAll** is a lightweight Python GUI framework that lets you build modern desktop applications using Python and Tailwind CSS. It combines the power of `pywebview` with a React-like component system and built-in state management.

## ✨ Features

- 🐍 **Pure Python** - Write your entire app in Python
- 🎨 **Tailwind CSS Integration** - Modern, utility-first styling
- ⚡ **Hot Reload** - Live reload during development
- 🧩 **Component-Based** - Reusable UI components
- 📱 **State Management** - Built-in reactive state system  
- 🔧 **CLI Tools** - Scaffold, develop, and build apps easily
- 📦 **Build Ready** - Generate standalone executables with PyInstaller

## 🚀 Quick Start

### Installation

```bash
pip install oneforall
```

### Create Your First App

```bash
# Scaffold a new project
oneforall init my_app
cd my_app

# Run in development mode
oneforall dev example_basic.py
```

### Hello World Example

```python
from oneforall import App, Text, Button, Container

# Create app
app = App()
window = app.create_window(title="My App")

# Create components
container = Container(className="p-8 space-y-4")
title = Text("Hello, OneForAll!", className="text-2xl font-bold")
counter_state = app.use_state('counter', 0)

def increment():
    current = app.get_state('counter')
    app.set_state('counter', current + 1)

counter_text = Text(f"Count: {counter_state}", className="text-lg")
button = Button("Increment", on_click=increment, className="px-4 py-2 bg-blue-500 text-white rounded")

# Build UI
container.add(title)
container.add(counter_text)  
container.add(button)
window.add_child(container)

# Run app
if __name__ == "__main__":
    app.run(dev_mode=True)
```

## 📖 Core Concepts

### 1. App & Windows

The `App` is the main entry point. You can create multiple windows:

```python
from oneforall import App, Window

app = App()
window = Window(title="My App", size=(800, 600))
app.windows.append(window)

# Or use the convenience method
window = app.create_window(title="My App", size=(800, 600))
```

### 2. Components

OneForAll provides several built-in components:

#### Text Component
```python
text = Text(
    "Hello World", 
    className="text-xl font-bold text-gray-800"
)
```

#### Button Component  
```python
def handle_click():
    print("Button clicked!")

button = Button(
    "Click Me",
    on_click=handle_click,
    className="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded"
)
```

#### Container Component
```python
container = Container(className="p-4 space-y-2 bg-gray-100")
container.add(text)
container.add(button)
```

### 3. State Management

OneForAll includes built-in reactive state management:

```python
# Initialize state
count = app.use_state('count', 0)

# Update state (triggers UI refresh)
def increment():
    current = app.get_state('count')
    app.set_state('count', current + 1)

# Use state in components
counter_display = Text(f"Count: {count}")
```

### 4. Custom Components

Create reusable components:

```python
# components/my_button.py
from oneforall.components import Button

def primary_button(label: str, on_click=None):
    return Button(
        label,
        on_click=on_click,
        className="px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-medium rounded-lg"
    )

def danger_button(label: str, on_click=None):
    return Button(
        label,
        on_click=on_click, 
        className="px-6 py-3 bg-red-600 hover:bg-red-700 text-white font-medium rounded-lg"
    )
```

## 🛠️ CLI Commands

OneForAll includes a powerful CLI for development and deployment:

### `oneforall init <name>`
Scaffold a new OneForAll project:

```bash
oneforall init my_awesome_app
cd my_awesome_app
```

### `oneforall dev <file>`
Run your app in development mode with hot reload:

```bash
# Run example_basic.py with live reload
oneforall dev example_basic.py

# Run a specific file
oneforall dev examples/todo_app.py
```

### `oneforall build <file>`
Build a standalone executable:

```bash
oneforall build example_basic.py --name="MyApp"
```

The built executable will be in the `dist/` folder.

### `oneforall generate <name> --type=<component>`
Generate component templates:

```bash
oneforall generate navbar --type=component
```

## 🎨 Styling with Tailwind CSS

OneForAll uses Tailwind CSS for styling. In development mode, it automatically loads Tailwind via CDN. For production builds, you can include a local Tailwind CSS file.

### Development Mode
```python
# Tailwind classes work out of the box
text = Text("Styled Text", className="text-3xl font-bold text-blue-600 hover:text-blue-800")
container = Container(className="flex items-center justify-center h-screen bg-gradient-to-r from-purple-400 to-pink-400")
```

### Production Mode  
Place a `tailwind.css` file in your project root, or OneForAll will use its built-in stylesheet:

```bash
# Install Tailwind CSS (optional, for custom builds)
npm install -D tailwindcss
npx tailwindcss init
```

## 📁 Project Structure

A typical OneForAll project looks like this:

```
my_app/
├── main.py              # Entry point
├── components/          # Custom components
│   ├── __init__.py
│   ├── button.py
│   └── navbar.py
├── assets/             # Static files
│   └── tailwind.css    # Custom Tailwind build (optional)
├── dist/               # Built executables
└── build/              # Build artifacts
```

## 🔄 Event Handling

OneForAll uses a bridge system to handle events between Python and the webview:

```python
def handle_button_click():
    print("Button was clicked!")
    # Update state
    app.set_state('message', 'Button clicked!')

# Event handlers are automatically registered
button = Button("Click Me", on_click=handle_button_click)
```

### Event Handler Best Practices

1. **Keep handlers simple** - Avoid complex operations
2. **Use state management** - Update UI through `app.set_state()`  
3. **Avoid direct DOM manipulation** - Let OneForAll handle re-rendering

```python
# ✅ Good
def good_handler():
    current_count = app.get_state('count')
    app.set_state('count', current_count + 1)

# ❌ Avoid - Direct DOM manipulation
def bad_handler():
    text.text = "Updated!"  # Can cause callback conflicts
```

## 🏗️ Architecture

OneForAll follows a clean architecture:

```
┌─────────────────┐
│   Your App      │ ← Python application code
├─────────────────┤  
│   OneForAll     │ ← Framework (components, state, etc.)
├─────────────────┤
│   PyWebView     │ ← Web rendering engine
├─────────────────┤
│   Tailwind CSS  │ ← Styling system
└─────────────────┘
```

- **App Layer**: Your Python application logic
- **Framework Layer**: OneForAll components, state management, and bridge
- **Rendering Layer**: PyWebView handles the web rendering
- **Styling Layer**: Tailwind CSS for modern, responsive design

## 🔧 Advanced Usage

### Custom Window Configuration

```python
window = Window(
    title="Advanced App",
    size=(1200, 800),
    min_size=(800, 600),
    resizable=True,
    on_top=False
)
```

### Multiple Windows

```python
app = App()

main_window = Window(title="Main Window")
settings_window = Window(title="Settings", size=(400, 300))

app.windows.extend([main_window, settings_window])
```

### Custom Tailwind Classes

```python
# Create your own utility classes
my_card = Container(className="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg space-y-4")
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyWebView](https://github.com/r0x0r/pywebview) - Web rendering engine
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Typer](https://github.com/tiangolo/typer) - CLI framework

## 📚 Examples

Check out the `/examples` directory for more complete applications:

- **Todo App** - Task management with state
- **Calculator** - Mathematical operations with component reuse  
- **Chat App** - Real-time messaging interface
- **Dashboard** - Data visualization with charts

## 🆘 Support

- 📖 [Documentation](https://oneforall-docs.example.com)
- 💬 [Discord Community](https://discord.gg/oneforall)
- 🐛 [Issue Tracker](https://github.com/Rohit-Ahirwal/oneforall/issues)
- 📧 [Email](mailto:lucifer@codewithlucifer.com)

---

**Built with ❤️ by [Rohit Ahirwal](https://github.com/rohitahirwal)**