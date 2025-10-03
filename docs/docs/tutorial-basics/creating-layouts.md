---
sidebar_position: 3
---

# Creating Layouts

Building effective layouts is crucial for creating professional-looking applications. In this tutorial, you'll learn how to use OneForAll's layout system with Tailwind CSS to create responsive and beautiful user interfaces.

## Layout Fundamentals

OneForAll uses the `Container` component as the primary layout building block. Combined with Tailwind CSS classes, you can create any layout pattern.

### Basic Container

```python
from oneforall import App, Window, Container, Text

app = App()
window = Window(title="Layout Demo", size=(800, 600))

# Basic container
container = Container(className="p-4")
container.add(Text("Hello, World!"))

window.add_child(container)
app.append(window)
app.run()
```

## Flexbox Layouts

Flexbox is perfect for creating flexible, responsive layouts.

### Horizontal Layout

```python
from oneforall import App, Window, Container, Text, Button

app = App()
window = Window(title="Horizontal Layout", size=(600, 200))

# Horizontal flex container
horizontal_container = Container(className="flex items-center justify-between p-4 bg-gray-100")

# Add items
horizontal_container.add(Text("Left Item", className="text-blue-600 font-bold"))
horizontal_container.add(Text("Center Item", className="text-green-600 font-bold"))
horizontal_container.add(Button("Right Button", className="bg-red-500 text-white px-4 py-2 rounded"))

window.add_child(horizontal_container)
app.append(window)
app.run()
```

### Vertical Layout

```python
# Vertical flex container
vertical_container = Container(className="flex flex-col space-y-4 p-4 h-full")

# Header
header = Container(className="bg-blue-500 text-white p-4 rounded")
header.add(Text("Header", className="text-xl font-bold"))
vertical_container.add(header)

# Content
content = Container(className="flex-1 bg-gray-100 p-4 rounded")
content.add(Text("Main Content Area", className="text-lg"))
vertical_container.add(content)

# Footer
footer = Container(className="bg-gray-800 text-white p-4 rounded")
footer.add(Text("Footer", className="text-center"))
vertical_container.add(footer)

window.add_child(vertical_container)
```

### Centered Layout

```python
# Center content both horizontally and vertically
centered_container = Container(className="flex items-center justify-center h-full bg-gradient-to-br from-purple-400 to-pink-400")

# Card in center
card = Container(className="bg-white p-8 rounded-lg shadow-lg max-w-md")
card.add(Text("Centered Card", className="text-2xl font-bold text-center mb-4"))
card.add(Text("This card is perfectly centered!", className="text-gray-600 text-center"))
card.add(Button("Action", className="w-full mt-4 bg-blue-500 text-white py-2 rounded"))

centered_container.add(card)
window.add_child(centered_container)
```

## Grid Layouts

CSS Grid is excellent for creating complex, two-dimensional layouts.

### Basic Grid

```python
# 2x2 grid
grid_container = Container(className="grid grid-cols-2 gap-4 p-4 h-full")

# Grid items
for i in range(4):
    item = Container(className="bg-blue-100 p-4 rounded border-2 border-blue-300")
    item.add(Text(f"Grid Item {i+1}", className="text-center font-bold"))
    grid_container.add(item)

window.add_child(grid_container)
```

### Responsive Grid

```python
# Responsive grid that adapts to screen size
responsive_grid = Container(className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4")

# Create cards
for i in range(6):
    card = Container(className="bg-white p-6 rounded-lg shadow-md border")
    card.add(Text(f"Card {i+1}", className="text-xl font-bold mb-2"))
    card.add(Text("This is a sample card with some content.", className="text-gray-600 mb-4"))
    card.add(Button("Learn More", className="bg-blue-500 text-white px-4 py-2 rounded"))
    responsive_grid.add(card)

window.add_child(responsive_grid)
```

### Dashboard Layout

```python
# Complex dashboard layout
dashboard = Container(className="grid grid-cols-12 gap-4 p-4 h-full")

# Sidebar (3 columns wide)
sidebar = Container(className="col-span-3 bg-gray-800 text-white p-4 rounded")
sidebar.add(Text("Dashboard", className="text-xl font-bold mb-4"))
sidebar.add(Text("Navigation", className="text-sm text-gray-300 mb-2"))
sidebar.add(Button("Home", className="w-full text-left text-white hover:bg-gray-700 p-2 rounded mb-1"))
sidebar.add(Button("Analytics", className="w-full text-left text-white hover:bg-gray-700 p-2 rounded mb-1"))
sidebar.add(Button("Settings", className="w-full text-left text-white hover:bg-gray-700 p-2 rounded"))
dashboard.add(sidebar)

# Main content area (9 columns wide)
main_content = Container(className="col-span-9 space-y-4")

# Top stats row
stats_row = Container(className="grid grid-cols-3 gap-4")
for i, (title, value) in enumerate([("Users", "1,234"), ("Revenue", "$12,345"), ("Orders", "567")]):
    stat_card = Container(className="bg-white p-4 rounded shadow border")
    stat_card.add(Text(title, className="text-sm text-gray-600"))
    stat_card.add(Text(value, className="text-2xl font-bold text-blue-600"))
    stats_row.add(stat_card)

main_content.add(stats_row)

# Chart area
chart_area = Container(className="bg-white p-6 rounded shadow border")
chart_area.add(Text("Analytics Chart", className="text-xl font-bold mb-4"))
chart_area.add(Container(className="h-64 bg-gray-100 rounded flex items-center justify-center"))
chart_area.children[-1].add(Text("Chart Placeholder", className="text-gray-500"))
main_content.add(chart_area)

dashboard.add(main_content)
window.add_child(dashboard)
```

## Common Layout Patterns

### Header-Content-Footer

```python
def create_app_layout():
    # Full height container
    app_container = Container(className="flex flex-col h-full")
    
    # Header
    header = Container(className="bg-blue-600 text-white p-4 shadow-lg")
    header_content = Container(className="flex items-center justify-between")
    header_content.add(Text("My App", className="text-xl font-bold"))
    
    nav_buttons = Container(className="flex space-x-2")
    nav_buttons.add(Button("Home", className="text-white hover:bg-blue-700 px-3 py-1 rounded"))
    nav_buttons.add(Button("About", className="text-white hover:bg-blue-700 px-3 py-1 rounded"))
    nav_buttons.add(Button("Contact", className="text-white hover:bg-blue-700 px-3 py-1 rounded"))
    header_content.add(nav_buttons)
    
    header.add(header_content)
    app_container.add(header)
    
    # Main content (flexible)
    main_content = Container(className="flex-1 p-4 overflow-auto")
    main_content.add(Text("Main Content Area", className="text-2xl font-bold mb-4"))
    main_content.add(Text("This area will expand to fill available space.", className="text-gray-600"))
    app_container.add(main_content)
    
    # Footer
    footer = Container(className="bg-gray-800 text-white p-4 text-center")
    footer.add(Text("© 2024 My App. All rights reserved.", className="text-sm"))
    app_container.add(footer)
    
    return app_container

window.add_child(create_app_layout())
```

### Sidebar Layout

```python
def create_sidebar_layout():
    # Main container
    layout_container = Container(className="flex h-full")
    
    # Sidebar
    sidebar = Container(className="w-64 bg-gray-100 border-r border-gray-300 p-4")
    sidebar.add(Text("Sidebar", className="text-lg font-bold mb-4"))
    
    # Sidebar menu
    menu_items = ["Dashboard", "Users", "Products", "Orders", "Settings"]
    for item in menu_items:
        sidebar.add(Button(
            item, 
            className="w-full text-left p-2 hover:bg-gray-200 rounded mb-1"
        ))
    
    layout_container.add(sidebar)
    
    # Main content
    main_area = Container(className="flex-1 p-6")
    main_area.add(Text("Main Content", className="text-2xl font-bold mb-4"))
    main_area.add(Text("Content goes here...", className="text-gray-600"))
    layout_container.add(main_area)
    
    return layout_container

window.add_child(create_sidebar_layout())
```

### Card Layout

```python
def create_card_layout():
    # Container for cards
    cards_container = Container(className="p-6 space-y-6")
    
    # Hero card
    hero_card = Container(className="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-8 rounded-lg shadow-lg")
    hero_card.add(Text("Welcome to OneForAll", className="text-3xl font-bold mb-2"))
    hero_card.add(Text("Build amazing desktop applications with Python", className="text-xl opacity-90 mb-4"))
    hero_card.add(Button("Get Started", className="bg-white text-blue-600 font-bold py-2 px-6 rounded"))
    cards_container.add(hero_card)
    
    # Feature cards grid
    features_grid = Container(className="grid grid-cols-1 md:grid-cols-3 gap-6")
    
    features = [
        ("Easy to Use", "Simple Python syntax", "🚀"),
        ("Reactive", "Automatic UI updates", "⚡"),
        ("Flexible", "Tailwind CSS styling", "🎨")
    ]
    
    for title, description, icon in features:
        feature_card = Container(className="bg-white p-6 rounded-lg shadow-md border hover:shadow-lg transition-shadow")
        feature_card.add(Text(icon, className="text-4xl mb-3"))
        feature_card.add(Text(title, className="text-xl font-bold mb-2"))
        feature_card.add(Text(description, className="text-gray-600"))
        features_grid.add(feature_card)
    
    cards_container.add(features_grid)
    return cards_container

window.add_child(create_card_layout())
```

## Responsive Design

### Breakpoint Classes

Tailwind CSS provides responsive breakpoints:

```python
# Responsive container
responsive_container = Container(className="p-4 sm:p-6 md:p-8 lg:p-12")

# Responsive grid
responsive_grid = Container(className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4")

# Responsive text
responsive_text = Text("Responsive Text", className="text-sm sm:text-base md:text-lg lg:text-xl")
```

### Mobile-First Design

```python
def create_mobile_first_layout():
    # Mobile-first approach
    container = Container(className="p-4 md:p-8")
    
    # Stack on mobile, side-by-side on desktop
    content_layout = Container(className="flex flex-col md:flex-row gap-4 md:gap-8")
    
    # Main content
    main_content = Container(className="flex-1")
    main_content.add(Text("Main Content", className="text-xl md:text-2xl font-bold mb-4"))
    main_content.add(Text("This content adapts to screen size.", className="text-sm md:text-base"))
    content_layout.add(main_content)
    
    # Sidebar (full width on mobile, fixed width on desktop)
    sidebar = Container(className="w-full md:w-64 bg-gray-100 p-4 rounded")
    sidebar.add(Text("Sidebar", className="font-bold mb-2"))
    sidebar.add(Text("Additional info", className="text-sm"))
    content_layout.add(sidebar)
    
    container.add(content_layout)
    return container

window.add_child(create_mobile_first_layout())
```

## Layout Components

### Reusable Layout Components

```python
class AppLayout:
    def __init__(self, app):
        self.app = app
    
    def create_page_header(self, title, subtitle=None):
        header = Container(className="mb-8")
        header.add(Text(title, className="text-3xl font-bold text-gray-800"))
        if subtitle:
            header.add(Text(subtitle, className="text-lg text-gray-600 mt-2"))
        return header
    
    def create_card(self, title, content, actions=None):
        card = Container(className="bg-white p-6 rounded-lg shadow-md border")
        card.add(Text(title, className="text-xl font-bold mb-4"))
        card.add(Text(content, className="text-gray-600 mb-4"))
        
        if actions:
            action_container = Container(className="flex space-x-2")
            for action in actions:
                action_container.add(action)
            card.add(action_container)
        
        return card
    
    def create_two_column_layout(self, left_content, right_content):
        layout = Container(className="grid grid-cols-1 lg:grid-cols-2 gap-8")
        layout.add(left_content)
        layout.add(right_content)
        return layout

# Usage
layout_helper = AppLayout(app)

# Create page
page_container = Container(className="p-6")

# Add header
page_container.add(layout_helper.create_page_header(
    "Dashboard", 
    "Welcome to your application dashboard"
))

# Create cards
card1 = layout_helper.create_card(
    "Statistics", 
    "View your application statistics and metrics.",
    [Button("View Details", className="bg-blue-500 text-white px-4 py-2 rounded")]
)

card2 = layout_helper.create_card(
    "Settings", 
    "Configure your application preferences.",
    [Button("Open Settings", className="bg-gray-500 text-white px-4 py-2 rounded")]
)

# Add two-column layout
page_container.add(layout_helper.create_two_column_layout(card1, card2))

window.add_child(page_container)
```

## Layout Best Practices

### 1. Use Consistent Spacing

```python
# ✅ Good - Consistent spacing scale
container = Container(className="p-4 space-y-4")  # 16px padding and spacing
inner_container = Container(className="p-2 space-y-2")  # 8px padding and spacing

# ❌ Bad - Inconsistent spacing
container = Container(className="p-3 space-y-5")  # Mixed spacing values
```

### 2. Plan for Different Screen Sizes

```python
# ✅ Good - Responsive design
responsive_layout = Container(className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4")

# ❌ Bad - Fixed layout
fixed_layout = Container(className="grid grid-cols-3 gap-4")  # Breaks on mobile
```

### 3. Use Semantic Layout Structure

```python
# ✅ Good - Clear structure
app_container = Container(className="flex flex-col h-full")
header = Container(className="bg-blue-600 p-4")  # Header
main = Container(className="flex-1 p-4")         # Main content
footer = Container(className="bg-gray-800 p-4")  # Footer

# ❌ Bad - Unclear structure
container1 = Container(className="bg-blue-600 p-4")
container2 = Container(className="flex-1 p-4")
container3 = Container(className="bg-gray-800 p-4")
```

### 4. Optimize for Performance

```python
# ✅ Good - Efficient nesting
main_container = Container(className="p-4")
content_grid = Container(className="grid grid-cols-2 gap-4")
main_container.add(content_grid)

# ❌ Bad - Unnecessary nesting
wrapper = Container()
outer = Container(className="p-4")
inner = Container()
content_grid = Container(className="grid grid-cols-2 gap-4")
inner.add(content_grid)
outer.add(inner)
wrapper.add(outer)
```

## Complete Layout Example

Here's a complete example combining multiple layout techniques:

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Initialize state for dynamic content
app.use_state("current_page", "dashboard")
app.use_state("user_name", "John Doe")

window = Window(title="Complete Layout Demo", size=(1200, 800))

# Main app container
app_container = Container(className="flex flex-col h-full bg-gray-50")

# Header
header = Container(className="bg-white shadow-sm border-b border-gray-200 p-4")
header_content = Container(className="flex items-center justify-between max-w-7xl mx-auto")

# Logo and title
logo_section = Container(className="flex items-center space-x-3")
logo_section.add(Text("🚀", className="text-2xl"))
logo_section.add(Text("OneForAll App", className="text-xl font-bold text-gray-800"))
header_content.add(logo_section)

# User section
user_section = Container(className="flex items-center space-x-4")
user_section.add(Text(f"Welcome, {app.use_state('user_name')}", className="text-gray-600"))
user_section.add(Button("Logout", className="bg-red-500 text-white px-3 py-1 rounded text-sm"))
header_content.add(user_section)

header.add(header_content)
app_container.add(header)

# Main content area
main_area = Container(className="flex flex-1 max-w-7xl mx-auto w-full")

# Sidebar
sidebar = Container(className="w-64 bg-white shadow-sm border-r border-gray-200 p-4")
sidebar.add(Text("Navigation", className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-4"))

nav_items = ["Dashboard", "Analytics", "Users", "Settings"]
for item in nav_items:
    is_active = item.lower() == app.use_state("current_page")
    button_class = "w-full text-left p-3 rounded mb-1 transition-colors "
    if is_active:
        button_class += "bg-blue-100 text-blue-700 font-medium"
    else:
        button_class += "text-gray-700 hover:bg-gray-100"
    
    def set_page(page_name):
        def handler():
            app.set_state("current_page", page_name.lower())
        return handler
    
    sidebar.add(Button(item, on_click=set_page(item), className=button_class))

main_area.add(sidebar)

# Content area
content_area = Container(className="flex-1 p-6")

# Page title
current_page = app.use_state("current_page").title()
content_area.add(Text(current_page, className="text-2xl font-bold text-gray-800 mb-6"))

# Dashboard content
if app.use_state("current_page") == "dashboard":
    # Stats cards
    stats_grid = Container(className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8")
    
    stats = [
        ("Total Users", "2,543", "👥", "text-blue-600"),
        ("Revenue", "$12,345", "💰", "text-green-600"),
        ("Orders", "1,234", "📦", "text-purple-600")
    ]
    
    for title, value, icon, color in stats:
        stat_card = Container(className="bg-white p-6 rounded-lg shadow-sm border")
        stat_card.add(Text(icon, className="text-3xl mb-2"))
        stat_card.add(Text(title, className="text-sm text-gray-600"))
        stat_card.add(Text(value, className=f"text-2xl font-bold {color}"))
        stats_grid.add(stat_card)
    
    content_area.add(stats_grid)
    
    # Chart section
    chart_section = Container(className="bg-white p-6 rounded-lg shadow-sm border")
    chart_section.add(Text("Analytics Overview", className="text-lg font-semibold mb-4"))
    chart_placeholder = Container(className="h-64 bg-gray-50 rounded border-2 border-dashed border-gray-300 flex items-center justify-center")
    chart_placeholder.add(Text("Chart would go here", className="text-gray-500"))
    chart_section.add(chart_placeholder)
    content_area.add(chart_section)

main_area.add(content_area)
app_container.add(main_area)

# Footer
footer = Container(className="bg-white border-t border-gray-200 p-4")
footer_content = Container(className="max-w-7xl mx-auto text-center")
footer_content.add(Text("© 2024 OneForAll App. Built with OneForAll Framework.", className="text-sm text-gray-600"))
footer.add(footer_content)
app_container.add(footer)

window.add_child(app_container)
app.append(window)
app.run()
```

## Next Steps

You now know how to:

- ✅ Create flexible layouts with Flexbox and Grid
- ✅ Build responsive designs that work on all screen sizes
- ✅ Implement common layout patterns (header-footer, sidebar, cards)
- ✅ Create reusable layout components
- ✅ Follow layout best practices

## What's Next?

- [Styling Guide](./styling) - Master Tailwind CSS styling
- [Multiple Windows](./multiple-windows) - Work with multiple windows
- [Components](../api/components) - Learn about all available components