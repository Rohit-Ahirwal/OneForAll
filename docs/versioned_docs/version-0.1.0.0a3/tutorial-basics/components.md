---
sidebar_position: 2
---

# Components

OneForAll provides a set of built-in components that serve as the building blocks for your desktop applications. All components follow a React-like pattern and support Tailwind CSS styling.

:::info Alpha Version
Component APIs are stable in OneForAll **alpha** (v0.1.0a3), but new components and features may be added in future releases.
:::

## Component Basics

All OneForAll components inherit from the base `Component` class and share common properties:

### Common Properties

- `className` (str): Tailwind CSS classes for styling
- `id` (str): Unique identifier (auto-generated if not provided)
- `attrs` (dict): Additional HTML attributes

### Component Lifecycle

1. **Creation**: Component is instantiated with properties
2. **Rendering**: Component generates its HTML representation
3. **State Updates**: Automatic re-rendering when dependent state changes
4. **Event Handling**: User interactions trigger event handlers

## Built-in Components

### Text Component

The `Text` component displays text content with optional formatting.

#### Basic Usage

```python
from oneforall import Text

# Simple text
greeting = Text("Hello, World!")

# Styled text with Tailwind CSS
title = Text(
    "Welcome to OneForAll", 
    className="text-3xl font-bold text-blue-600"
)

# Text with custom HTML tag
subtitle = Text(
    "A Python GUI Framework", 
    tag="h2",
    className="text-xl text-gray-600"
)
```

#### Dynamic Text with State

```python
from oneforall import App, Text

app = App()

# Text that updates with state
user_name = app.use_state('user', 'Anonymous')
welcome_text = Text(
    f"Welcome, {user_name}!", 
    className="text-lg font-medium"
)

# Update the text by changing state
def update_user():
    app.set_state('user', 'John Doe')
```

#### Text Properties

- `content` (str): The text content to display
- `tag` (str): HTML tag to use (default: "span")
- `className` (str): CSS classes for styling

### Button Component

The `Button` component creates interactive buttons with click handlers.

#### Basic Usage

```python
from oneforall import Button

# Simple button
click_me = Button("Click Me")

# Styled button with event handler
def handle_click():
    print("Button was clicked!")

styled_button = Button(
    "Submit", 
    on_click=handle_click,
    className="px-6 py-3 bg-blue-500 hover:bg-blue-600 text-white rounded-lg font-medium transition-colors"
)
```

#### Button Variants

```python
# Primary button
primary_btn = Button(
    "Primary Action",
    className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
)

# Secondary button
secondary_btn = Button(
    "Secondary Action",
    className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-4 py-2 rounded"
)

# Danger button
danger_btn = Button(
    "Delete",
    className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded"
)

# Icon button (using emoji or text)
icon_btn = Button(
    "❤️ Like",
    className="bg-pink-500 hover:bg-pink-600 text-white px-3 py-2 rounded-full"
)
```

#### Button with State Integration

```python
from oneforall import App, Button, Text

app = App()
counter = app.use_state('counter', 0)

def increment():
    current = app.get_state('counter')
    app.set_state('counter', current + 1)

increment_btn = Button(
    f"Clicked {counter} times", 
    on_click=increment,
    className="px-4 py-2 bg-green-500 text-white rounded"
)
```

#### Button Properties

- `label` (str): Button text
- `on_click` (function): Click event handler
- `className` (str): CSS classes for styling

### Container Component

The `Container` component groups and layouts other components. It's essential for creating structured UIs.

#### Basic Usage

```python
from oneforall import Container, Text, Button

# Simple container
main_container = Container(className="p-4")

# Add children to container
main_container.add(Text("Welcome!"))
main_container.add(Button("Get Started"))
```

#### Layout Patterns

```python
# Vertical layout with spacing
vertical_container = Container(className="flex flex-col space-y-4 p-6")

# Horizontal layout
horizontal_container = Container(className="flex flex-row space-x-4 items-center")

# Grid layout
grid_container = Container(className="grid grid-cols-2 gap-4 p-4")

# Card-like container
card_container = Container(className="bg-white rounded-lg shadow-lg p-6 max-w-md")

# Full-screen container
fullscreen_container = Container(className="min-h-screen bg-gray-50 flex items-center justify-center")
```

#### Nested Containers

```python
# Create complex layouts with nested containers
app_layout = Container(className="min-h-screen bg-gray-100")

# Header
header = Container(className="bg-white shadow-sm p-4")
header.add(Text("My App", className="text-2xl font-bold"))

# Main content area
main_content = Container(className="flex-1 p-6")

# Sidebar
sidebar = Container(className="w-64 bg-gray-200 p-4")
sidebar.add(Text("Navigation", className="font-semibold mb-4"))

# Content area
content_area = Container(className="flex-1 bg-white rounded-lg p-6 ml-4")

# Assemble layout
main_content.add(sidebar)
main_content.add(content_area)
app_layout.add(header)
app_layout.add(main_content)
```

#### Container Properties

- `className` (str): CSS classes for styling and layout
- `children` (list): Child components (managed via `add()` method)

### Image Component

The `Image` component displays images with automatic embedding and optimization.

#### Basic Usage

```python
from oneforall import Image

# Display an image
logo = Image(
    src="assets/logo.png", 
    alt="Company Logo",
    className="w-32 h-32 object-contain"
)

# Responsive image
hero_image = Image(
    src="images/hero.jpg",
    alt="Hero Image",
    className="w-full h-64 object-cover rounded-lg"
)
```

#### Image Styling

```python
# Avatar image
avatar = Image(
    src="user-avatar.jpg",
    alt="User Avatar",
    className="w-12 h-12 rounded-full object-cover border-2 border-gray-300"
)

# Thumbnail image
thumbnail = Image(
    src="thumbnail.png",
    alt="Thumbnail",
    className="w-20 h-20 object-cover rounded-md hover:scale-105 transition-transform cursor-pointer"
)

# Full-width banner
banner = Image(
    src="banner.jpg",
    alt="Banner",
    className="w-full h-48 object-cover"
)
```

#### Image Properties

- `src` (str): Path to the image file
- `alt` (str): Alternative text for accessibility
- `className` (str): CSS classes for styling

## Component Composition

### Building Complex UIs

Combine components to create sophisticated interfaces:

```python
from oneforall import App, Container, Text, Button, Image

app = App()
window = app.create_window(title="User Profile", size=(600, 400))

# Profile card
profile_card = Container(className="bg-white rounded-xl shadow-lg p-6 max-w-md mx-auto")

# Profile header
profile_header = Container(className="flex items-center space-x-4 mb-6")
profile_header.add(Image(
    src="avatar.jpg", 
    alt="Profile Picture",
    className="w-16 h-16 rounded-full object-cover"
))

profile_info = Container(className="flex-1")
profile_info.add(Text("John Doe", className="text-xl font-bold text-gray-800"))
profile_info.add(Text("Software Developer", className="text-gray-600"))

profile_header.add(profile_info)

# Profile actions
actions = Container(className="flex space-x-3")
actions.add(Button(
    "Edit Profile", 
    className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
))
actions.add(Button(
    "Settings", 
    className="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300"
))

# Assemble profile card
profile_card.add(profile_header)
profile_card.add(actions)

window.add_child(profile_card)
```

### Reusable Component Patterns

Create reusable component functions:

```python
def create_card(title, content, actions=None):
    """Create a reusable card component"""
    card = Container(className="bg-white rounded-lg shadow-md p-6 mb-4")
    
    # Card header
    if title:
        card.add(Text(title, className="text-lg font-semibold mb-3"))
    
    # Card content
    if content:
        card.add(Text(content, className="text-gray-600 mb-4"))
    
    # Card actions
    if actions:
        action_container = Container(className="flex space-x-2")
        for action in actions:
            action_container.add(action)
        card.add(action_container)
    
    return card

# Usage
info_card = create_card(
    title="Welcome",
    content="This is a reusable card component.",
    actions=[
        Button("Learn More", className="px-3 py-1 bg-blue-500 text-white rounded"),
        Button("Dismiss", className="px-3 py-1 bg-gray-300 text-gray-700 rounded")
    ]
)
```

## Best Practices

### Component Organization

```python
# ✅ Good: Organize components logically
def create_navigation():
    nav = Container(className="bg-gray-800 p-4")
    nav.add(Text("My App", className="text-white text-xl font-bold"))
    return nav

def create_main_content():
    content = Container(className="flex-1 p-6")
    # Add content components
    return content

# ✅ Good: Use descriptive names
user_profile_section = Container(className="mb-8")
settings_panel = Container(className="bg-gray-50 p-4 rounded")
```

### State Integration

```python
# ✅ Good: Use state for dynamic content
app = App()
user_name = app.use_state('user_name', 'Guest')
is_logged_in = app.use_state('logged_in', False)

welcome_message = Text(
    f"Welcome, {user_name}!" if is_logged_in else "Please log in",
    className="text-lg"
)

# ✅ Good: Update state in event handlers
def handle_login():
    app.set_state('logged_in', True)
    app.set_state('user_name', 'John Doe')

login_button = Button("Login", on_click=handle_login)
```

### Styling Consistency

```python
# ✅ Good: Define consistent styling patterns
BUTTON_STYLES = {
    'primary': "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600",
    'secondary': "px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300",
    'danger': "px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
}

# Use consistent styles
save_btn = Button("Save", className=BUTTON_STYLES['primary'])
cancel_btn = Button("Cancel", className=BUTTON_STYLES['secondary'])
delete_btn = Button("Delete", className=BUTTON_STYLES['danger'])
```

## Next Steps

Now that you understand OneForAll components:

- [Learn State Management](./state-management) - Master reactive state patterns
- [Create Beautiful Layouts](./creating-layouts) - Advanced layout techniques
- [Style with Tailwind](./styling) - Comprehensive styling guide
- [Explore API Reference](../api/components) - Complete component API documentation

---

Components are the foundation of OneForAll applications. Master these building blocks to create powerful and beautiful desktop applications!