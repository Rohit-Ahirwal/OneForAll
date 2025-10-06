---
sidebar_position: 4
---

# Creating Layouts

Learn how to create beautiful, responsive layouts in OneForAll using Container components and Tailwind CSS. This guide covers everything from basic layouts to complex application structures.

:::info Alpha Version
Layout capabilities are fully functional in OneForAll **alpha** (v0.1.0a3). Tailwind CSS integration provides extensive layout options.
:::

## Layout Fundamentals

### Container Component

The `Container` component is your primary tool for creating layouts. It acts as a wrapper that can hold other components and apply layout styles.

```python
from oneforall import Container, Text, Button

# Basic container
main_container = Container(className="p-4")
main_container.add(Text("Hello World"))
main_container.add(Button("Click Me"))
```

### Flexbox Layouts

Flexbox is the most versatile layout system in OneForAll, powered by Tailwind CSS.

#### Basic Flex Container

```python
# Horizontal layout (default)
horizontal_container = Container(className="flex space-x-4")
horizontal_container.add(Button("Button 1"))
horizontal_container.add(Button("Button 2"))
horizontal_container.add(Button("Button 3"))

# Vertical layout
vertical_container = Container(className="flex flex-col space-y-4")
vertical_container.add(Text("Item 1"))
vertical_container.add(Text("Item 2"))
vertical_container.add(Text("Item 3"))
```

#### Flex Alignment

```python
# Center items horizontally and vertically
centered_container = Container(className="flex items-center justify-center min-h-screen")
centered_container.add(Text("Perfectly Centered", className="text-2xl"))

# Distribute items evenly
distributed_container = Container(className="flex justify-between items-center p-4")
distributed_container.add(Text("Left"))
distributed_container.add(Text("Center"))
distributed_container.add(Text("Right"))

# Align items to different positions
header_container = Container(className="flex justify-between items-center p-4 bg-gray-100")
header_container.add(Text("Logo", className="font-bold"))
header_container.add(Button("Login", className="px-4 py-2 bg-blue-500 text-white rounded"))
```

## Common Layout Patterns

### Application Shell

Create a typical application layout with header, sidebar, and main content:

```python
from oneforall import App, Container, Text, Button

app = App()
window = app.create_window(title="App Layout", size=(1000, 700))

# Main application container
app_container = Container(className="flex flex-col min-h-screen bg-gray-50")

# Header
header = Container(className="bg-white shadow-sm border-b border-gray-200 p-4")
header_content = Container(className="flex justify-between items-center max-w-7xl mx-auto")
header_content.add(Text("My Application", className="text-xl font-bold text-gray-800"))

# Navigation buttons
nav_container = Container(className="flex space-x-4")
nav_container.add(Button("Home", className="px-3 py-2 text-gray-600 hover:text-gray-800"))
nav_container.add(Button("About", className="px-3 py-2 text-gray-600 hover:text-gray-800"))
nav_container.add(Button("Contact", className="px-3 py-2 text-gray-600 hover:text-gray-800"))

header_content.add(nav_container)
header.add(header_content)

# Main content area with sidebar
main_area = Container(className="flex flex-1")

# Sidebar
sidebar = Container(className="w-64 bg-white border-r border-gray-200 p-6")
sidebar.add(Text("Navigation", className="text-lg font-semibold mb-4"))
sidebar.add(Button("Dashboard", className="w-full text-left p-2 hover:bg-gray-100 rounded mb-2"))
sidebar.add(Button("Settings", className="w-full text-left p-2 hover:bg-gray-100 rounded mb-2"))
sidebar.add(Button("Profile", className="w-full text-left p-2 hover:bg-gray-100 rounded mb-2"))

# Main content
content = Container(className="flex-1 p-6")
content.add(Text("Main Content Area", className="text-2xl font-bold mb-4"))
content.add(Text("This is where your main application content goes.", className="text-gray-600"))

# Assemble layout
main_area.add(sidebar)
main_area.add(content)
app_container.add(header)
app_container.add(main_area)

window.add_child(app_container)
```

### Card Layout

Create card-based layouts for displaying information:

```python
def create_card(title, description, image_url=None, actions=None):
    """Create a reusable card component"""
    card = Container(className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow")
    
    # Card image (if provided)
    if image_url:
        from oneforall import Image
        card.add(Image(
            src=image_url, 
            alt=title,
            className="w-full h-48 object-cover"
        ))
    
    # Card content
    content = Container(className="p-6")
    content.add(Text(title, className="text-xl font-bold mb-2"))
    content.add(Text(description, className="text-gray-600 mb-4"))
    
    # Card actions
    if actions:
        action_container = Container(className="flex space-x-2")
        for action in actions:
            action_container.add(action)
        content.add(action_container)
    
    card.add(content)
    return card

# Create a grid of cards
cards_container = Container(className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6")

# Add multiple cards
for i in range(6):
    card = create_card(
        title=f"Card {i+1}",
        description="This is a sample card with some description text.",
        actions=[
            Button("View", className="px-3 py-1 bg-blue-500 text-white rounded text-sm"),
            Button("Edit", className="px-3 py-1 bg-gray-200 text-gray-700 rounded text-sm")
        ]
    )
    cards_container.add(card)
```

### Dashboard Layout

Create a dashboard with metrics and charts:

```python
# Dashboard container
dashboard = Container(className="p-6 bg-gray-50 min-h-screen")

# Dashboard header
dashboard_header = Container(className="mb-8")
dashboard_header.add(Text("Dashboard", className="text-3xl font-bold text-gray-800 mb-2"))
dashboard_header.add(Text("Welcome back! Here's what's happening.", className="text-gray-600"))

# Metrics row
metrics_row = Container(className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8")

def create_metric_card(title, value, change, color="blue"):
    """Create a metric card"""
    card = Container(className="bg-white rounded-lg shadow p-6")
    card.add(Text(title, className="text-sm font-medium text-gray-600 mb-2"))
    card.add(Text(value, className="text-3xl font-bold text-gray-800 mb-1"))
    card.add(Text(
        change, 
        className=f"text-sm font-medium text-{color}-600"
    ))
    return card

# Add metric cards
metrics_row.add(create_metric_card("Total Users", "12,345", "+12% from last month", "green"))
metrics_row.add(create_metric_card("Revenue", "$45,678", "+8% from last month", "green"))
metrics_row.add(create_metric_card("Orders", "1,234", "-3% from last month", "red"))
metrics_row.add(create_metric_card("Conversion", "3.2%", "+0.5% from last month", "green"))

# Charts row
charts_row = Container(className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8")

# Chart placeholders
chart1 = Container(className="bg-white rounded-lg shadow p-6")
chart1.add(Text("Sales Overview", className="text-lg font-semibold mb-4"))
chart1.add(Container(className="h-64 bg-gray-100 rounded flex items-center justify-center"))
chart1.children[-1].add(Text("Chart Placeholder", className="text-gray-500"))

chart2 = Container(className="bg-white rounded-lg shadow p-6")
chart2.add(Text("User Activity", className="text-lg font-semibold mb-4"))
chart2.add(Container(className="h-64 bg-gray-100 rounded flex items-center justify-center"))
chart2.children[-1].add(Text("Chart Placeholder", className="text-gray-500"))

charts_row.add(chart1)
charts_row.add(chart2)

# Recent activity
activity_section = Container(className="bg-white rounded-lg shadow p-6")
activity_section.add(Text("Recent Activity", className="text-lg font-semibold mb-4"))

activity_list = Container(className="space-y-3")
activities = [
    "User John Doe registered",
    "New order #1234 received",
    "Payment processed for order #1233",
    "User Jane Smith updated profile"
]

for activity in activities:
    activity_item = Container(className="flex items-center space-x-3 p-3 bg-gray-50 rounded")
    activity_item.add(Container(className="w-2 h-2 bg-blue-500 rounded-full"))
    activity_item.add(Text(activity, className="text-gray-700"))
    activity_list.add(activity_item)

activity_section.add(activity_list)

# Assemble dashboard
dashboard.add(dashboard_header)
dashboard.add(metrics_row)
dashboard.add(charts_row)
dashboard.add(activity_section)
```

### Form Layout

Create well-structured forms:

```python
def create_form():
    """Create a user registration form"""
    form_container = Container(className="max-w-md mx-auto bg-white rounded-lg shadow-lg p-8")
    
    # Form header
    form_container.add(Text("Create Account", className="text-2xl font-bold text-center mb-6"))
    
    # Form fields
    fields_container = Container(className="space-y-4")
    
    # Name field
    name_field = Container(className="")
    name_field.add(Text("Full Name", className="block text-sm font-medium text-gray-700 mb-1"))
    # Note: In a real app, you'd use an Input component here
    name_field.add(Container(className="w-full p-3 border border-gray-300 rounded-md bg-gray-50"))
    name_field.children[-1].add(Text("Input placeholder", className="text-gray-400"))
    
    # Email field
    email_field = Container(className="")
    email_field.add(Text("Email Address", className="block text-sm font-medium text-gray-700 mb-1"))
    email_field.add(Container(className="w-full p-3 border border-gray-300 rounded-md bg-gray-50"))
    email_field.children[-1].add(Text("Input placeholder", className="text-gray-400"))
    
    # Password field
    password_field = Container(className="")
    password_field.add(Text("Password", className="block text-sm font-medium text-gray-700 mb-1"))
    password_field.add(Container(className="w-full p-3 border border-gray-300 rounded-md bg-gray-50"))
    password_field.children[-1].add(Text("Input placeholder", className="text-gray-400"))
    
    fields_container.add(name_field)
    fields_container.add(email_field)
    fields_container.add(password_field)
    
    # Form actions
    actions_container = Container(className="flex space-x-4 mt-6")
    actions_container.add(Button(
        "Create Account", 
        className="flex-1 py-3 bg-blue-500 text-white rounded-md hover:bg-blue-600 font-medium"
    ))
    actions_container.add(Button(
        "Cancel", 
        className="flex-1 py-3 bg-gray-200 text-gray-700 rounded-md hover:bg-gray-300 font-medium"
    ))
    
    form_container.add(fields_container)
    form_container.add(actions_container)
    
    return form_container

# Use the form
registration_form = create_form()
```

## Responsive Design

### Breakpoint Classes

Use Tailwind's responsive classes for different screen sizes:

```python
# Responsive grid
responsive_grid = Container(className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4")

# Responsive padding
responsive_container = Container(className="p-4 sm:p-6 lg:p-8")

# Responsive text sizes
responsive_title = Text("Responsive Title", className="text-xl sm:text-2xl lg:text-3xl font-bold")

# Hide/show on different screens
mobile_only = Container(className="block sm:hidden")
desktop_only = Container(className="hidden lg:block")
```

### Mobile-First Layout

```python
def create_mobile_first_layout():
    """Create a layout that works well on mobile and scales up"""
    
    # Main container with mobile-first approach
    main = Container(className="min-h-screen bg-gray-50")
    
    # Header - stacks on mobile, horizontal on desktop
    header = Container(className="bg-white shadow-sm p-4")
    header_content = Container(className="flex flex-col sm:flex-row sm:justify-between sm:items-center space-y-4 sm:space-y-0")
    
    # Logo/title
    header_content.add(Text("Mobile App", className="text-xl font-bold"))
    
    # Navigation - vertical on mobile, horizontal on desktop
    nav = Container(className="flex flex-col sm:flex-row space-y-2 sm:space-y-0 sm:space-x-4")
    nav.add(Button("Home", className="text-left sm:text-center px-3 py-2"))
    nav.add(Button("About", className="text-left sm:text-center px-3 py-2"))
    nav.add(Button("Contact", className="text-left sm:text-center px-3 py-2"))
    
    header_content.add(nav)
    header.add(header_content)
    
    # Content area - full width on mobile, centered with max width on desktop
    content = Container(className="p-4 sm:p-6 lg:p-8")
    content_inner = Container(className="max-w-4xl mx-auto")
    
    # Cards - single column on mobile, multiple on larger screens
    cards_grid = Container(className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6")
    
    for i in range(6):
        card = Container(className="bg-white rounded-lg shadow p-4 sm:p-6")
        card.add(Text(f"Card {i+1}", className="text-lg font-semibold mb-2"))
        card.add(Text("Mobile-friendly card content.", className="text-gray-600 text-sm sm:text-base"))
        cards_grid.add(card)
    
    content_inner.add(cards_grid)
    content.add(content_inner)
    
    main.add(header)
    main.add(content)
    
    return main
```

## Advanced Layout Techniques

### Sticky Elements

```python
# Sticky header
sticky_header = Container(className="sticky top-0 bg-white shadow-sm z-10 p-4")
sticky_header.add(Text("Sticky Header", className="font-bold"))

# Sticky sidebar
layout_with_sticky = Container(className="flex")
sticky_sidebar = Container(className="w-64 sticky top-0 h-screen overflow-y-auto bg-gray-100 p-4")
main_content = Container(className="flex-1 p-4")

# Long content to demonstrate scrolling
for i in range(50):
    main_content.add(Text(f"Content item {i+1}", className="mb-4"))
```

### Overlay and Modal Patterns

```python
def create_modal_overlay():
    """Create a modal overlay pattern"""
    
    # Overlay background
    overlay = Container(className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50")
    
    # Modal content
    modal = Container(className="bg-white rounded-lg shadow-xl max-w-md w-full mx-4 p-6")
    modal.add(Text("Modal Title", className="text-xl font-bold mb-4"))
    modal.add(Text("This is modal content.", className="text-gray-600 mb-6"))
    
    # Modal actions
    actions = Container(className="flex justify-end space-x-3")
    actions.add(Button("Cancel", className="px-4 py-2 text-gray-600 hover:text-gray-800"))
    actions.add(Button("Confirm", className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"))
    
    modal.add(actions)
    overlay.add(modal)
    
    return overlay
```

### Split Panes

```python
def create_split_pane_layout():
    """Create a resizable split pane layout"""
    
    split_container = Container(className="flex h-screen")
    
    # Left pane
    left_pane = Container(className="w-1/3 bg-gray-100 border-r border-gray-300 p-4 overflow-y-auto")
    left_pane.add(Text("Left Pane", className="font-bold mb-4"))
    for i in range(20):
        left_pane.add(Text(f"Item {i+1}", className="mb-2 p-2 hover:bg-gray-200 rounded"))
    
    # Right pane
    right_pane = Container(className="flex-1 p-4 overflow-y-auto")
    right_pane.add(Text("Right Pane", className="font-bold mb-4"))
    right_pane.add(Text("Main content area with detailed information.", className="text-gray-600"))
    
    split_container.add(left_pane)
    split_container.add(right_pane)
    
    return split_container
```

## Layout Best Practices

### Consistent Spacing

```python
# ✅ Good: Use consistent spacing scale
SPACING = {
    'xs': 'space-y-1',
    'sm': 'space-y-2', 
    'md': 'space-y-4',
    'lg': 'space-y-6',
    'xl': 'space-y-8'
}

container = Container(className=f"p-6 {SPACING['md']}")
```

### Semantic Layout Structure

```python
# ✅ Good: Clear layout hierarchy
app_shell = Container(className="min-h-screen flex flex-col")
header = Container(className="bg-white shadow-sm")
main = Container(className="flex-1 flex")
sidebar = Container(className="w-64 bg-gray-50")
content = Container(className="flex-1 p-6")
footer = Container(className="bg-gray-800 text-white p-4")
```

### Performance Considerations

```python
# ✅ Good: Avoid deeply nested containers when possible
efficient_layout = Container(className="grid grid-cols-3 gap-4")

# ❌ Avoid: Unnecessary nesting
inefficient_layout = Container(className="flex")
wrapper = Container(className="flex-1")
inner_wrapper = Container(className="w-full")
content = Container(className="p-4")
# ... too many levels
```

## Next Steps

Now that you understand OneForAll layouts:

- [Style with Tailwind](./styling) - Advanced styling techniques
- [Multiple Windows](./multiple-windows) - Layout across multiple windows
- [API Reference](../api/components) - Complete component documentation

---

Master these layout patterns to create professional, responsive desktop applications with OneForAll!