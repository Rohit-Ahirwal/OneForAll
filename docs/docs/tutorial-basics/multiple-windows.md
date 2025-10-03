---
sidebar_position: 5
---

# Multiple Windows

OneForAll supports creating applications with multiple windows, allowing you to build complex desktop applications with separate windows for different purposes. This tutorial covers everything you need to know about working with multiple windows.

## Basic Multiple Windows

### Creating Multiple Windows

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Create main window
main_window = Window(title="Main Window", size=(600, 400))
main_container = Container(className="p-6")
main_container.add(Text("This is the main window", className="text-2xl font-bold mb-4"))
main_container.add(Text("You can create multiple windows in OneForAll", className="text-gray-600"))
main_window.add_child(main_container)

# Create secondary window
secondary_window = Window(title="Secondary Window", size=(400, 300))
secondary_container = Container(className="p-6 bg-blue-50")
secondary_container.add(Text("Secondary Window", className="text-xl font-bold mb-4 text-blue-800"))
secondary_container.add(Text("This is a separate window", className="text-blue-600"))
secondary_window.add_child(secondary_container)

# Add both windows to the app
app.append(main_window)
app.append(secondary_window)

app.run()
```

### Window Management

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Initialize state for window management
app.use_state("windows_created", 0)
app.use_state("secondary_visible", True)

# Main window
main_window = Window(title="Window Manager", size=(500, 400))
main_container = Container(className="p-6 space-y-4")

# Window counter
counter_text = Text(
    f"Windows created: {app.use_state('windows_created')}", 
    className="text-lg font-medium"
)
main_container.add(counter_text)

# Create new window button
def create_new_window():
    count = app.use_state("windows_created") + 1
    app.set_state("windows_created", count)
    
    # Create new window
    new_window = Window(title=f"Window {count}", size=(300, 200))
    new_container = Container(className="p-4 bg-green-50")
    new_container.add(Text(f"Window #{count}", className="text-lg font-bold text-green-800"))
    new_container.add(Text("This is a dynamically created window", className="text-green-600"))
    new_window.add_child(new_container)
    
    # Add to app
    app.append(new_window)

create_button = Button(
    "Create New Window", 
    on_click=create_new_window,
    className="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded"
)
main_container.add(create_button)

main_window.add_child(main_container)
app.append(main_window)

# Secondary window (can be toggled)
secondary_window = Window(title="Toggleable Window", size=(350, 250))
secondary_container = Container(className="p-4 bg-purple-50")
secondary_container.add(Text("Toggleable Window", className="text-lg font-bold text-purple-800"))
secondary_container.add(Text("This window can be shown/hidden", className="text-purple-600"))

# Toggle button in secondary window
def hide_secondary():
    app.set_state("secondary_visible", False)
    secondary_window.hide()

hide_button = Button(
    "Hide This Window", 
    on_click=hide_secondary,
    className="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded mt-4"
)
secondary_container.add(hide_button)
secondary_window.add_child(secondary_container)

# Show/hide toggle in main window
def toggle_secondary():
    visible = app.use_state("secondary_visible")
    if visible:
        secondary_window.hide()
        app.set_state("secondary_visible", False)
    else:
        secondary_window.show()
        app.set_state("secondary_visible", True)

toggle_button = Button(
    f"{'Hide' if app.use_state('secondary_visible') else 'Show'} Secondary Window",
    on_click=toggle_secondary,
    className="bg-purple-500 hover:bg-purple-600 text-white font-medium py-2 px-4 rounded"
)
main_container.add(toggle_button)

app.append(secondary_window)
app.run()
```

## Window Communication

### Shared State Between Windows

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Shared state
app.use_state("shared_counter", 0)
app.use_state("shared_message", "Hello from shared state!")

# Window 1 - Counter Controller
window1 = Window(title="Counter Controller", size=(400, 300))
container1 = Container(className="p-6 space-y-4")

container1.add(Text("Counter Controller", className="text-xl font-bold mb-4"))
container1.add(Text(f"Current count: {app.use_state('shared_counter')}", className="text-lg"))

def increment_counter():
    current = app.use_state("shared_counter")
    app.set_state("shared_counter", current + 1)

def decrement_counter():
    current = app.use_state("shared_counter")
    app.set_state("shared_counter", current - 1)

def reset_counter():
    app.set_state("shared_counter", 0)

button_container = Container(className="flex space-x-2")
button_container.add(Button(
    "+", 
    on_click=increment_counter,
    className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded"
))
button_container.add(Button(
    "-", 
    on_click=decrement_counter,
    className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
))
button_container.add(Button(
    "Reset", 
    on_click=reset_counter,
    className="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded"
))

container1.add(button_container)
window1.add_child(container1)

# Window 2 - Counter Display
window2 = Window(title="Counter Display", size=(400, 300))
container2 = Container(className="p-6 space-y-4 bg-blue-50")

container2.add(Text("Counter Display", className="text-xl font-bold mb-4 text-blue-800"))

# Large counter display
counter_display = Container(className="bg-white p-8 rounded-lg shadow-md text-center")
counter_display.add(Text(
    str(app.use_state("shared_counter")), 
    className="text-6xl font-bold text-blue-600"
))
container2.add(counter_display)

# Status message
status_text = "Even" if app.use_state("shared_counter") % 2 == 0 else "Odd"
container2.add(Text(f"Status: {status_text}", className="text-lg text-blue-700"))

window2.add_child(container2)

# Window 3 - Message Editor
window3 = Window(title="Message Editor", size=(450, 250))
container3 = Container(className="p-6 space-y-4 bg-green-50")

container3.add(Text("Message Editor", className="text-xl font-bold mb-4 text-green-800"))
container3.add(Text(f"Current message: {app.use_state('shared_message')}", className="text-green-700"))

def update_message(new_message):
    def handler():
        app.set_state("shared_message", new_message)
    return handler

message_buttons = Container(className="space-y-2")
messages = [
    "Hello from shared state!",
    "Counter updated!",
    "Multiple windows are awesome!",
    "OneForAll rocks!"
]

for message in messages:
    message_buttons.add(Button(
        message,
        on_click=update_message(message),
        className="w-full text-left bg-white hover:bg-green-100 text-green-800 font-medium py-2 px-4 rounded border border-green-200"
    ))

container3.add(message_buttons)
window3.add_child(container3)

# Add all windows
app.append(window1)
app.append(window2)
app.append(window3)

app.run()
```

### Event-Based Communication

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Event state
app.use_state("last_event", "No events yet")
app.use_state("event_count", 0)
app.use_state("event_history", [])

def broadcast_event(event_name, source_window):
    def handler():
        # Update event state
        app.set_state("last_event", f"{event_name} from {source_window}")
        app.set_state("event_count", app.use_state("event_count") + 1)
        
        # Add to history
        history = app.use_state("event_history").copy()
        history.append(f"{event_name} from {source_window}")
        if len(history) > 5:  # Keep only last 5 events
            history = history[-5:]
        app.set_state("event_history", history)
    
    return handler

# Event Broadcaster Window
broadcaster_window = Window(title="Event Broadcaster", size=(400, 350))
broadcaster_container = Container(className="p-6 space-y-4")

broadcaster_container.add(Text("Event Broadcaster", className="text-xl font-bold mb-4"))
broadcaster_container.add(Text("Click buttons to broadcast events:", className="text-gray-600 mb-4"))

events = [
    ("User Login", "bg-blue-500 hover:bg-blue-600"),
    ("Data Updated", "bg-green-500 hover:bg-green-600"),
    ("Error Occurred", "bg-red-500 hover:bg-red-600"),
    ("Task Completed", "bg-purple-500 hover:bg-purple-600"),
]

for event_name, button_class in events:
    broadcaster_container.add(Button(
        event_name,
        on_click=broadcast_event(event_name, "Broadcaster"),
        className=f"{button_class} text-white font-medium py-2 px-4 rounded w-full"
    ))

broadcaster_window.add_child(broadcaster_container)

# Event Monitor Window
monitor_window = Window(title="Event Monitor", size=(450, 400))
monitor_container = Container(className="p-6 space-y-4 bg-gray-50")

monitor_container.add(Text("Event Monitor", className="text-xl font-bold mb-4"))

# Current event display
current_event_card = Container(className="bg-white p-4 rounded-lg shadow-md")
current_event_card.add(Text("Last Event:", className="text-sm text-gray-600"))
current_event_card.add(Text(app.use_state("last_event"), className="text-lg font-medium"))
monitor_container.add(current_event_card)

# Event count
count_card = Container(className="bg-blue-100 p-4 rounded-lg")
count_card.add(Text("Total Events:", className="text-sm text-blue-600"))
count_card.add(Text(str(app.use_state("event_count")), className="text-2xl font-bold text-blue-800"))
monitor_container.add(count_card)

# Event history
history_card = Container(className="bg-white p-4 rounded-lg shadow-md")
history_card.add(Text("Recent Events:", className="text-sm text-gray-600 mb-2"))

history_list = Container(className="space-y-1")
for event in app.use_state("event_history"):
    history_list.add(Text(f"• {event}", className="text-sm text-gray-700"))

if not app.use_state("event_history"):
    history_list.add(Text("No events yet", className="text-sm text-gray-400 italic"))

history_card.add(history_list)
monitor_container.add(history_card)

monitor_window.add_child(monitor_container)

# Control Panel Window
control_window = Window(title="Control Panel", size=(350, 300))
control_container = Container(className="p-6 space-y-4 bg-yellow-50")

control_container.add(Text("Control Panel", className="text-xl font-bold mb-4 text-yellow-800"))

def clear_events():
    app.set_state("last_event", "Events cleared")
    app.set_state("event_count", 0)
    app.set_state("event_history", [])

def send_system_event():
    broadcast_event("System Check", "Control Panel")()

control_buttons = Container(className="space-y-2")
control_buttons.add(Button(
    "Clear All Events",
    on_click=clear_events,
    className="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded w-full"
))
control_buttons.add(Button(
    "Send System Event",
    on_click=send_system_event,
    className="bg-yellow-500 hover:bg-yellow-600 text-white font-medium py-2 px-4 rounded w-full"
))

control_container.add(control_buttons)

# System status
status_card = Container(className="bg-white p-4 rounded-lg shadow-md")
status_card.add(Text("System Status:", className="text-sm text-gray-600"))
status_text = "Active" if app.use_state("event_count") > 0 else "Idle"
status_color = "text-green-600" if app.use_state("event_count") > 0 else "text-gray-600"
status_card.add(Text(status_text, className=f"text-lg font-medium {status_color}"))
control_container.add(status_card)

control_window.add_child(control_container)

# Add all windows
app.append(broadcaster_window)
app.append(monitor_window)
app.append(control_window)

app.run()
```

## Window Positioning and Sizing

### Programmatic Window Control

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# State for window properties
app.use_state("target_window_size", (400, 300))
app.use_state("target_window_position", (100, 100))

# Main control window
control_window = Window(title="Window Controller", size=(500, 600))
control_container = Container(className="p-6 space-y-6")

control_container.add(Text("Window Controller", className="text-2xl font-bold mb-4"))

# Target window (the one we'll control)
target_window = Window(title="Controlled Window", size=(400, 300))
target_container = Container(className="p-6 bg-gradient-to-br from-purple-100 to-pink-100")
target_container.add(Text("Controlled Window", className="text-xl font-bold text-purple-800 mb-2"))
target_container.add(Text("This window is controlled by the controller", className="text-purple-600"))

# Window state display
state_display = Container(className="bg-white p-4 rounded-lg shadow-md")
state_display.add(Text("Current Window State:", className="text-lg font-bold mb-2"))
state_display.add(Text(f"Size: {target_window.size}", className="text-gray-700"))
state_display.add(Text(f"Position: {target_window.position}", className="text-gray-700"))
target_container.add(state_display)

target_window.add_child(target_container)

# Size controls
size_section = Container(className="bg-gray-50 p-4 rounded-lg")
size_section.add(Text("Size Controls", className="text-lg font-bold mb-3"))

size_buttons = Container(className="grid grid-cols-2 gap-2")
sizes = [
    ("Small", (300, 200)),
    ("Medium", (500, 400)),
    ("Large", (700, 500)),
    ("Wide", (800, 300)),
]

for label, size in sizes:
    def resize_window(new_size):
        def handler():
            target_window.size = new_size
            app.set_state("target_window_size", new_size)
        return handler
    
    size_buttons.add(Button(
        f"{label} {size[0]}x{size[1]}",
        on_click=resize_window(size),
        className="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-3 rounded text-sm"
    ))

size_section.add(size_buttons)
control_container.add(size_section)

# Position controls
position_section = Container(className="bg-gray-50 p-4 rounded-lg")
position_section.add(Text("Position Controls", className="text-lg font-bold mb-3"))

position_buttons = Container(className="grid grid-cols-3 gap-2")
positions = [
    ("Top Left", (50, 50)),
    ("Top Center", (400, 50)),
    ("Top Right", (750, 50)),
    ("Center Left", (50, 300)),
    ("Center", (400, 300)),
    ("Center Right", (750, 300)),
    ("Bottom Left", (50, 550)),
    ("Bottom Center", (400, 550)),
    ("Bottom Right", (750, 550)),
]

for label, position in positions:
    def move_window(new_position):
        def handler():
            target_window.position = new_position
            app.set_state("target_window_position", new_position)
        return handler
    
    position_buttons.add(Button(
        label,
        on_click=move_window(position),
        className="bg-green-500 hover:bg-green-600 text-white font-medium py-2 px-2 rounded text-xs"
    ))

position_section.add(position_buttons)
control_container.add(position_section)

# Window state controls
state_section = Container(className="bg-gray-50 p-4 rounded-lg")
state_section.add(Text("Window State Controls", className="text-lg font-bold mb-3"))

state_buttons = Container(className="grid grid-cols-2 gap-2")

def minimize_window():
    target_window.minimize()

def maximize_window():
    target_window.maximize()

def restore_window():
    target_window.restore()

def hide_window():
    target_window.hide()

def show_window():
    target_window.show()

def close_window():
    target_window.close()

state_actions = [
    ("Minimize", minimize_window, "bg-yellow-500 hover:bg-yellow-600"),
    ("Maximize", maximize_window, "bg-blue-500 hover:bg-blue-600"),
    ("Restore", restore_window, "bg-green-500 hover:bg-green-600"),
    ("Hide", hide_window, "bg-orange-500 hover:bg-orange-600"),
    ("Show", show_window, "bg-purple-500 hover:bg-purple-600"),
    ("Close", close_window, "bg-red-500 hover:bg-red-600"),
]

for label, action, button_class in state_actions:
    state_buttons.add(Button(
        label,
        on_click=action,
        className=f"{button_class} text-white font-medium py-2 px-4 rounded"
    ))

state_section.add(state_buttons)
control_container.add(state_section)

control_window.add_child(control_container)

# Add windows to app
app.append(control_window)
app.append(target_window)

app.run()
```

## Modal and Dialog Windows

### Creating Modal-like Windows

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# State for modal management
app.use_state("modal_visible", False)
app.use_state("modal_type", "info")
app.use_state("modal_message", "")

# Main application window
main_window = Window(title="Modal Demo", size=(600, 400))
main_container = Container(className="p-6 space-y-4")

main_container.add(Text("Modal Dialog Demo", className="text-2xl font-bold mb-4"))
main_container.add(Text("Click buttons to show different types of modal dialogs:", className="text-gray-600 mb-4"))

# Modal trigger buttons
modal_buttons = Container(className="space-y-2")

def show_modal(modal_type, message):
    def handler():
        app.set_state("modal_type", modal_type)
        app.set_state("modal_message", message)
        app.set_state("modal_visible", True)
        modal_window.show()
    return handler

modal_types = [
    ("Info", "info", "This is an information dialog", "bg-blue-500 hover:bg-blue-600"),
    ("Warning", "warning", "This is a warning dialog", "bg-yellow-500 hover:bg-yellow-600"),
    ("Error", "error", "This is an error dialog", "bg-red-500 hover:bg-red-600"),
    ("Success", "success", "Operation completed successfully!", "bg-green-500 hover:bg-green-600"),
]

for label, modal_type, message, button_class in modal_types:
    modal_buttons.add(Button(
        f"Show {label} Modal",
        on_click=show_modal(modal_type, message),
        className=f"{button_class} text-white font-medium py-2 px-4 rounded w-full"
    ))

main_container.add(modal_buttons)
main_window.add_child(main_container)

# Modal window
modal_window = Window(title="Dialog", size=(400, 250))

def create_modal_content():
    modal_type = app.use_state("modal_type")
    message = app.use_state("modal_message")
    
    # Color schemes for different modal types
    color_schemes = {
        "info": {"bg": "bg-blue-50", "text": "text-blue-800", "icon": "ℹ️", "button": "bg-blue-500 hover:bg-blue-600"},
        "warning": {"bg": "bg-yellow-50", "text": "text-yellow-800", "icon": "⚠️", "button": "bg-yellow-500 hover:bg-yellow-600"},
        "error": {"bg": "bg-red-50", "text": "text-red-800", "icon": "❌", "button": "bg-red-500 hover:bg-red-600"},
        "success": {"bg": "bg-green-50", "text": "text-green-800", "icon": "✅", "button": "bg-green-500 hover:bg-green-600"},
    }
    
    scheme = color_schemes.get(modal_type, color_schemes["info"])
    
    modal_container = Container(className=f"p-6 {scheme['bg']} h-full flex flex-col justify-between")
    
    # Header with icon and title
    header = Container(className="text-center mb-4")
    header.add(Text(scheme["icon"], className="text-4xl mb-2"))
    header.add(Text(modal_type.title(), className=f"text-xl font-bold {scheme['text']}"))
    modal_container.add(header)
    
    # Message
    message_container = Container(className="flex-1 flex items-center justify-center")
    message_container.add(Text(message, className=f"text-center {scheme['text']}"))
    modal_container.add(message_container)
    
    # Buttons
    button_container = Container(className="flex justify-center space-x-3")
    
    def close_modal():
        app.set_state("modal_visible", False)
        modal_window.hide()
    
    button_container.add(Button(
        "OK",
        on_click=close_modal,
        className=f"{scheme['button']} text-white font-medium py-2 px-6 rounded"
    ))
    
    if modal_type in ["warning", "error"]:
        button_container.add(Button(
            "Cancel",
            on_click=close_modal,
            className="bg-gray-500 hover:bg-gray-600 text-white font-medium py-2 px-6 rounded"
        ))
    
    modal_container.add(button_container)
    
    return modal_container

# Initially hide modal
modal_window.add_child(create_modal_content())

# Add windows to app
app.append(main_window)
app.append(modal_window)

# Initially hide modal window
modal_window.hide()

app.run()
```

## Window Lifecycle Management

### Advanced Window Management

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Window registry state
app.use_state("window_registry", {})
app.use_state("next_window_id", 1)

class WindowManager:
    def __init__(self, app):
        self.app = app
    
    def create_window(self, window_type, title, size=(400, 300)):
        window_id = self.app.use_state("next_window_id")
        self.app.set_state("next_window_id", window_id + 1)
        
        # Create window based on type
        if window_type == "text_editor":
            window = self.create_text_editor_window(title, size, window_id)
        elif window_type == "calculator":
            window = self.create_calculator_window(title, size, window_id)
        elif window_type == "settings":
            window = self.create_settings_window(title, size, window_id)
        else:
            window = self.create_generic_window(title, size, window_id)
        
        # Register window
        registry = self.app.use_state("window_registry").copy()
        registry[window_id] = {
            "window": window,
            "type": window_type,
            "title": title,
            "created_at": "now",  # In real app, use datetime
            "visible": True
        }
        self.app.set_state("window_registry", registry)
        
        # Add to app
        self.app.append(window)
        
        return window_id
    
    def create_text_editor_window(self, title, size, window_id):
        window = Window(title=title, size=size)
        container = Container(className="p-4 space-y-4 bg-gray-50 h-full")
        
        # Header
        header = Container(className="flex justify-between items-center bg-white p-3 rounded shadow-sm")
        header.add(Text(f"Text Editor #{window_id}", className="font-bold"))
        header.add(Button(
            "Close",
            on_click=lambda: self.close_window(window_id),
            className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm"
        ))
        container.add(header)
        
        # Content area
        content = Container(className="flex-1 bg-white p-4 rounded shadow-sm")
        content.add(Text("Text Editor Content", className="text-lg font-medium mb-2"))
        content.add(Text("This is a text editor window. You can add text editing functionality here.", className="text-gray-600"))
        container.add(content)
        
        window.add_child(container)
        return window
    
    def create_calculator_window(self, title, size, window_id):
        window = Window(title=title, size=size)
        container = Container(className="p-4 space-y-4 bg-blue-50 h-full")
        
        # Header
        header = Container(className="flex justify-between items-center bg-white p-3 rounded shadow-sm")
        header.add(Text(f"Calculator #{window_id}", className="font-bold"))
        header.add(Button(
            "Close",
            on_click=lambda: self.close_window(window_id),
            className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm"
        ))
        container.add(header)
        
        # Calculator display
        display = Container(className="bg-black text-white p-4 rounded text-right")
        display.add(Text("0", className="text-2xl font-mono"))
        container.add(display)
        
        # Calculator buttons
        buttons = Container(className="grid grid-cols-4 gap-2")
        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        
        for label in button_labels:
            buttons.add(Button(
                label,
                className="bg-white hover:bg-gray-100 border border-gray-300 py-2 px-4 rounded font-mono"
            ))
        
        container.add(buttons)
        window.add_child(container)
        return window
    
    def create_settings_window(self, title, size, window_id):
        window = Window(title=title, size=size)
        container = Container(className="p-4 space-y-4 bg-green-50 h-full")
        
        # Header
        header = Container(className="flex justify-between items-center bg-white p-3 rounded shadow-sm")
        header.add(Text(f"Settings #{window_id}", className="font-bold"))
        header.add(Button(
            "Close",
            on_click=lambda: self.close_window(window_id),
            className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm"
        ))
        container.add(header)
        
        # Settings content
        settings_content = Container(className="bg-white p-4 rounded shadow-sm space-y-3")
        settings_content.add(Text("Application Settings", className="text-lg font-bold mb-3"))
        
        settings = [
            "Enable notifications",
            "Auto-save documents",
            "Dark mode",
            "Show line numbers"
        ]
        
        for setting in settings:
            setting_row = Container(className="flex justify-between items-center py-2 border-b border-gray-200")
            setting_row.add(Text(setting, className="text-gray-700"))
            setting_row.add(Button("Toggle", className="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded text-sm"))
            settings_content.add(setting_row)
        
        container.add(settings_content)
        window.add_child(container)
        return window
    
    def create_generic_window(self, title, size, window_id):
        window = Window(title=title, size=size)
        container = Container(className="p-4 space-y-4 bg-gray-50 h-full")
        
        header = Container(className="flex justify-between items-center bg-white p-3 rounded shadow-sm")
        header.add(Text(f"Window #{window_id}", className="font-bold"))
        header.add(Button(
            "Close",
            on_click=lambda: self.close_window(window_id),
            className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm"
        ))
        container.add(header)
        
        content = Container(className="flex-1 bg-white p-4 rounded shadow-sm")
        content.add(Text("Generic Window", className="text-lg font-medium"))
        content.add(Text("This is a generic window.", className="text-gray-600"))
        container.add(content)
        
        window.add_child(container)
        return window
    
    def close_window(self, window_id):
        registry = self.app.use_state("window_registry").copy()
        if window_id in registry:
            window_info = registry[window_id]
            window_info["window"].close()
            del registry[window_id]
            self.app.set_state("window_registry", registry)
    
    def get_window_list(self):
        return list(self.app.use_state("window_registry").values())

# Create window manager
window_manager = WindowManager(app)

# Main control window
main_window = Window(title="Window Manager", size=(600, 500))
main_container = Container(className="p-6 space-y-6")

main_container.add(Text("Advanced Window Manager", className="text-2xl font-bold"))

# Window creation section
creation_section = Container(className="bg-gray-50 p-4 rounded-lg")
creation_section.add(Text("Create New Window", className="text-lg font-bold mb-3"))

window_types = [
    ("Text Editor", "text_editor", "bg-blue-500 hover:bg-blue-600"),
    ("Calculator", "calculator", "bg-green-500 hover:bg-green-600"),
    ("Settings", "settings", "bg-purple-500 hover:bg-purple-600"),
    ("Generic", "generic", "bg-gray-500 hover:bg-gray-600"),
]

creation_buttons = Container(className="grid grid-cols-2 gap-2")
for label, window_type, button_class in window_types:
    def create_window_handler(wtype, label):
        def handler():
            window_manager.create_window(wtype, f"{label} Window", (450, 350))
        return handler
    
    creation_buttons.add(Button(
        f"Create {label}",
        on_click=create_window_handler(window_type, label),
        className=f"{button_class} text-white font-medium py-2 px-4 rounded"
    ))

creation_section.add(creation_buttons)
main_container.add(creation_section)

# Window list section
list_section = Container(className="bg-gray-50 p-4 rounded-lg")
list_section.add(Text("Active Windows", className="text-lg font-bold mb-3"))

# Window count
window_count = len(app.use_state("window_registry"))
list_section.add(Text(f"Total windows: {window_count}", className="text-gray-600 mb-3"))

# Window list
window_list = Container(className="space-y-2")
for window_id, window_info in app.use_state("window_registry").items():
    window_item = Container(className="bg-white p-3 rounded shadow-sm flex justify-between items-center")
    
    info_section = Container()
    info_section.add(Text(window_info["title"], className="font-medium"))
    info_section.add(Text(f"Type: {window_info['type']} | ID: {window_id}", className="text-sm text-gray-600"))
    window_item.add(info_section)
    
    button_section = Container(className="flex space-x-2")
    button_section.add(Button(
        "Close",
        on_click=lambda wid=window_id: window_manager.close_window(wid),
        className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm"
    ))
    window_item.add(button_section)
    
    window_list.add(window_item)

if window_count == 0:
    window_list.add(Text("No active windows", className="text-gray-500 italic text-center py-4"))

list_section.add(window_list)
main_container.add(list_section)

main_window.add_child(main_container)
app.append(main_window)

app.run()
```

## Best Practices for Multiple Windows

### 1. Window State Management

```python
# ✅ Good - Centralized window state
app.use_state("window_states", {
    "main": {"visible": True, "position": (100, 100)},
    "settings": {"visible": False, "position": (200, 200)}
})

# ❌ Bad - Scattered window state
app.use_state("main_window_visible", True)
app.use_state("settings_window_visible", False)
app.use_state("main_window_x", 100)
app.use_state("main_window_y", 100)
```

### 2. Consistent Window Styling

```python
# ✅ Good - Consistent window styling
WINDOW_STYLES = {
    "header": "bg-white p-4 border-b border-gray-200",
    "content": "p-6 bg-gray-50",
    "footer": "bg-white p-4 border-t border-gray-200"
}

def create_styled_window(title, content):
    window = Window(title=title, size=(500, 400))
    container = Container(className="h-full flex flex-col")
    
    # Header
    header = Container(className=WINDOW_STYLES["header"])
    header.add(Text(title, className="text-lg font-bold"))
    container.add(header)
    
    # Content
    content_area = Container(className=WINDOW_STYLES["content"])
    content_area.add(content)
    container.add(content_area)
    
    window.add_child(container)
    return window
```

### 3. Proper Window Cleanup

```python
# ✅ Good - Proper cleanup
def close_window_properly(window_id):
    # Clean up state
    registry = app.use_state("window_registry").copy()
    if window_id in registry:
        # Save any necessary data
        window_data = registry[window_id]
        save_window_data(window_data)
        
        # Close window
        window_data["window"].close()
        
        # Remove from registry
        del registry[window_id]
        app.set_state("window_registry", registry)

# ❌ Bad - Just closing without cleanup
def close_window_bad(window):
    window.close()  # Leaves orphaned state
```

### 4. Window Communication Patterns

```python
# ✅ Good - Event-driven communication
def broadcast_to_windows(event_type, data):
    app.set_state("global_event", {
        "type": event_type,
        "data": data,
        "timestamp": time.time()
    })

# ❌ Bad - Direct window manipulation
def update_other_window(window, data):
    # Directly manipulating another window's content
    window.children[0].children[1].text = data  # Fragile and hard to maintain
```

## Complete Multiple Windows Example

Here's a complete example demonstrating multiple windows working together:

```python
from oneforall import App, Window, Container, Text, Button

app = App()

# Shared application state
app.use_state("documents", [])
app.use_state("active_document", None)
app.use_state("app_settings", {"theme": "light", "auto_save": True})

# Document Manager Window
manager_window = Window(title="Document Manager", size=(400, 500))
manager_container = Container(className="p-4 space-y-4 h-full")

manager_container.add(Text("Document Manager", className="text-xl font-bold"))

# Document list
doc_list = Container(className="bg-white p-4 rounded shadow-sm flex-1")
doc_list.add(Text("Documents:", className="font-medium mb-2"))

documents = app.use_state("documents")
if documents:
    for i, doc in enumerate(documents):
        doc_item = Container(className="flex justify-between items-center py-2 border-b border-gray-200")
        doc_item.add(Text(doc["name"], className="font-medium"))
        
        def open_doc(doc_data):
            def handler():
                app.set_state("active_document", doc_data)
                # Create editor window for this document
                create_editor_window(doc_data)
            return handler
        
        doc_item.add(Button("Open", on_click=open_doc(doc), className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm"))
        doc_list.add(doc_item)
else:
    doc_list.add(Text("No documents", className="text-gray-500 italic"))

manager_container.add(doc_list)

# Create new document
def create_new_document():
    docs = app.use_state("documents").copy()
    new_doc = {
        "id": len(docs) + 1,
        "name": f"Document {len(docs) + 1}",
        "content": "New document content..."
    }
    docs.append(new_doc)
    app.set_state("documents", docs)

manager_container.add(Button(
    "New Document",
    on_click=create_new_document,
    className="bg-green-500 hover:bg-green-600 text-white font-medium py-2 px-4 rounded w-full"
))

manager_window.add_child(manager_container)

def create_editor_window(document):
    editor_window = Window(title=f"Editor - {document['name']}", size=(600, 400))
    editor_container = Container(className="p-4 space-y-4 h-full")
    
    # Editor header
    header = Container(className="flex justify-between items-center bg-gray-100 p-3 rounded")
    header.add(Text(document["name"], className="font-bold"))
    header.add(Button("Save", className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-sm"))
    editor_container.add(header)
    
    # Editor content
    content = Container(className="flex-1 bg-white p-4 rounded shadow-sm")
    content.add(Text("Content:", className="font-medium mb-2"))
    content.add(Text(document["content"], className="text-gray-700"))
    editor_container.add(content)
    
    editor_window.add_child(editor_container)
    app.append(editor_window)

# Settings Window
settings_window = Window(title="Settings", size=(400, 300))
settings_container = Container(className="p-4 space-y-4")

settings_container.add(Text("Application Settings", className="text-xl font-bold"))

# Settings form
settings_form = Container(className="bg-gray-50 p-4 rounded space-y-3")

current_settings = app.use_state("app_settings")
settings_form.add(Text(f"Theme: {current_settings['theme']}", className="font-medium"))
settings_form.add(Text(f"Auto-save: {'Enabled' if current_settings['auto_save'] else 'Disabled'}", className="font-medium"))

def toggle_theme():
    settings = app.use_state("app_settings").copy()
    settings["theme"] = "dark" if settings["theme"] == "light" else "light"
    app.set_state("app_settings", settings)

def toggle_auto_save():
    settings = app.use_state("app_settings").copy()
    settings["auto_save"] = not settings["auto_save"]
    app.set_state("app_settings", settings)

settings_buttons = Container(className="space-y-2")
settings_buttons.add(Button("Toggle Theme", on_click=toggle_theme, className="bg-purple-500 hover:bg-purple-600 text-white font-medium py-2 px-4 rounded w-full"))
settings_buttons.add(Button("Toggle Auto-save", on_click=toggle_auto_save, className="bg-orange-500 hover:bg-orange-600 text-white font-medium py-2 px-4 rounded w-full"))

settings_form.add(settings_buttons)
settings_container.add(settings_form)
settings_window.add_child(settings_container)

# Add windows to app
app.append(manager_window)
app.append(settings_window)

# Create some sample documents
app.set_state("documents", [
    {"id": 1, "name": "Welcome.txt", "content": "Welcome to the document editor!"},
    {"id": 2, "name": "Notes.txt", "content": "These are my notes..."},
])

app.run()
```

## Next Steps

You now know how to:

- ✅ Create and manage multiple windows
- ✅ Share state between windows
- ✅ Control window positioning and sizing
- ✅ Create modal-like dialogs
- ✅ Implement proper window lifecycle management
- ✅ Follow best practices for multi-window applications

## What's Next?

- [API Reference](../api/app) - Explore the complete API
- [Advanced Examples](../examples) - See complex application examples
- [Deployment](../deployment) - Learn how to build and distribute your app