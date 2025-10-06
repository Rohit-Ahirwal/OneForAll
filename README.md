# OneForAll

> ⚠️ **Alpha Version**: OneForAll is currently in alpha. APIs may change and some features are still in development.

**Build beautiful desktop apps with Python and Tailwind CSS.**

OneForAll is a modern Python GUI framework that combines the simplicity of Python with the power of Tailwind CSS. Create responsive, beautiful desktop applications with hot reload, reactive state management, and a component-based architecture.

## 🚀 Quick Start

```bash
# Install OneForAll
pip install oneforall-gui

# Create a new app
oneforall init my_app
cd my_app

# Run with hot reload
oneforall dev example_basic.py
```

## ✨ Features

- **Pure Python** - No HTML, CSS, or JavaScript required
- **Tailwind CSS** - Beautiful styling with utility classes
- **Hot Reload** - Instant updates during development
- **Component-Based** - Reusable UI components
- **Reactive State** - Automatic UI updates when state changes
- **Multi-Window** - Support for multiple application windows
- **CLI Tools** - Project scaffolding and development server

## 📖 Documentation

**📚 [Complete Documentation](https://rohit-ahirwal.github.io/OneForAll/)**

### Quick Links
- **[Getting Started Guide](https://rohit-ahirwal.github.io/OneForAll/docs/intro)** - Installation and first app
- **[Tutorial Series](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/your-first-app)** - Step-by-step learning
- **[API Reference](https://rohit-ahirwal.github.io/OneForAll/docs/api/app)** - Complete technical reference
- **[Components Guide](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/components)** - Built-in components
- **[State Management](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/state-management)** - Reactive state system
- **[Styling with Tailwind](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/styling)** - CSS styling guide

## 💡 Simple Example

```python
from oneforall import App, Window
from oneforall.components import Container, Text, Button

# Create app and window
app = App()
window = Window(title="Counter App", size=(300, 200))

# Create container with Tailwind classes
container = Container(className="p-8 text-center space-y-4")

# Add counter display
count = app.use_state('count', 0)
display = Text(f"Count: {count}", className="text-2xl font-bold")
container.add(display)

# Add increment button
def increment():
    current = app.use_state('count', 0)
    app.set_state('count', current + 1)

button = Button(
    "Click Me!", 
    on_click=increment,
    className="px-6 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
)
container.add(button)

# Run the app
window.add_child(container)
app.windows.append(window)

if __name__ == "__main__":
    app.run(dev_mode=True)
```

## 🧩 Core Components

```python
# Text with styling
text = Text("Hello World", className="text-lg font-bold text-blue-600")

# Interactive button
button = Button("Click Me", on_click=handler, className="px-4 py-2 bg-green-500 text-white rounded")

# Layout container
container = Container(className="flex items-center justify-center p-4 space-x-2")
```

## 🎨 Tailwind CSS Styling

OneForAll includes full [Tailwind CSS](https://tailwindcss.com/) support:

```python
# Flexbox layouts
Container(className="flex items-center justify-between")

# Responsive design
Text("Title", className="text-sm md:text-lg lg:text-xl")

# Hover effects
Button("Hover Me", className="bg-blue-500 hover:bg-blue-600 transition-colors")
```

## ⚡ CLI Commands

```bash
# Create new project
oneforall init my_project

# Development with hot reload
oneforall dev app.py

# Generate Tailwind CSS
oneforall css
```

## 🔄 State Management

Reactive state that automatically updates your UI:

```python
app = App()

# Create reactive state
counter = app.use_state('counter', 0)

# State updates trigger UI re-renders
def increment():
    current = app.use_state('counter', 0)
    app.set_state('counter', current + 1)  # UI updates automatically
```

> 📖 **Learn More**: Check out the [State Management Tutorial](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/state-management) for advanced patterns and best practices.

## 🏗️ Example Apps

### Counter App
```python
from oneforall import App, Window
from oneforall.components import Container, Text, Button

app = App()
window = Window(title="Counter", size=(300, 200))
container = Container(className="p-8 text-center space-y-4")

count = app.use_state('count', 0)
display = Text(f"count", className="text-2xl font-bold")

def increment():
    current = app.use_state('count', 0)
    app.set_state('count', current + 1)

def decrement():
    current = app.use_state('count', 0)
    app.set_state('count', current - 1)

container.add(display)
container.add(Button("+", on_click=increment, className="mx-2 px-4 py-2 bg-green-500 text-white rounded"))
container.add(Button("-", on_click=decrement, className="mx-2 px-4 py-2 bg-red-500 text-white rounded"))

window.add_child(container)
app.windows.append(window)
app.run(dev_mode=True)
```

> 📖 **More Examples**: See the [Tutorial Series](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/your-first-app) for complete walkthroughs including Todo apps, layouts, and multi-window applications.

## 🔧 Custom Components

Create reusable components for your apps:

```python
def Card(title, content, className=""):
    card = Container(className=f"p-6 bg-white rounded-lg shadow-md {className}")
    card.add(Text(title, className="text-xl font-bold mb-2"))
    card.add(Text(content, className="text-gray-600"))
    return card

# Usage
welcome_card = Card("Welcome", "Get started with OneForAll", "max-w-sm mx-auto")
```

> 📖 **Learn More**: Visit the [Components Guide](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/components) for advanced component patterns and composition techniques.

## 📚 Learning Resources

- **[📖 Complete Documentation](https://rohit-ahirwal.github.io/OneForAll/)** - Full guides and API reference
- **[🎯 Your First App](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/your-first-app)** - Step-by-step tutorial
- **[🧩 Components](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/components)** - Built-in components guide
- **[🔄 State Management](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/state-management)** - Reactive state patterns
- **[🎨 Styling](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/styling)** - Tailwind CSS integration
- **[🪟 Multiple Windows](https://rohit-ahirwal.github.io/OneForAll/docs/tutorial-basics/multiple-windows)** - Multi-window apps

## 🆘 Need Help?

- **📖 [Documentation](https://rohit-ahirwal.github.io/OneForAll/)** - Comprehensive guides and API reference
- **🐛 [GitHub Issues](https://github.com/Rohit-Ahirwal/OneForAll/issues)** - Bug reports and feature requests
- **📧 Email**: lucifer@codewithlucifer.com
- **🎨 [Tailwind CSS Docs](https://tailwindcss.com/docs)** - Styling reference

## 📄 License

This project is licensed under the [Apache License 2.0](./LICENSE).

You are free to use this framework in commercial and non-commercial projects.  
Apps built with this framework can be proprietary or open-source.  
The project name and branding are owned by Rohit Ahirwal and may not be used  
to imply official affiliation without permission.

---

**Built by [Rohit Ahirwal](https://github.com/rohitahirwal)** | **[📖 Documentation](https://rohit-ahirwal.github.io/OneForAll/)** | **[🐛 Issues](https://github.com/Rohit-Ahirwal/OneForAll/issues)**
