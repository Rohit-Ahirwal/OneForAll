---
sidebar_position: 3
---

# Components API Reference

OneForAll provides a component-based architecture for building user interfaces. All components inherit from the base `Component` class and can be composed to create complex UIs.

:::info Alpha Version
The Components API is stable in OneForAll **alpha** (v0.1.0a3) with full functionality for building desktop applications.
:::

## Base Component Class

All OneForAll components inherit from the base `Component` class, which provides core functionality for rendering, state management, and lifecycle.

### Component

The base class for all UI components.

```python
from oneforall.components import Component

class CustomComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
    
    def render(self):
        return f'<div class="{self.className}">{self.children_html()}</div>'
```

#### Properties

All components support these base properties:

- **className** (`str`): CSS classes to apply to the component
- **id** (`str`): Unique identifier for the component
- **style** (`dict`): Inline CSS styles
- **children** (`list`): Child components

#### Methods

##### render()

Renders the component to HTML.

```python
html = component.render()
```

**Returns:** `str` - The HTML representation of the component

##### add()

Adds a child component.

```python
container.add(Text("Hello World"))
container.add(Button("Click Me"))
```

**Parameters:**
- `component` (Component): The child component to add

##### remove()

Removes a child component.

```python
container.remove(child_component)
```

**Parameters:**
- `component` (Component): The child component to remove

##### children_html()

Renders all child components to HTML.

```python
children_html = component.children_html()
```

**Returns:** `str` - The HTML of all child components

## Built-in Components

### Container

A flexible container component for layout and grouping.

```python
from oneforall import Container

container = Container(
    className="flex flex-col p-4 bg-white rounded shadow",
    id="main-container"
)
```

#### Properties

- **className** (`str`): CSS classes (supports all Tailwind CSS classes)
- **id** (`str`): Unique identifier
- **style** (`dict`): Inline CSS styles

#### Usage Examples

```python
# Basic container
container = Container(className="p-6")

# Flexbox layout
flex_container = Container(className="flex items-center justify-between")

# Grid layout
grid_container = Container(className="grid grid-cols-3 gap-4")

# Card-like container
card = Container(className="bg-white rounded-lg shadow-md p-6 m-4")
```

### Text

Displays text content with styling support.

```python
from oneforall import Text

text = Text(
    "Hello World",
    className="text-xl font-bold text-blue-600",
    id="greeting"
)
```

#### Constructor

```python
Text(content, className="", id="", style={})
```

**Parameters:**
- `content` (`str`): The text content to display
- `className` (`str`): CSS classes
- `id` (`str`): Unique identifier
- `style` (`dict`): Inline CSS styles

#### Usage Examples

```python
# Basic text
title = Text("Welcome to OneForAll", className="text-2xl font-bold")

# Styled text
subtitle = Text(
    "Build desktop apps with Python",
    className="text-lg text-gray-600 mb-4"
)

# Text with custom styling
custom_text = Text(
    "Custom styled text",
    style={"color": "#ff6b6b", "font-weight": "bold"}
)

# Multi-line text
description = Text(
    "This is a longer description that might span multiple lines.",
    className="text-base leading-relaxed"
)
```

### Button

Interactive button component with click handling.

```python
from oneforall import Button

button = Button(
    "Click Me",
    className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600",
    onclick=handle_click
)
```

#### Constructor

```python
Button(text, className="", id="", onclick=None, disabled=False, style={})
```

**Parameters:**
- `text` (`str`): The button text
- `className` (`str`): CSS classes
- `id` (`str`): Unique identifier
- `onclick` (`callable`): Click event handler function
- `disabled` (`bool`): Whether the button is disabled
- `style` (`dict`): Inline CSS styles

#### Usage Examples

```python
# Basic button
save_button = Button("Save", onclick=save_data)

# Styled button
primary_button = Button(
    "Get Started",
    className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
)

# Disabled button
disabled_button = Button(
    "Loading...",
    disabled=True,
    className="px-4 py-2 bg-gray-300 text-gray-500 rounded cursor-not-allowed"
)

# Button with custom styling
custom_button = Button(
    "Custom",
    style={
        "background": "linear-gradient(45deg, #ff6b6b, #4ecdc4)",
        "border": "none",
        "color": "white",
        "padding": "12px 24px",
        "border-radius": "25px"
    }
)
```

### Image

Displays images with various sizing and styling options.

```python
from oneforall import Image

image = Image(
    src="path/to/image.jpg",
    alt="Description",
    className="w-32 h-32 object-cover rounded"
)
```

#### Constructor

```python
Image(src, alt="", className="", id="", width=None, height=None, style={})
```

**Parameters:**
- `src` (`str`): Image source path or URL
- `alt` (`str`): Alternative text for accessibility
- `className` (`str`): CSS classes
- `id` (`str`): Unique identifier
- `width` (`int`): Image width in pixels
- `height` (`int`): Image height in pixels
- `style` (`dict`): Inline CSS styles

#### Usage Examples

```python
# Basic image
logo = Image(
    src="assets/logo.png",
    alt="Company Logo",
    className="w-24 h-24"
)

# Responsive image
hero_image = Image(
    src="assets/hero.jpg",
    alt="Hero Image",
    className="w-full h-64 object-cover"
)

# Fixed size image
avatar = Image(
    src="assets/avatar.jpg",
    alt="User Avatar",
    width=50,
    height=50,
    className="rounded-full"
)

# Image with custom styling
styled_image = Image(
    src="assets/photo.jpg",
    alt="Photo",
    style={
        "border": "3px solid #ddd",
        "border-radius": "10px",
        "box-shadow": "0 4px 8px rgba(0,0,0,0.1)"
    }
)
```

## Component Composition

### Building Complex Components

```python
from oneforall import Container, Text, Button, Image

def create_user_card(user_data):
    """Create a user card component"""
    card = Container(className="bg-white rounded-lg shadow-md p-6 m-4 max-w-sm")
    
    # Header with avatar and name
    header = Container(className="flex items-center mb-4")
    
    avatar = Image(
        src=user_data.get("avatar", "assets/default-avatar.png"),
        alt=f"{user_data['name']} Avatar",
        className="w-12 h-12 rounded-full mr-4"
    )
    
    name_container = Container(className="flex-1")
    name = Text(user_data["name"], className="text-lg font-semibold")
    role = Text(user_data["role"], className="text-sm text-gray-600")
    
    name_container.add(name)
    name_container.add(role)
    
    header.add(avatar)
    header.add(name_container)
    
    # Content
    if user_data.get("bio"):
        bio = Text(user_data["bio"], className="text-gray-700 mb-4")
        card.add(bio)
    
    # Actions
    actions = Container(className="flex space-x-2")
    
    view_button = Button(
        "View Profile",
        className="flex-1 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600",
        onclick=lambda: view_profile(user_data["id"])
    )
    
    message_button = Button(
        "Message",
        className="flex-1 px-4 py-2 bg-gray-200 text-gray-700 rounded hover:bg-gray-300",
        onclick=lambda: send_message(user_data["id"])
    )
    
    actions.add(view_button)
    actions.add(message_button)
    
    # Assemble card
    card.add(header)
    card.add(actions)
    
    return card

# Usage
user = {
    "id": 1,
    "name": "John Doe",
    "role": "Software Developer",
    "bio": "Passionate about building great software with Python.",
    "avatar": "assets/john-avatar.jpg"
}

user_card = create_user_card(user)
```

### Component Factory Pattern

```python
class ComponentFactory:
    """Factory for creating common component patterns"""
    
    @staticmethod
    def create_form_field(label, input_type="text", placeholder="", required=False):
        """Create a form field with label and input"""
        field = Container(className="mb-4")
        
        # Label
        label_text = label
        if required:
            label_text += " *"
        
        field_label = Text(
            label_text,
            className="block text-sm font-medium text-gray-700 mb-1"
        )
        
        # Input (simulated with styled container for now)
        input_field = Container(
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        )
        
        if placeholder:
            input_field.add(Text(placeholder, className="text-gray-400"))
        
        field.add(field_label)
        field.add(input_field)
        
        return field
    
    @staticmethod
    def create_alert(message, alert_type="info"):
        """Create an alert component"""
        type_classes = {
            "info": "bg-blue-100 border-blue-500 text-blue-700",
            "success": "bg-green-100 border-green-500 text-green-700",
            "warning": "bg-yellow-100 border-yellow-500 text-yellow-700",
            "error": "bg-red-100 border-red-500 text-red-700"
        }
        
        alert = Container(
            className=f"border-l-4 p-4 mb-4 {type_classes.get(alert_type, type_classes['info'])}"
        )
        
        alert.add(Text(message, className="font-medium"))
        
        return alert
    
    @staticmethod
    def create_loading_spinner():
        """Create a loading spinner component"""
        spinner = Container(
            className="flex items-center justify-center p-4"
        )
        
        # Animated spinner (CSS animation would be handled by Tailwind)
        spinner_element = Container(
            className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"
        )
        
        spinner.add(spinner_element)
        spinner.add(Text("Loading...", className="ml-2 text-gray-600"))
        
        return spinner
    
    @staticmethod
    def create_modal(title, content, on_close=None):
        """Create a modal dialog component"""
        # Backdrop
        modal = Container(
            className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
        )
        
        # Modal content
        modal_content = Container(
            className="bg-white rounded-lg shadow-xl max-w-md w-full mx-4"
        )
        
        # Header
        header = Container(
            className="flex items-center justify-between p-6 border-b"
        )
        
        title_text = Text(title, className="text-lg font-semibold")
        close_button = Button(
            "×",
            className="text-gray-400 hover:text-gray-600 text-2xl font-bold",
            onclick=on_close
        )
        
        header.add(title_text)
        header.add(close_button)
        
        # Body
        body = Container(className="p-6")
        if isinstance(content, str):
            body.add(Text(content))
        else:
            body.add(content)
        
        modal_content.add(header)
        modal_content.add(body)
        modal.add(modal_content)
        
        return modal

# Usage examples
name_field = ComponentFactory.create_form_field("Full Name", required=True)
success_alert = ComponentFactory.create_alert("Data saved successfully!", "success")
loading = ComponentFactory.create_loading_spinner()
modal = ComponentFactory.create_modal("Confirm Action", "Are you sure you want to proceed?")
```

## Custom Components

### Creating Custom Components

```python
from oneforall.components import Component

class ProgressBar(Component):
    """Custom progress bar component"""
    
    def __init__(self, value=0, max_value=100, className="", **props):
        super().__init__(className=className, **props)
        self.value = value
        self.max_value = max_value
    
    def render(self):
        percentage = (self.value / self.max_value) * 100
        
        return f'''
        <div class="w-full bg-gray-200 rounded-full h-4 {self.className}">
            <div class="bg-blue-500 h-4 rounded-full transition-all duration-300" 
                 style="width: {percentage}%"></div>
        </div>
        '''
    
    def set_value(self, value):
        """Update the progress value"""
        self.value = max(0, min(value, self.max_value))

class CounterWidget(Component):
    """Custom counter widget with increment/decrement buttons"""
    
    def __init__(self, initial_value=0, min_value=None, max_value=None, **props):
        super().__init__(**props)
        self.value = initial_value
        self.min_value = min_value
        self.max_value = max_value
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the counter UI"""
        self.container = Container(className="flex items-center space-x-2")
        
        # Decrement button
        self.decrement_btn = Button(
            "-",
            className="px-3 py-1 bg-gray-200 rounded hover:bg-gray-300",
            onclick=self.decrement
        )
        
        # Value display
        self.value_display = Text(
            str(self.value),
            className="px-4 py-1 bg-gray-100 rounded min-w-12 text-center"
        )
        
        # Increment button
        self.increment_btn = Button(
            "+",
            className="px-3 py-1 bg-gray-200 rounded hover:bg-gray-300",
            onclick=self.increment
        )
        
        self.container.add(self.decrement_btn)
        self.container.add(self.value_display)
        self.container.add(self.increment_btn)
        
        self.add(self.container)
    
    def increment(self):
        """Increment the counter value"""
        if self.max_value is None or self.value < self.max_value:
            self.value += 1
            self.update_display()
    
    def decrement(self):
        """Decrement the counter value"""
        if self.min_value is None or self.value > self.min_value:
            self.value -= 1
            self.update_display()
    
    def update_display(self):
        """Update the value display"""
        self.value_display.content = str(self.value)
    
    def render(self):
        return self.container.render()

# Usage
progress = ProgressBar(value=75, className="mb-4")
counter = CounterWidget(initial_value=5, min_value=0, max_value=10)
```

### Component with State Integration

```python
from oneforall import App, Container, Text, Button
from oneforall.components import Component

class TodoItem(Component):
    """Todo item component with state integration"""
    
    def __init__(self, todo_id, app_state, **props):
        super().__init__(**props)
        self.todo_id = todo_id
        self.app_state = app_state
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the todo item UI"""
        todo = self.app_state.get(f"todos.{self.todo_id}")
        
        self.container = Container(
            className="flex items-center justify-between p-3 border-b hover:bg-gray-50"
        )
        
        # Left side - checkbox and text
        left_side = Container(className="flex items-center space-x-3")
        
        # Checkbox (simulated with button)
        checkbox = Button(
            "✓" if todo.get("completed") else "○",
            className=f"w-6 h-6 rounded border text-sm {
                'bg-green-500 text-white' if todo.get('completed') 
                else 'bg-white border-gray-300'
            }",
            onclick=self.toggle_completed
        )
        
        # Todo text
        text_class = "text-gray-500 line-through" if todo.get("completed") else "text-gray-900"
        todo_text = Text(todo.get("text", ""), className=text_class)
        
        left_side.add(checkbox)
        left_side.add(todo_text)
        
        # Right side - delete button
        delete_btn = Button(
            "🗑",
            className="text-red-500 hover:text-red-700 px-2 py-1",
            onclick=self.delete_todo
        )
        
        self.container.add(left_side)
        self.container.add(delete_btn)
        
        self.add(self.container)
    
    def toggle_completed(self):
        """Toggle the completed state of the todo"""
        current_state = self.app_state.get(f"todos.{self.todo_id}.completed", False)
        self.app_state.set(f"todos.{self.todo_id}.completed", not current_state)
    
    def delete_todo(self):
        """Delete the todo item"""
        todos = self.app_state.get("todos", {})
        if self.todo_id in todos:
            del todos[self.todo_id]
            self.app_state.set("todos", todos)
    
    def render(self):
        return self.container.render()

# Usage in an app
class TodoApp:
    def __init__(self):
        self.app = App()
        self.window = self.app.create_window("Todo App", (500, 600))
        self.setup_ui()
    
    def setup_ui(self):
        container = Container(className="p-6")
        
        # Title
        container.add(Text("My Todos", className="text-2xl font-bold mb-6"))
        
        # Todo list
        self.todo_list = Container(className="space-y-2")
        self.update_todo_list()
        container.add(self.todo_list)
        
        self.window.add_child(container)
    
    def update_todo_list(self):
        """Update the todo list display"""
        self.todo_list.children.clear()
        
        todos = self.app.state.get("todos", {})
        for todo_id in todos:
            todo_item = TodoItem(todo_id, self.app.state)
            self.todo_list.add(todo_item)
    
    def run(self):
        # Initialize with some sample todos
        self.app.state.set("todos", {
            "1": {"text": "Learn OneForAll", "completed": False},
            "2": {"text": "Build an app", "completed": False},
            "3": {"text": "Deploy to production", "completed": False}
        })
        
        self.app.run()
```

## Component Lifecycle

### Initialization

```python
class MyComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        # Component initialization
        self.setup_initial_state()
        self.setup_ui()
    
    def setup_initial_state(self):
        """Initialize component state"""
        self.internal_state = {}
    
    def setup_ui(self):
        """Setup the component UI"""
        # Build component structure
        pass
```

### Rendering

```python
class MyComponent(Component):
    def render(self):
        """Render the component to HTML"""
        # Custom rendering logic
        return f'<div class="{self.className}">{self.children_html()}</div>'
```

### Updates and Re-rendering

```python
class DynamicComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.data = []
        self.setup_ui()
    
    def update_data(self, new_data):
        """Update component data and re-render"""
        self.data = new_data
        self.refresh_ui()
    
    def refresh_ui(self):
        """Refresh the component UI"""
        # Clear existing children
        self.children.clear()
        
        # Rebuild UI with new data
        self.setup_ui()
```

## Best Practices

### Component Organization

```python
# ✅ Good: Organize components by functionality
class UserInterface:
    @staticmethod
    def create_header(title):
        header = Container(className="bg-blue-500 text-white p-4")
        header.add(Text(title, className="text-xl font-bold"))
        return header
    
    @staticmethod
    def create_sidebar():
        sidebar = Container(className="w-64 bg-gray-100 p-4")
        # Add sidebar content
        return sidebar
    
    @staticmethod
    def create_main_content():
        content = Container(className="flex-1 p-6")
        # Add main content
        return content

# ✅ Good: Use composition over inheritance
def create_dashboard():
    dashboard = Container(className="flex h-screen")
    
    sidebar = UserInterface.create_sidebar()
    main_area = Container(className="flex-1 flex flex-col")
    
    header = UserInterface.create_header("Dashboard")
    content = UserInterface.create_main_content()
    
    main_area.add(header)
    main_area.add(content)
    
    dashboard.add(sidebar)
    dashboard.add(main_area)
    
    return dashboard
```

### Performance Optimization

```python
# ✅ Good: Minimize re-renders
class OptimizedList(Component):
    def __init__(self, items, **props):
        super().__init__(**props)
        self.items = items
        self.rendered_items = {}
        self.setup_ui()
    
    def update_items(self, new_items):
        """Update items efficiently"""
        # Only re-render changed items
        for item in new_items:
            if item.id not in self.rendered_items or item != self.rendered_items[item.id]:
                self.rendered_items[item.id] = item
                # Re-render only this item
                self.update_item_display(item)
    
    def update_item_display(self, item):
        """Update a specific item display"""
        # Efficient item update logic
        pass

# ✅ Good: Use lazy loading for large datasets
class LazyLoadList(Component):
    def __init__(self, data_source, page_size=20, **props):
        super().__init__(**props)
        self.data_source = data_source
        self.page_size = page_size
        self.current_page = 0
        self.loaded_items = []
        self.load_initial_data()
    
    def load_initial_data(self):
        """Load initial page of data"""
        self.loaded_items = self.data_source.get_page(0, self.page_size)
        self.setup_ui()
    
    def load_more(self):
        """Load more data"""
        self.current_page += 1
        new_items = self.data_source.get_page(self.current_page, self.page_size)
        self.loaded_items.extend(new_items)
        self.add_items_to_ui(new_items)
```

### Error Handling

```python
class RobustComponent(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.error_state = None
        try:
            self.setup_ui()
        except Exception as e:
            self.handle_error(e)
    
    def handle_error(self, error):
        """Handle component errors gracefully"""
        self.error_state = str(error)
        self.show_error_ui()
    
    def show_error_ui(self):
        """Show error state UI"""
        error_container = Container(className="p-4 bg-red-100 border border-red-400 rounded")
        error_container.add(Text("Error loading component", className="text-red-700 font-bold"))
        error_container.add(Text(self.error_state, className="text-red-600 text-sm"))
        
        retry_button = Button(
            "Retry",
            className="mt-2 px-4 py-2 bg-red-500 text-white rounded",
            onclick=self.retry_setup
        )
        error_container.add(retry_button)
        
        self.add(error_container)
    
    def retry_setup(self):
        """Retry component setup"""
        self.children.clear()
        self.error_state = None
        try:
            self.setup_ui()
        except Exception as e:
            self.handle_error(e)
```

## Related APIs

- [App API](./app) - Application management
- [Window API](./window) - Window management
- [State Management API](./state-management) - Reactive state handling

## Examples

See the [Components Tutorial](../tutorial-basics/components) for comprehensive examples and usage patterns.

---

The Components API provides a powerful foundation for building rich, interactive desktop applications with OneForAll's reactive architecture.