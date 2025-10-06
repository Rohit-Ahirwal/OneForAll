---
sidebar_position: 5
---

# Styling with Tailwind CSS

OneForAll integrates seamlessly with Tailwind CSS, providing a powerful utility-first approach to styling your desktop applications. Learn how to create beautiful, responsive interfaces with minimal custom CSS.

:::info Alpha Version
Tailwind CSS integration is fully functional in OneForAll **alpha** (v0.1.0a3). The CLI automatically scans and builds your styles.
:::

## Getting Started with Tailwind

### Automatic CSS Generation

OneForAll automatically scans your Python files for Tailwind classes and generates the necessary CSS:

```bash
# Development mode (auto-rebuilds CSS)
oneforall dev

# Manual CSS build
oneforall css
```

### Basic Styling

Apply Tailwind classes using the `className` parameter:

```python
from oneforall import Container, Text, Button

# Basic styling
styled_text = Text(
    "Welcome to OneForAll", 
    className="text-2xl font-bold text-blue-600 mb-4"
)

# Styled button
primary_button = Button(
    "Get Started", 
    className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
)

# Styled container
card = Container(className="bg-white rounded-lg shadow-lg p-6 max-w-md mx-auto")
card.add(styled_text)
card.add(primary_button)
```

## Typography

### Text Styling

```python
# Headings
heading_1 = Text("Main Title", className="text-4xl font-bold text-gray-900 mb-4")
heading_2 = Text("Subtitle", className="text-2xl font-semibold text-gray-700 mb-3")
heading_3 = Text("Section Title", className="text-xl font-medium text-gray-600 mb-2")

# Body text
paragraph = Text(
    "This is a paragraph with proper typography styling for readability.",
    className="text-base text-gray-600 leading-relaxed mb-4"
)

# Small text
caption = Text("Caption text", className="text-sm text-gray-500")

# Text variations
bold_text = Text("Bold text", className="font-bold")
italic_text = Text("Italic text", className="italic")
underlined_text = Text("Underlined text", className="underline")
```

### Text Colors and Alignment

```python
# Color variations
primary_text = Text("Primary text", className="text-blue-600")
success_text = Text("Success message", className="text-green-600")
warning_text = Text("Warning message", className="text-yellow-600")
error_text = Text("Error message", className="text-red-600")

# Text alignment
left_aligned = Text("Left aligned", className="text-left")
center_aligned = Text("Center aligned", className="text-center")
right_aligned = Text("Right aligned", className="text-right")
justified = Text("Justified text content", className="text-justify")

# Text transform
uppercase_text = Text("uppercase text", className="uppercase")
lowercase_text = Text("LOWERCASE TEXT", className="lowercase")
capitalized_text = Text("capitalized text", className="capitalize")
```

## Colors and Backgrounds

### Background Colors

```python
# Solid backgrounds
white_bg = Container(className="bg-white p-4")
gray_bg = Container(className="bg-gray-100 p-4")
blue_bg = Container(className="bg-blue-500 p-4")
gradient_bg = Container(className="bg-gradient-to-r from-blue-500 to-purple-600 p-4")

# Background with opacity
transparent_bg = Container(className="bg-black bg-opacity-50 p-4")
```

### Color Palette

```python
def create_color_palette():
    """Demonstrate OneForAll color palette"""
    palette = Container(className="grid grid-cols-2 md:grid-cols-4 gap-4 p-6")
    
    colors = [
        ("Primary", "bg-blue-500", "text-white"),
        ("Secondary", "bg-gray-500", "text-white"),
        ("Success", "bg-green-500", "text-white"),
        ("Warning", "bg-yellow-500", "text-black"),
        ("Error", "bg-red-500", "text-white"),
        ("Info", "bg-cyan-500", "text-white"),
        ("Light", "bg-gray-100", "text-gray-800"),
        ("Dark", "bg-gray-800", "text-white")
    ]
    
    for name, bg_color, text_color in colors:
        color_card = Container(className=f"{bg_color} {text_color} p-4 rounded-lg text-center")
        color_card.add(Text(name, className="font-semibold"))
        palette.add(color_card)
    
    return palette
```

## Spacing and Layout

### Padding and Margins

```python
# Padding variations
small_padding = Container(className="p-2")      # 8px
medium_padding = Container(className="p-4")     # 16px
large_padding = Container(className="p-6")      # 24px
extra_large_padding = Container(className="p-8") # 32px

# Directional padding
top_padding = Container(className="pt-4")
right_padding = Container(className="pr-4")
bottom_padding = Container(className="pb-4")
left_padding = Container(className="pl-4")

# Horizontal and vertical padding
horizontal_padding = Container(className="px-4")  # left and right
vertical_padding = Container(className="py-4")    # top and bottom

# Margins (similar to padding)
margin_container = Container(className="m-4 mx-auto")  # margin with auto centering
```

### Spacing Between Elements

```python
# Vertical spacing
vertical_stack = Container(className="space-y-4")
vertical_stack.add(Text("Item 1"))
vertical_stack.add(Text("Item 2"))
vertical_stack.add(Text("Item 3"))

# Horizontal spacing
horizontal_stack = Container(className="flex space-x-4")
horizontal_stack.add(Button("Button 1"))
horizontal_stack.add(Button("Button 2"))
horizontal_stack.add(Button("Button 3"))
```

## Borders and Shadows

### Border Styling

```python
# Basic borders
bordered_container = Container(className="border border-gray-300 p-4")

# Border variations
thick_border = Container(className="border-2 border-blue-500 p-4")
dashed_border = Container(className="border-2 border-dashed border-gray-400 p-4")
rounded_border = Container(className="border border-gray-300 rounded-lg p-4")

# Directional borders
top_border = Container(className="border-t-2 border-blue-500 p-4")
bottom_border = Container(className="border-b border-gray-300 p-4")
```

### Shadow Effects

```python
# Shadow variations
small_shadow = Container(className="shadow-sm bg-white p-4 rounded")
medium_shadow = Container(className="shadow-md bg-white p-4 rounded")
large_shadow = Container(className="shadow-lg bg-white p-4 rounded")
extra_large_shadow = Container(className="shadow-xl bg-white p-4 rounded")

# Colored shadows
blue_shadow = Container(className="shadow-lg shadow-blue-500/25 bg-white p-4 rounded")
```

## Interactive States

### Hover Effects

```python
# Hover color changes
hover_button = Button(
    "Hover Me", 
    className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
)

# Hover transformations
hover_card = Container(className="bg-white p-4 rounded-lg shadow hover:shadow-lg hover:scale-105 transition-all duration-200")

# Hover text effects
hover_text = Text(
    "Hover for effect", 
    className="text-blue-500 hover:text-blue-700 hover:underline cursor-pointer"
)
```

### Focus and Active States

```python
# Focus styles (for interactive elements)
focused_button = Button(
    "Focus Me", 
    className="px-4 py-2 bg-blue-500 text-white rounded focus:outline-none focus:ring-2 focus:ring-blue-300"
)

# Active states
active_button = Button(
    "Press Me", 
    className="px-4 py-2 bg-blue-500 text-white rounded active:bg-blue-700 active:scale-95 transition-all"
)
```

## Responsive Design

### Breakpoint-Specific Styles

```python
# Responsive text sizes
responsive_title = Text(
    "Responsive Title", 
    className="text-lg sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl font-bold"
)

# Responsive padding
responsive_container = Container(className="p-2 sm:p-4 md:p-6 lg:p-8")

# Responsive grid
responsive_grid = Container(className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4")

# Show/hide on different screens
mobile_only = Text("Mobile Only", className="block sm:hidden")
desktop_only = Text("Desktop Only", className="hidden lg:block")
```

### Mobile-First Approach

```python
def create_responsive_card():
    """Create a card that adapts to different screen sizes"""
    
    card = Container(className="bg-white rounded-lg shadow-md overflow-hidden")
    
    # Responsive image container
    image_container = Container(className="h-32 sm:h-48 md:h-64 bg-gray-200")
    
    # Responsive content
    content = Container(className="p-3 sm:p-4 md:p-6")
    
    # Responsive title
    title = Text(
        "Responsive Card Title", 
        className="text-base sm:text-lg md:text-xl font-bold mb-2"
    )
    
    # Responsive description
    description = Text(
        "This card adapts its layout and typography based on screen size.",
        className="text-sm sm:text-base text-gray-600 mb-3 sm:mb-4"
    )
    
    # Responsive button
    button = Button(
        "Learn More", 
        className="w-full sm:w-auto px-3 sm:px-4 py-2 bg-blue-500 text-white rounded text-sm sm:text-base"
    )
    
    content.add(title)
    content.add(description)
    content.add(button)
    
    card.add(image_container)
    card.add(content)
    
    return card
```

## Component Styling Patterns

### Button Variants

```python
def create_button_variants():
    """Create different button styles"""
    
    container = Container(className="space-y-4 p-6")
    
    # Primary button
    primary = Button(
        "Primary", 
        className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300 transition-all"
    )
    
    # Secondary button
    secondary = Button(
        "Secondary", 
        className="px-6 py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-300 transition-all"
    )
    
    # Outline button
    outline = Button(
        "Outline", 
        className="px-6 py-3 border-2 border-blue-500 text-blue-500 rounded-lg hover:bg-blue-500 hover:text-white focus:outline-none focus:ring-2 focus:ring-blue-300 transition-all"
    )
    
    # Ghost button
    ghost = Button(
        "Ghost", 
        className="px-6 py-3 text-blue-500 rounded-lg hover:bg-blue-50 focus:outline-none focus:ring-2 focus:ring-blue-300 transition-all"
    )
    
    # Danger button
    danger = Button(
        "Danger", 
        className="px-6 py-3 bg-red-500 text-white rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-300 transition-all"
    )
    
    container.add(primary)
    container.add(secondary)
    container.add(outline)
    container.add(ghost)
    container.add(danger)
    
    return container
```

### Card Components

```python
def create_styled_cards():
    """Create various card styles"""
    
    cards_container = Container(className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6")
    
    # Basic card
    basic_card = Container(className="bg-white rounded-lg shadow-md p-6")
    basic_card.add(Text("Basic Card", className="text-xl font-bold mb-2"))
    basic_card.add(Text("Simple card with shadow", className="text-gray-600"))
    
    # Elevated card
    elevated_card = Container(className="bg-white rounded-lg shadow-xl p-6 hover:shadow-2xl transition-shadow")
    elevated_card.add(Text("Elevated Card", className="text-xl font-bold mb-2"))
    elevated_card.add(Text("Card with hover effect", className="text-gray-600"))
    
    # Bordered card
    bordered_card = Container(className="bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-blue-300 transition-colors")
    bordered_card.add(Text("Bordered Card", className="text-xl font-bold mb-2"))
    bordered_card.add(Text("Card with border styling", className="text-gray-600"))
    
    # Gradient card
    gradient_card = Container(className="bg-gradient-to-br from-purple-500 to-pink-500 text-white rounded-lg p-6")
    gradient_card.add(Text("Gradient Card", className="text-xl font-bold mb-2"))
    gradient_card.add(Text("Card with gradient background", className="text-purple-100"))
    
    cards_container.add(basic_card)
    cards_container.add(elevated_card)
    cards_container.add(bordered_card)
    cards_container.add(gradient_card)
    
    return cards_container
```

## Advanced Styling Techniques

### CSS Grid Layouts

```python
# Complex grid layout
grid_container = Container(className="grid grid-cols-4 grid-rows-3 gap-4 h-96")

# Grid item spanning multiple columns/rows
header_item = Container(className="col-span-4 bg-blue-500 text-white p-4 rounded")
header_item.add(Text("Header (spans 4 columns)", className="font-bold"))

sidebar_item = Container(className="row-span-2 bg-gray-200 p-4 rounded")
sidebar_item.add(Text("Sidebar (spans 2 rows)", className="font-semibold"))

main_item = Container(className="col-span-2 bg-white border p-4 rounded"))
main_item.add(Text("Main Content", className="font-semibold"))

aside_item = Container(className="bg-gray-100 p-4 rounded"))
aside_item.add(Text("Aside", className="font-semibold"))

footer_item = Container(className="col-span-3 bg-gray-800 text-white p-4 rounded"))
footer_item.add(Text("Footer (spans 3 columns)", className="font-bold"))

grid_container.add(header_item)
grid_container.add(sidebar_item)
grid_container.add(main_item)
grid_container.add(aside_item)
grid_container.add(footer_item)
```

### Animations and Transitions

```python
# Smooth transitions
animated_button = Button(
    "Animated Button", 
    className="px-6 py-3 bg-blue-500 text-white rounded-lg transform hover:scale-105 hover:bg-blue-600 transition-all duration-300 ease-in-out"
)

# Loading animation
loading_spinner = Container(className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500")

# Fade in animation
fade_in_container = Container(className="animate-fade-in opacity-0 animate-delay-300")

# Pulse animation
pulse_notification = Container(className="animate-pulse bg-red-500 text-white p-2 rounded")
pulse_notification.add(Text("New notification!", className="font-semibold"))
```

### Custom Utility Classes

```python
# Create reusable style patterns
BUTTON_STYLES = {
    'primary': 'px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300 transition-all',
    'secondary': 'px-6 py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-300 transition-all',
    'danger': 'px-6 py-3 bg-red-500 text-white rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-300 transition-all'
}

CARD_STYLES = {
    'default': 'bg-white rounded-lg shadow-md p-6',
    'elevated': 'bg-white rounded-lg shadow-xl p-6 hover:shadow-2xl transition-shadow',
    'bordered': 'bg-white border-2 border-gray-200 rounded-lg p-6 hover:border-blue-300 transition-colors'
}

# Usage
primary_button = Button("Save", className=BUTTON_STYLES['primary'])
info_card = Container(className=CARD_STYLES['elevated'])
```

## Dark Mode Support

```python
def create_dark_mode_component():
    """Create a component that supports dark mode"""
    
    # Container with dark mode variants
    container = Container(className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg")
    
    # Text with dark mode
    title = Text(
        "Dark Mode Example", 
        className="text-2xl font-bold text-gray-900 dark:text-white mb-4"
    )
    
    description = Text(
        "This component adapts to dark mode automatically.",
        className="text-gray-600 dark:text-gray-300 mb-4"
    )
    
    # Button with dark mode
    button = Button(
        "Toggle Theme", 
        className="px-4 py-2 bg-blue-500 dark:bg-blue-600 text-white rounded hover:bg-blue-600 dark:hover:bg-blue-700 transition-colors"
    )
    
    container.add(title)
    container.add(description)
    container.add(button)
    
    return container
```

## Performance Best Practices

### Efficient Class Usage

```python
# ✅ Good: Combine related classes
efficient_button = Button(
    "Efficient", 
    className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
)

# ❌ Avoid: Redundant or conflicting classes
inefficient_button = Button(
    "Inefficient", 
    className="px-4 py-2 p-3 bg-blue-500 bg-red-500 text-white rounded"  # conflicting classes
)
```

### Reusable Style Patterns

```python
# Create a style system
class StyleSystem:
    COLORS = {
        'primary': 'blue-500',
        'secondary': 'gray-500',
        'success': 'green-500',
        'warning': 'yellow-500',
        'danger': 'red-500'
    }
    
    SIZES = {
        'sm': 'px-3 py-1 text-sm',
        'md': 'px-4 py-2 text-base',
        'lg': 'px-6 py-3 text-lg'
    }
    
    @classmethod
    def button(cls, variant='primary', size='md', extra_classes=''):
        base = f"rounded font-medium transition-colors focus:outline-none focus:ring-2"
        color = f"bg-{cls.COLORS[variant]} hover:bg-{cls.COLORS[variant].replace('500', '600')} text-white focus:ring-{cls.COLORS[variant].replace('500', '300')}"
        size_classes = cls.SIZES[size]
        return f"{base} {color} {size_classes} {extra_classes}".strip()

# Usage
styled_button = Button("Click Me", className=StyleSystem.button('primary', 'lg', 'w-full'))
```

## Debugging Styles

### Common Issues and Solutions

```python
# ✅ Proper container setup
proper_container = Container(className="flex flex-col space-y-4 p-4")

# ❌ Common mistake: Missing flex direction
improper_container = Container(className="flex space-y-4 p-4")  # space-y won't work with flex-row

# ✅ Proper responsive classes
responsive_text = Text("Responsive", className="text-sm md:text-base lg:text-lg")

# ❌ Common mistake: Wrong breakpoint order
wrong_responsive = Text("Wrong", className="text-lg md:text-base text-sm")  # should be mobile-first
```

## Next Steps

Now that you've mastered OneForAll styling:

- [Multiple Windows](./multiple-windows) - Style across multiple windows
- [API Reference](../api/components) - Complete styling API
- [Advanced Patterns](../advanced/custom-components) - Create custom styled components

---

With Tailwind CSS and OneForAll, you have everything needed to create beautiful, professional desktop applications!