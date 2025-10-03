---
sidebar_position: 4
---

# Styling with Tailwind CSS

OneForAll uses Tailwind CSS for styling, providing a utility-first approach that makes it easy to create beautiful, responsive designs. This tutorial covers everything you need to know about styling your OneForAll applications.

## Tailwind CSS Basics

Tailwind CSS uses utility classes that you apply directly to your components. Instead of writing custom CSS, you compose designs using pre-built classes.

### Basic Styling

```python
from oneforall import App, Window, Container, Text, Button

app = App()
window = Window(title="Styling Demo", size=(800, 600))

# Basic text styling
styled_text = Text(
    "Hello, World!", 
    className="text-2xl font-bold text-blue-600 text-center"
)

# Basic button styling
styled_button = Button(
    "Click Me", 
    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
)

# Container with background and padding
styled_container = Container(className="bg-gray-100 p-6 rounded-lg shadow-md")
styled_container.add(styled_text)
styled_container.add(styled_button)

window.add_child(styled_container)
app.append(window)
app.run()
```

## Color System

### Text Colors

```python
# Text color examples
colors_container = Container(className="space-y-2 p-4")

text_colors = [
    ("text-gray-900", "Dark Gray Text"),
    ("text-red-600", "Red Text"),
    ("text-blue-600", "Blue Text"),
    ("text-green-600", "Green Text"),
    ("text-yellow-600", "Yellow Text"),
    ("text-purple-600", "Purple Text"),
    ("text-pink-600", "Pink Text"),
]

for color_class, label in text_colors:
    colors_container.add(Text(label, className=f"{color_class} font-medium"))

window.add_child(colors_container)
```

### Background Colors

```python
# Background color examples
bg_container = Container(className="grid grid-cols-2 gap-4 p-4")

background_colors = [
    ("bg-red-100", "Light Red Background"),
    ("bg-blue-100", "Light Blue Background"),
    ("bg-green-100", "Light Green Background"),
    ("bg-yellow-100", "Light Yellow Background"),
    ("bg-purple-100", "Light Purple Background"),
    ("bg-pink-100", "Light Pink Background"),
]

for bg_class, label in background_colors:
    card = Container(className=f"{bg_class} p-4 rounded-lg")
    card.add(Text(label, className="text-gray-800 font-medium"))
    bg_container.add(card)

window.add_child(bg_container)
```

### Color Shades

```python
# Different shades of the same color
shades_container = Container(className="space-y-2 p-4")

blue_shades = [
    ("bg-blue-50 text-blue-900", "Blue 50"),
    ("bg-blue-100 text-blue-900", "Blue 100"),
    ("bg-blue-200 text-blue-900", "Blue 200"),
    ("bg-blue-300 text-blue-800", "Blue 300"),
    ("bg-blue-400 text-blue-800", "Blue 400"),
    ("bg-blue-500 text-white", "Blue 500"),
    ("bg-blue-600 text-white", "Blue 600"),
    ("bg-blue-700 text-white", "Blue 700"),
    ("bg-blue-800 text-white", "Blue 800"),
    ("bg-blue-900 text-white", "Blue 900"),
]

for classes, label in blue_shades:
    shade_item = Container(className=f"{classes} p-3 rounded")
    shade_item.add(Text(label, className="font-medium"))
    shades_container.add(shade_item)

window.add_child(shades_container)
```

## Typography

### Font Sizes

```python
# Font size examples
typography_container = Container(className="space-y-4 p-4")

font_sizes = [
    ("text-xs", "Extra Small Text (12px)"),
    ("text-sm", "Small Text (14px)"),
    ("text-base", "Base Text (16px)"),
    ("text-lg", "Large Text (18px)"),
    ("text-xl", "Extra Large Text (20px)"),
    ("text-2xl", "2X Large Text (24px)"),
    ("text-3xl", "3X Large Text (30px)"),
    ("text-4xl", "4X Large Text (36px)"),
]

for size_class, label in font_sizes:
    typography_container.add(Text(label, className=f"{size_class} text-gray-800"))

window.add_child(typography_container)
```

### Font Weights

```python
# Font weight examples
weights_container = Container(className="space-y-2 p-4")

font_weights = [
    ("font-thin", "Thin Weight (100)"),
    ("font-light", "Light Weight (300)"),
    ("font-normal", "Normal Weight (400)"),
    ("font-medium", "Medium Weight (500)"),
    ("font-semibold", "Semibold Weight (600)"),
    ("font-bold", "Bold Weight (700)"),
    ("font-extrabold", "Extra Bold Weight (800)"),
    ("font-black", "Black Weight (900)"),
]

for weight_class, label in font_weights:
    weights_container.add(Text(label, className=f"{weight_class} text-lg text-gray-800"))

window.add_child(weights_container)
```

### Text Alignment

```python
# Text alignment examples
alignment_container = Container(className="space-y-4 p-4 bg-gray-50")

alignments = [
    ("text-left", "Left aligned text"),
    ("text-center", "Center aligned text"),
    ("text-right", "Right aligned text"),
    ("text-justify", "Justified text that spans multiple lines and is aligned to both left and right margins"),
]

for align_class, text_content in alignments:
    alignment_container.add(Text(text_content, className=f"{align_class} text-gray-800 bg-white p-3 rounded"))

window.add_child(alignment_container)
```

## Spacing

### Padding

```python
# Padding examples
padding_container = Container(className="space-y-4 p-4")

padding_examples = [
    ("p-2", "Padding 2 (8px all sides)"),
    ("p-4", "Padding 4 (16px all sides)"),
    ("px-4 py-2", "Horizontal 4, Vertical 2"),
    ("pt-4 pb-2 pl-6 pr-6", "Top 4, Bottom 2, Left/Right 6"),
]

for padding_class, label in padding_examples:
    example = Container(className=f"bg-blue-100 {padding_class} rounded border-2 border-blue-300")
    example.add(Text(label, className="text-blue-800 font-medium"))
    padding_container.add(example)

window.add_child(padding_container)
```

### Margin

```python
# Margin examples
margin_container = Container(className="bg-gray-100 p-4")

margin_examples = [
    ("m-2", "Margin 2 (8px all sides)"),
    ("m-4", "Margin 4 (16px all sides)"),
    ("mx-4 my-2", "Horizontal 4, Vertical 2"),
    ("mt-4 mb-2", "Top 4, Bottom 2"),
]

for margin_class, label in margin_examples:
    example = Container(className=f"bg-white {margin_class} p-3 rounded border")
    example.add(Text(label, className="text-gray-800 font-medium"))
    margin_container.add(example)

window.add_child(margin_container)
```

### Space Between

```python
# Space between children
space_container = Container(className="space-y-4 p-4")

# Vertical spacing
vertical_space = Container(className="space-y-3")
for i in range(3):
    vertical_space.add(Container(className="bg-blue-100 p-3 rounded"))
    vertical_space.children[-1].add(Text(f"Item {i+1}", className="text-blue-800"))

space_container.add(Text("Vertical Spacing (space-y-3):", className="font-bold"))
space_container.add(vertical_space)

# Horizontal spacing
horizontal_space = Container(className="flex space-x-3")
for i in range(3):
    horizontal_space.add(Container(className="bg-green-100 p-3 rounded"))
    horizontal_space.children[-1].add(Text(f"Item {i+1}", className="text-green-800"))

space_container.add(Text("Horizontal Spacing (space-x-3):", className="font-bold"))
space_container.add(horizontal_space)

window.add_child(space_container)
```

## Borders and Shadows

### Borders

```python
# Border examples
border_container = Container(className="grid grid-cols-2 gap-4 p-4")

border_examples = [
    ("border", "Default Border"),
    ("border-2", "Thick Border"),
    ("border-4", "Extra Thick Border"),
    ("border-dashed", "Dashed Border"),
    ("border-dotted", "Dotted Border"),
    ("border-t-4", "Top Border Only"),
    ("border-l-4 border-blue-500", "Left Blue Border"),
    ("border-2 border-red-500", "Red Border"),
]

for border_class, label in border_examples:
    border_example = Container(className=f"{border_class} p-4 rounded bg-white")
    border_example.add(Text(label, className="text-gray-800 font-medium"))
    border_container.add(border_example)

window.add_child(border_container)
```

### Shadows

```python
# Shadow examples
shadow_container = Container(className="grid grid-cols-2 gap-6 p-6 bg-gray-50")

shadow_examples = [
    ("shadow-sm", "Small Shadow"),
    ("shadow", "Default Shadow"),
    ("shadow-md", "Medium Shadow"),
    ("shadow-lg", "Large Shadow"),
    ("shadow-xl", "Extra Large Shadow"),
    ("shadow-2xl", "2X Large Shadow"),
    ("shadow-inner", "Inner Shadow"),
    ("shadow-none", "No Shadow"),
]

for shadow_class, label in shadow_examples:
    shadow_example = Container(className=f"bg-white p-4 rounded {shadow_class}")
    shadow_example.add(Text(label, className="text-gray-800 font-medium"))
    shadow_container.add(shadow_example)

window.add_child(shadow_container)
```

## Rounded Corners

```python
# Rounded corner examples
rounded_container = Container(className="grid grid-cols-3 gap-4 p-4")

rounded_examples = [
    ("rounded-none", "No Rounding"),
    ("rounded-sm", "Small Rounding"),
    ("rounded", "Default Rounding"),
    ("rounded-md", "Medium Rounding"),
    ("rounded-lg", "Large Rounding"),
    ("rounded-xl", "Extra Large Rounding"),
    ("rounded-2xl", "2X Large Rounding"),
    ("rounded-3xl", "3X Large Rounding"),
    ("rounded-full", "Full Rounding"),
]

for rounded_class, label in rounded_examples:
    rounded_example = Container(className=f"bg-blue-100 p-4 {rounded_class} border-2 border-blue-300")
    rounded_example.add(Text(label, className="text-blue-800 font-medium text-center"))
    rounded_container.add(rounded_example)

window.add_child(rounded_container)
```

## Interactive States

### Hover Effects

```python
# Hover effect examples
hover_container = Container(className="space-y-4 p-4")

# Hover button
hover_button = Button(
    "Hover Me", 
    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors duration-200"
)
hover_container.add(hover_button)

# Hover card
hover_card = Container(className="bg-white p-4 rounded-lg shadow hover:shadow-lg transition-shadow duration-200 cursor-pointer")
hover_card.add(Text("Hover Card", className="font-bold text-lg"))
hover_card.add(Text("This card has a hover effect", className="text-gray-600"))
hover_container.add(hover_card)

# Color change on hover
color_hover = Container(className="bg-gray-100 hover:bg-blue-100 p-4 rounded transition-colors duration-200")
color_hover.add(Text("Hover to change background", className="text-gray-800"))
hover_container.add(color_hover)

window.add_child(hover_container)
```

### Focus States

```python
# Focus state examples (for interactive elements)
focus_container = Container(className="space-y-4 p-4")

# Focus button
focus_button = Button(
    "Focus Me", 
    className="bg-green-500 hover:bg-green-600 focus:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-400 text-white font-bold py-2 px-4 rounded"
)
focus_container.add(focus_button)

window.add_child(focus_container)
```

## Gradients

```python
# Gradient examples
gradient_container = Container(className="space-y-4 p-4")

gradient_examples = [
    ("bg-gradient-to-r from-blue-500 to-purple-600", "Blue to Purple"),
    ("bg-gradient-to-br from-green-400 to-blue-600", "Green to Blue (diagonal)"),
    ("bg-gradient-to-t from-yellow-400 via-red-500 to-pink-500", "Multi-color gradient"),
    ("bg-gradient-to-r from-purple-400 via-pink-500 to-red-500", "Purple to Red"),
]

for gradient_class, label in gradient_examples:
    gradient_example = Container(className=f"{gradient_class} p-6 rounded-lg")
    gradient_example.add(Text(label, className="text-white font-bold text-center"))
    gradient_container.add(gradient_example)

window.add_child(gradient_container)
```

## Responsive Design

### Responsive Classes

```python
# Responsive design examples
responsive_container = Container(className="p-4")

# Responsive text size
responsive_text = Text(
    "Responsive Text", 
    className="text-sm sm:text-base md:text-lg lg:text-xl xl:text-2xl font-bold text-center"
)
responsive_container.add(responsive_text)

# Responsive padding
responsive_padding = Container(className="bg-blue-100 p-2 sm:p-4 md:p-6 lg:p-8 rounded mt-4")
responsive_padding.add(Text("Responsive Padding", className="text-blue-800 font-medium"))
responsive_container.add(responsive_padding)

# Responsive grid
responsive_grid = Container(className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-4")
for i in range(8):
    grid_item = Container(className="bg-gray-200 p-3 rounded")
    grid_item.add(Text(f"Item {i+1}", className="text-center font-medium"))
    responsive_grid.add(grid_item)

responsive_container.add(responsive_grid)
window.add_child(responsive_container)
```

### Breakpoint Reference

```python
# Breakpoint demonstration
breakpoint_info = Container(className="p-4 bg-gray-50 rounded")
breakpoint_info.add(Text("Tailwind CSS Breakpoints:", className="font-bold text-lg mb-4"))

breakpoints = [
    ("sm:", "640px and up"),
    ("md:", "768px and up"),
    ("lg:", "1024px and up"),
    ("xl:", "1280px and up"),
    ("2xl:", "1536px and up"),
]

for prefix, description in breakpoints:
    breakpoint_item = Container(className="flex justify-between items-center py-2 border-b border-gray-200")
    breakpoint_item.add(Text(prefix, className="font-mono font-bold text-blue-600"))
    breakpoint_item.add(Text(description, className="text-gray-600"))
    breakpoint_info.add(breakpoint_item)

window.add_child(breakpoint_info)
```

## Component Styling Patterns

### Button Variants

```python
# Different button styles
button_variants = Container(className="space-y-4 p-4")

# Primary button
primary_btn = Button(
    "Primary", 
    className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
)
button_variants.add(primary_btn)

# Secondary button
secondary_btn = Button(
    "Secondary", 
    className="bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-4 rounded-md transition-colors"
)
button_variants.add(secondary_btn)

# Outline button
outline_btn = Button(
    "Outline", 
    className="border-2 border-blue-600 text-blue-600 hover:bg-blue-600 hover:text-white font-medium py-2 px-4 rounded-md transition-colors"
)
button_variants.add(outline_btn)

# Danger button
danger_btn = Button(
    "Danger", 
    className="bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
)
button_variants.add(danger_btn)

# Success button
success_btn = Button(
    "Success", 
    className="bg-green-600 hover:bg-green-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
)
button_variants.add(success_btn)

window.add_child(button_variants)
```

### Card Variants

```python
# Different card styles
card_variants = Container(className="grid grid-cols-1 md:grid-cols-2 gap-6 p-4")

# Simple card
simple_card = Container(className="bg-white p-6 rounded-lg shadow-md")
simple_card.add(Text("Simple Card", className="text-xl font-bold mb-2"))
simple_card.add(Text("This is a simple card with basic styling.", className="text-gray-600"))
card_variants.add(simple_card)

# Bordered card
bordered_card = Container(className="bg-white p-6 rounded-lg border-2 border-gray-200 hover:border-blue-300 transition-colors")
bordered_card.add(Text("Bordered Card", className="text-xl font-bold mb-2"))
bordered_card.add(Text("This card has a border instead of shadow.", className="text-gray-600"))
card_variants.add(bordered_card)

# Gradient card
gradient_card = Container(className="bg-gradient-to-br from-purple-500 to-pink-500 p-6 rounded-lg text-white")
gradient_card.add(Text("Gradient Card", className="text-xl font-bold mb-2"))
gradient_card.add(Text("This card has a gradient background.", className="text-purple-100"))
card_variants.add(gradient_card)

# Elevated card
elevated_card = Container(className="bg-white p-6 rounded-lg shadow-xl hover:shadow-2xl transition-shadow")
elevated_card.add(Text("Elevated Card", className="text-xl font-bold mb-2"))
elevated_card.add(Text("This card has a strong shadow effect.", className="text-gray-600"))
card_variants.add(elevated_card)

window.add_child(card_variants)
```

## Dark Mode Support

```python
# Dark mode styling (when supported)
dark_mode_container = Container(className="p-4")

# Dark mode card
dark_card = Container(className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md")
dark_card.add(Text("Dark Mode Card", className="text-gray-900 dark:text-white text-xl font-bold mb-2"))
dark_card.add(Text("This card adapts to dark mode.", className="text-gray-600 dark:text-gray-300"))
dark_mode_container.add(dark_card)

# Dark mode button
dark_button = Button(
    "Dark Mode Button", 
    className="bg-blue-600 dark:bg-blue-500 hover:bg-blue-700 dark:hover:bg-blue-600 text-white font-medium py-2 px-4 rounded-md transition-colors"
)
dark_mode_container.add(dark_button)

window.add_child(dark_mode_container)
```

## Custom Styling Utilities

### Creating Reusable Style Classes

```python
class StyleUtils:
    """Utility class for common styling patterns"""
    
    # Button styles
    BUTTON_PRIMARY = "bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
    BUTTON_SECONDARY = "bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-4 rounded-md transition-colors"
    BUTTON_DANGER = "bg-red-600 hover:bg-red-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
    
    # Card styles
    CARD_DEFAULT = "bg-white p-6 rounded-lg shadow-md"
    CARD_BORDERED = "bg-white p-6 rounded-lg border-2 border-gray-200"
    CARD_ELEVATED = "bg-white p-6 rounded-lg shadow-xl"
    
    # Text styles
    HEADING_1 = "text-3xl font-bold text-gray-900"
    HEADING_2 = "text-2xl font-bold text-gray-900"
    HEADING_3 = "text-xl font-bold text-gray-900"
    BODY_TEXT = "text-base text-gray-700"
    MUTED_TEXT = "text-sm text-gray-500"
    
    # Layout styles
    CONTAINER_CENTERED = "max-w-4xl mx-auto px-4"
    FLEX_CENTER = "flex items-center justify-center"
    GRID_RESPONSIVE = "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"

# Usage example
utils_demo = Container(className="p-4 space-y-4")

# Using style utilities
utils_demo.add(Text("Main Heading", className=StyleUtils.HEADING_1))
utils_demo.add(Text("Subheading", className=StyleUtils.HEADING_2))
utils_demo.add(Text("This is body text using our utility class.", className=StyleUtils.BODY_TEXT))
utils_demo.add(Text("This is muted text.", className=StyleUtils.MUTED_TEXT))

# Card with utility class
utility_card = Container(className=StyleUtils.CARD_DEFAULT)
utility_card.add(Text("Utility Card", className=StyleUtils.HEADING_3))
utility_card.add(Text("This card uses our predefined style.", className=StyleUtils.BODY_TEXT))
utility_card.add(Button("Primary Action", className=StyleUtils.BUTTON_PRIMARY))
utils_demo.add(utility_card)

window.add_child(utils_demo)
```

## Animation and Transitions

```python
# Animation examples
animation_container = Container(className="space-y-6 p-4")

# Transition effects
transition_card = Container(className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transform hover:scale-105 transition-all duration-300")
transition_card.add(Text("Hover Animation", className="text-xl font-bold mb-2"))
transition_card.add(Text("This card scales and changes shadow on hover.", className="text-gray-600"))
animation_container.add(transition_card)

# Color transition
color_transition = Container(className="bg-blue-100 hover:bg-blue-200 p-4 rounded transition-colors duration-500")
color_transition.add(Text("Slow Color Transition", className="text-blue-800 font-medium"))
animation_container.add(color_transition)

# Multiple transitions
multi_transition = Button(
    "Multi-Effect Button", 
    className="bg-purple-500 hover:bg-purple-600 text-white font-bold py-3 px-6 rounded-lg transform hover:scale-110 hover:shadow-lg transition-all duration-200"
)
animation_container.add(multi_transition)

window.add_child(animation_container)
```

## Complete Styling Example

Here's a complete example showcasing various styling techniques:

```python
from oneforall import App, Window, Container, Text, Button

app = App()
window = Window(title="Complete Styling Demo", size=(1000, 700))

# Main container with background
main_container = Container(className="min-h-full bg-gradient-to-br from-blue-50 to-indigo-100 p-6")

# Header section
header = Container(className="text-center mb-8")
header.add(Text("OneForAll Styling Demo", className="text-4xl font-bold text-gray-800 mb-2"))
header.add(Text("Showcasing Tailwind CSS styling capabilities", className="text-xl text-gray-600"))
main_container.add(header)

# Feature cards grid
features_grid = Container(className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8")

features = [
    {
        "title": "Colors & Typography",
        "description": "Rich color palette and typography system",
        "icon": "🎨",
        "bg": "bg-red-100",
        "text": "text-red-800",
        "button": "bg-red-500 hover:bg-red-600"
    },
    {
        "title": "Layouts & Spacing",
        "description": "Flexible layout system with consistent spacing",
        "icon": "📐",
        "bg": "bg-blue-100",
        "text": "text-blue-800",
        "button": "bg-blue-500 hover:bg-blue-600"
    },
    {
        "title": "Interactive States",
        "description": "Hover, focus, and transition effects",
        "icon": "⚡",
        "bg": "bg-green-100",
        "text": "text-green-800",
        "button": "bg-green-500 hover:bg-green-600"
    },
    {
        "title": "Responsive Design",
        "description": "Mobile-first responsive design system",
        "icon": "📱",
        "bg": "bg-purple-100",
        "text": "text-purple-800",
        "button": "bg-purple-500 hover:bg-purple-600"
    },
    {
        "title": "Shadows & Borders",
        "description": "Elegant shadows and border utilities",
        "icon": "🔲",
        "bg": "bg-yellow-100",
        "text": "text-yellow-800",
        "button": "bg-yellow-500 hover:bg-yellow-600"
    },
    {
        "title": "Animations",
        "description": "Smooth transitions and animations",
        "icon": "🎭",
        "bg": "bg-pink-100",
        "text": "text-pink-800",
        "button": "bg-pink-500 hover:bg-pink-600"
    }
]

for feature in features:
    card = Container(className=f"bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300 {feature['bg']} border border-gray-200")
    
    # Icon
    card.add(Text(feature["icon"], className="text-4xl mb-4 text-center"))
    
    # Title
    card.add(Text(feature["title"], className=f"text-xl font-bold {feature['text']} mb-3 text-center"))
    
    # Description
    card.add(Text(feature["description"], className="text-gray-600 text-center mb-4"))
    
    # Button
    card.add(Button(
        "Learn More", 
        className=f"{feature['button']} text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200 w-full"
    ))
    
    features_grid.add(card)

main_container.add(features_grid)

# Stats section
stats_section = Container(className="bg-white rounded-2xl shadow-xl p-8 mb-8")
stats_section.add(Text("Styling Statistics", className="text-2xl font-bold text-center text-gray-800 mb-6"))

stats_grid = Container(className="grid grid-cols-1 md:grid-cols-4 gap-6")

stats = [
    ("500+", "Utility Classes", "text-blue-600"),
    ("12", "Color Palettes", "text-green-600"),
    ("5", "Breakpoints", "text-purple-600"),
    ("∞", "Possibilities", "text-red-600")
]

for value, label, color in stats:
    stat_item = Container(className="text-center")
    stat_item.add(Text(value, className=f"text-4xl font-bold {color} mb-2"))
    stat_item.add(Text(label, className="text-gray-600 font-medium"))
    stats_grid.add(stat_item)

stats_section.add(stats_grid)
main_container.add(stats_section)

# Call-to-action section
cta_section = Container(className="bg-gradient-to-r from-indigo-500 to-purple-600 rounded-2xl p-8 text-center text-white")
cta_section.add(Text("Ready to Style Your App?", className="text-3xl font-bold mb-4"))
cta_section.add(Text("Start building beautiful interfaces with OneForAll and Tailwind CSS", className="text-xl text-indigo-100 mb-6"))

cta_buttons = Container(className="flex flex-col sm:flex-row gap-4 justify-center")
cta_buttons.add(Button(
    "Get Started", 
    className="bg-white text-indigo-600 font-bold py-3 px-8 rounded-lg hover:bg-gray-100 transition-colors duration-200"
))
cta_buttons.add(Button(
    "View Examples", 
    className="border-2 border-white text-white font-bold py-3 px-8 rounded-lg hover:bg-white hover:text-indigo-600 transition-colors duration-200"
))
cta_section.add(cta_buttons)

main_container.add(cta_section)

window.add_child(main_container)
app.append(window)
app.run()
```

## Styling Best Practices

### 1. Use Consistent Color Schemes

```python
# ✅ Good - Consistent color scheme
primary_color = "blue-600"
secondary_color = "gray-600"
success_color = "green-600"
danger_color = "red-600"

# Use throughout your app
primary_button = Button("Primary", className=f"bg-{primary_color} text-white")
secondary_button = Button("Secondary", className=f"bg-{secondary_color} text-white")
```

### 2. Maintain Consistent Spacing

```python
# ✅ Good - Consistent spacing scale
container = Container(className="p-4 space-y-4")  # 16px padding and spacing
card = Container(className="p-6 space-y-3")       # 24px padding, 12px spacing

# ❌ Bad - Inconsistent spacing
container = Container(className="p-3 space-y-5")  # Mixed spacing values
```

### 3. Use Semantic Class Names

```python
# ✅ Good - Semantic styling
error_message = Text("Error occurred", className="text-red-600 font-medium")
success_message = Text("Success!", className="text-green-600 font-medium")

# ❌ Bad - Non-semantic styling
red_text = Text("Error occurred", className="text-red-600 font-medium")
green_text = Text("Success!", className="text-green-600 font-medium")
```

### 4. Plan for Responsive Design

```python
# ✅ Good - Mobile-first responsive
responsive_grid = Container(className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4")

# ❌ Bad - Desktop-only design
fixed_grid = Container(className="grid grid-cols-3 gap-4")
```

## Next Steps

You now know how to:

- ✅ Apply colors, typography, and spacing
- ✅ Create borders, shadows, and rounded corners
- ✅ Use responsive design principles
- ✅ Add hover effects and transitions
- ✅ Create reusable styling utilities
- ✅ Build complete styled interfaces

## What's Next?

- [Multiple Windows](./multiple-windows) - Learn to work with multiple windows
- [Advanced Components](../api/components) - Explore all available components
- [State Management](../api/state-management) - Master reactive state management