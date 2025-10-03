---
sidebar_position: 3
---

# Components

OneForAll provides a set of built-in components for building user interfaces. All components inherit from the base `Component` class and support reactive state management.

## Base Component

All OneForAll components inherit from the `Component` base class.

### Common Properties

All components support these common properties:

- `className` (str, optional): CSS classes for styling (Tailwind CSS supported)
- `style` (dict, optional): Inline CSS styles
- `id` (str, optional): HTML element ID
- `on_click` (function, optional): Click event handler

### Common Methods

#### `add(child)`

Adds a child component (for container components).

**Parameters:**
- `child` (Component): The child component to add

#### `remove(child)`

Removes a child component.

**Parameters:**
- `child` (Component): The child component to remove

#### `render()`

Returns the HTML representation of the component.

**Returns:**
- `str`: HTML string

## Text

Displays text content with optional formatting.

### Constructor

```python
from oneforall import Text

text = Text(
    content="Hello World",
    className="text-lg font-bold text-blue-500",
    tag="p"
)
```

**Parameters:**
- `content` (str): The text content to display
- `className` (str, optional): CSS classes for styling
- `tag` (str, optional): HTML tag to use. Defaults to `"span"`
- `style` (dict, optional): Inline CSS styles
- `id` (str, optional): HTML element ID

### Examples

```python
# Basic text
title = Text("Welcome to OneForAll", className="text-2xl font-bold")

# Text with state binding
app.use_state("user_name", "Guest")
greeting = Text(f"Hello, {app.use_state('user_name')}!")

# Different HTML tags
heading = Text("Main Title", tag="h1", className="text-3xl")
paragraph = Text("This is a paragraph.", tag="p", className="mb-4")
```

## Button

Interactive button component with click handling.

### Constructor

```python
from oneforall import Button

def handle_click():
    print("Button clicked!")

button = Button(
    text="Click Me",
    on_click=handle_click,
    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
)
```

**Parameters:**
- `text` (str): Button text content
- `on_click` (function, optional): Click event handler
- `className` (str, optional): CSS classes for styling
- `disabled` (bool, optional): Whether button is disabled. Defaults to `False`
- `button_type` (str, optional): Button type (`"button"`, `"submit"`, `"reset"`). Defaults to `"button"`
- `style` (dict, optional): Inline CSS styles
- `id` (str, optional): HTML element ID

### Examples

```python
# Basic button
save_btn = Button("Save", on_click=lambda: print("Saved!"))

# Styled button with Tailwind
primary_btn = Button(
    "Primary Action",
    className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-2 px-4 rounded-md"
)

# Disabled button
disabled_btn = Button("Loading...", disabled=True, className="opacity-50 cursor-not-allowed")

# Button with state interaction
def increment_counter():
    current = app.use_state("counter")
    app.set_state("counter", current + 1)

counter_btn = Button(f"Count: {app.use_state('counter')}", on_click=increment_counter)
```

## Container

Layout container for organizing child components.

### Constructor

```python
from oneforall import Container

container = Container(
    className="flex flex-col space-y-4 p-4",
    tag="div"
)
```

**Parameters:**
- `className` (str, optional): CSS classes for styling
- `tag` (str, optional): HTML tag to use. Defaults to `"div"`
- `style` (dict, optional): Inline CSS styles
- `id` (str, optional): HTML element ID

### Examples

```python
# Flex container
flex_container = Container(className="flex items-center justify-between p-4")
flex_container.add(Text("Left side"))
flex_container.add(Button("Right side"))

# Grid container
grid_container = Container(className="grid grid-cols-2 gap-4")
grid_container.add(Text("Item 1"))
grid_container.add(Text("Item 2"))
grid_container.add(Text("Item 3"))
grid_container.add(Text("Item 4"))

# Card container
card = Container(className="bg-white shadow-lg rounded-lg p-6 max-w-sm")
card.add(Text("Card Title", className="text-xl font-bold mb-2"))
card.add(Text("Card content goes here.", className="text-gray-700"))
card.add(Button("Action", className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"))
```

## Image

Displays images with optional styling and event handling.

### Constructor

```python
from oneforall import Image

image = Image(
    src="https://example.com/image.jpg",
    alt="Description",
    className="w-32 h-32 object-cover rounded"
)
```

**Parameters:**
- `src` (str): Image source URL or path
- `alt` (str, optional): Alternative text for accessibility
- `className` (str, optional): CSS classes for styling
- `width` (int, optional): Image width in pixels
- `height` (int, optional): Image height in pixels
- `style` (dict, optional): Inline CSS styles
- `id` (str, optional): HTML element ID
- `on_click` (function, optional): Click event handler

### Examples

```python
# Basic image
logo = Image(src="./assets/logo.png", alt="Company Logo")

# Responsive image
hero_image = Image(
    src="./assets/hero.jpg",
    alt="Hero Image",
    className="w-full h-64 object-cover"
)

# Clickable image
def show_full_image():
    print("Opening full image...")

thumbnail = Image(
    src="./assets/thumb.jpg",
    alt="Thumbnail",
    className="w-24 h-24 cursor-pointer hover:opacity-80",
    on_click=show_full_image
)

# Image with state-based src
app.use_state("current_image", "./assets/default.jpg")
dynamic_image = Image(
    src=app.use_state("current_image"),
    alt="Dynamic Image",
    className="w-48 h-48"
)
```

## Custom Components

You can create custom components by inheriting from the `Component` base class:

```python
from oneforall import Component, Container, Text, Button

class CounterComponent(Component):
    def __init__(self, app, initial_value=0, className=""):
        super().__init__(className=className)
        self.app = app
        self.state_key = f"counter_{id(self)}"
        
        # Initialize state
        app.use_state(self.state_key, initial_value)
        
        # Create UI
        self.container = Container(className="flex items-center space-x-2")
        
        # Decrement button
        self.container.add(Button(
            "-",
            on_click=self.decrement,
            className="bg-red-500 text-white px-2 py-1 rounded"
        ))
        
        # Counter display
        self.counter_text = Text(
            str(app.use_state(self.state_key)),
            className="font-mono text-lg"
        )
        self.container.add(self.counter_text)
        
        # Increment button
        self.container.add(Button(
            "+",
            on_click=self.increment,
            className="bg-green-500 text-white px-2 py-1 rounded"
        ))
    
    def increment(self):
        current = self.app.use_state(self.state_key)
        self.app.set_state(self.state_key, current + 1)
    
    def decrement(self):
        current = self.app.use_state(self.state_key)
        self.app.set_state(self.state_key, current - 1)
    
    def render(self):
        # Update counter display
        self.counter_text.content = str(self.app.use_state(self.state_key))
        return self.container.render()

# Usage
app = App()
window = Window(title="Custom Component Demo")

counter1 = CounterComponent(app, initial_value=0)
counter2 = CounterComponent(app, initial_value=10)

main_container = Container(className="p-4 space-y-4")
main_container.add(Text("Counter 1:", className="font-bold"))
main_container.add(counter1)
main_container.add(Text("Counter 2:", className="font-bold"))
main_container.add(counter2)

window.add_child(main_container)
app.append(window)
app.run()
```

## Component Lifecycle

Components in OneForAll follow a simple lifecycle:

1. **Creation**: Component is instantiated with initial properties
2. **Rendering**: Component's `render()` method is called to generate HTML
3. **State Updates**: When state changes, components are re-rendered automatically
4. **Event Handling**: User interactions trigger event handlers
5. **Cleanup**: Components are cleaned up when removed from the UI

## Best Practices

### State Management

```python
# ✅ Good: Use state keys for reactive updates
app.use_state("message", "Hello")
text = Text(app.use_state("message"))

# ❌ Bad: Direct value won't update reactively
text = Text("Hello")
```

### Event Handlers

```python
# ✅ Good: Update state in event handlers
def handle_click():
    app.set_state("clicked", True)

button = Button("Click me", on_click=handle_click)

# ❌ Bad: Direct DOM manipulation
def handle_click():
    # Don't do this - OneForAll manages the DOM
    document.getElementById("button").innerHTML = "Clicked"
```

### Component Composition

```python
# ✅ Good: Compose components hierarchically
main_container = Container(className="p-4")
header = Container(className="mb-4")
header.add(Text("Title", className="text-2xl font-bold"))
main_container.add(header)

content = Container(className="space-y-2")
content.add(Text("Content line 1"))
content.add(Text("Content line 2"))
main_container.add(content)
```

## See Also

- [App](./app) - Main application class
- [Window](./window) - Window management
- [State Management](../tutorial-basics/state-management) - Learn about reactive state
- [Styling Guide](../tutorial-basics/styling) - Learn about styling components