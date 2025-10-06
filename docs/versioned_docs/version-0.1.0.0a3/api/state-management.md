---
sidebar_position: 4
---

# State Management API Reference

OneForAll provides a reactive state management system that automatically updates the UI when state changes occur. The state system is built into the `App` class and provides a simple yet powerful way to manage application data.

:::info Alpha Version
The State Management API is stable in OneForAll **alpha** (v0.1.0a3) with full reactive functionality for desktop applications.
:::

## State Object

The state object is automatically created when you instantiate an `App` and is accessible via `app.state`. It provides methods for getting, setting, and observing state changes.

### Basic Usage

```python
from oneforall import App

app = App()

# Set state
app.state.set("user.name", "John Doe")
app.state.set("user.email", "john@example.com")
app.state.set("counter", 0)

# Get state
name = app.state.get("user.name")  # "John Doe"
counter = app.state.get("counter")  # 0

# Get with default value
theme = app.state.get("settings.theme", "light")  # "light" (default)
```

## State Methods

### set()

Sets a value in the state at the specified path.

```python
app.state.set(path, value)
```

**Parameters:**
- `path` (`str`): Dot-notation path to the state property
- `value` (`any`): The value to set

**Examples:**

```python
# Simple values
app.state.set("username", "alice")
app.state.set("isLoggedIn", True)
app.state.set("score", 100)

# Nested objects
app.state.set("user.profile.name", "Alice Smith")
app.state.set("user.profile.age", 30)

# Arrays/Lists
app.state.set("todos", [
    {"id": 1, "text": "Learn OneForAll", "completed": False},
    {"id": 2, "text": "Build an app", "completed": True}
])

# Complex objects
app.state.set("settings", {
    "theme": "dark",
    "notifications": True,
    "language": "en"
})
```

### get()

Gets a value from the state at the specified path.

```python
value = app.state.get(path, default=None)
```

**Parameters:**
- `path` (`str`): Dot-notation path to the state property
- `default` (`any`): Default value if path doesn't exist

**Returns:**
- The value at the specified path, or the default value

**Examples:**

```python
# Get simple values
username = app.state.get("username")  # "alice"
is_logged_in = app.state.get("isLoggedIn")  # True

# Get nested values
user_name = app.state.get("user.profile.name")  # "Alice Smith"
user_age = app.state.get("user.profile.age")  # 30

# Get with defaults
theme = app.state.get("settings.theme", "light")
max_items = app.state.get("config.maxItems", 10)

# Get arrays
todos = app.state.get("todos", [])
first_todo = app.state.get("todos.0.text")  # "Learn OneForAll"
```

### update()

Updates an existing object in the state by merging new values.

```python
app.state.update(path, updates)
```

**Parameters:**
- `path` (`str`): Dot-notation path to the object to update
- `updates` (`dict`): Dictionary of updates to merge

**Examples:**

```python
# Initial state
app.state.set("user", {
    "name": "John",
    "email": "john@example.com",
    "age": 25
})

# Update specific fields
app.state.update("user", {
    "age": 26,
    "city": "New York"
})

# Result: {"name": "John", "email": "john@example.com", "age": 26, "city": "New York"}

# Update nested objects
app.state.set("settings", {
    "ui": {"theme": "light", "fontSize": 14},
    "notifications": {"email": True, "push": False}
})

app.state.update("settings.ui", {"theme": "dark"})
# Result: settings.ui = {"theme": "dark", "fontSize": 14}
```

### delete()

Removes a property from the state.

```python
app.state.delete(path)
```

**Parameters:**
- `path` (`str`): Dot-notation path to the property to delete

**Examples:**

```python
# Delete simple property
app.state.delete("temporaryData")

# Delete nested property
app.state.delete("user.profile.tempField")

# Delete array item
app.state.delete("todos.0")  # Removes first todo item
```

### observe()

Observes changes to a specific path in the state.

```python
app.state.observe(path, callback)
```

**Parameters:**
- `path` (`str`): Dot-notation path to observe
- `callback` (`callable`): Function called when the path changes

**Examples:**

```python
def on_user_change(new_value, old_value):
    print(f"User changed from {old_value} to {new_value}")

def on_counter_change(new_value, old_value):
    print(f"Counter: {old_value} → {new_value}")

# Observe specific paths
app.state.observe("user.name", on_user_change)
app.state.observe("counter", on_counter_change)

# Observe nested objects
def on_settings_change(new_settings, old_settings):
    print("Settings updated:", new_settings)

app.state.observe("settings", on_settings_change)
```

### unobserve()

Removes an observer from a specific path.

```python
app.state.unobserve(path, callback)
```

**Parameters:**
- `path` (`str`): Dot-notation path to stop observing
- `callback` (`callable`): The callback function to remove

**Examples:**

```python
# Remove specific observer
app.state.unobserve("user.name", on_user_change)

# Remove all observers for a path
app.state.unobserve("counter")
```

## State Patterns

### Counter Pattern

```python
from oneforall import App, Container, Text, Button

class CounterApp:
    def __init__(self):
        self.app = App()
        self.window = self.app.create_window("Counter", (300, 200))
        
        # Initialize state
        self.app.state.set("counter", 0)
        
        # Setup UI
        self.setup_ui()
        
        # Observe state changes
        self.app.state.observe("counter", self.on_counter_change)
    
    def setup_ui(self):
        container = Container(className="p-6 text-center")
        
        # Counter display
        self.counter_display = Text(
            str(self.app.state.get("counter")),
            className="text-4xl font-bold mb-4"
        )
        
        # Buttons
        buttons = Container(className="flex space-x-4 justify-center")
        
        decrement_btn = Button(
            "-",
            className="px-4 py-2 bg-red-500 text-white rounded",
            onclick=self.decrement
        )
        
        increment_btn = Button(
            "+",
            className="px-4 py-2 bg-green-500 text-white rounded",
            onclick=self.increment
        )
        
        reset_btn = Button(
            "Reset",
            className="px-4 py-2 bg-gray-500 text-white rounded",
            onclick=self.reset
        )
        
        buttons.add(decrement_btn)
        buttons.add(increment_btn)
        buttons.add(reset_btn)
        
        container.add(self.counter_display)
        container.add(buttons)
        
        self.window.add_child(container)
    
    def increment(self):
        current = self.app.state.get("counter")
        self.app.state.set("counter", current + 1)
    
    def decrement(self):
        current = self.app.state.get("counter")
        self.app.state.set("counter", current - 1)
    
    def reset(self):
        self.app.state.set("counter", 0)
    
    def on_counter_change(self, new_value, old_value):
        """Update UI when counter changes"""
        self.counter_display.content = str(new_value)
    
    def run(self):
        self.app.run()

# Usage
counter_app = CounterApp()
counter_app.run()
```

### Todo List Pattern

```python
from oneforall import App, Container, Text, Button
import uuid

class TodoApp:
    def __init__(self):
        self.app = App()
        self.window = self.app.create_window("Todo List", (500, 600))
        
        # Initialize state
        self.app.state.set("todos", {})
        self.app.state.set("newTodoText", "")
        
        # Setup UI
        self.setup_ui()
        
        # Observe state changes
        self.app.state.observe("todos", self.on_todos_change)
    
    def setup_ui(self):
        container = Container(className="p-6")
        
        # Title
        container.add(Text("My Todos", className="text-2xl font-bold mb-6"))
        
        # Add todo form
        form = Container(className="mb-6")
        
        # Input field (simulated)
        input_container = Container(className="flex space-x-2")
        
        # New todo input (simulated with text display)
        self.new_todo_input = Container(
            className="flex-1 px-3 py-2 border border-gray-300 rounded"
        )
        self.new_todo_input.add(Text("Enter new todo...", className="text-gray-400"))
        
        add_button = Button(
            "Add",
            className="px-4 py-2 bg-blue-500 text-white rounded",
            onclick=self.add_todo
        )
        
        input_container.add(self.new_todo_input)
        input_container.add(add_button)
        form.add(input_container)
        
        # Todo list
        self.todo_list = Container(className="space-y-2")
        self.render_todos()
        
        # Stats
        self.stats = Container(className="mt-6 p-4 bg-gray-100 rounded")
        self.update_stats()
        
        container.add(form)
        container.add(self.todo_list)
        container.add(self.stats)
        
        self.window.add_child(container)
    
    def add_todo(self):
        """Add a new todo item"""
        todo_id = str(uuid.uuid4())
        new_todo = {
            "id": todo_id,
            "text": f"New Todo {len(self.app.state.get('todos', {})) + 1}",
            "completed": False,
            "created_at": "now"  # In real app, use datetime
        }
        
        todos = self.app.state.get("todos", {})
        todos[todo_id] = new_todo
        self.app.state.set("todos", todos)
    
    def toggle_todo(self, todo_id):
        """Toggle todo completion status"""
        current_status = self.app.state.get(f"todos.{todo_id}.completed", False)
        self.app.state.set(f"todos.{todo_id}.completed", not current_status)
    
    def delete_todo(self, todo_id):
        """Delete a todo item"""
        todos = self.app.state.get("todos", {})
        if todo_id in todos:
            del todos[todo_id]
            self.app.state.set("todos", todos)
    
    def render_todos(self):
        """Render the todo list"""
        self.todo_list.children.clear()
        
        todos = self.app.state.get("todos", {})
        
        if not todos:
            self.todo_list.add(Text("No todos yet. Add one above!", className="text-gray-500 italic"))
            return
        
        for todo_id, todo in todos.items():
            todo_item = self.create_todo_item(todo_id, todo)
            self.todo_list.add(todo_item)
    
    def create_todo_item(self, todo_id, todo):
        """Create a todo item component"""
        item = Container(
            className="flex items-center justify-between p-3 border rounded hover:bg-gray-50"
        )
        
        # Left side - checkbox and text
        left_side = Container(className="flex items-center space-x-3")
        
        # Checkbox
        checkbox = Button(
            "✓" if todo["completed"] else "○",
            className=f"w-6 h-6 rounded border text-sm {
                'bg-green-500 text-white' if todo['completed'] 
                else 'bg-white border-gray-300'
            }",
            onclick=lambda: self.toggle_todo(todo_id)
        )
        
        # Todo text
        text_class = "text-gray-500 line-through" if todo["completed"] else "text-gray-900"
        todo_text = Text(todo["text"], className=text_class)
        
        left_side.add(checkbox)
        left_side.add(todo_text)
        
        # Right side - delete button
        delete_btn = Button(
            "Delete",
            className="px-3 py-1 bg-red-500 text-white rounded text-sm",
            onclick=lambda: self.delete_todo(todo_id)
        )
        
        item.add(left_side)
        item.add(delete_btn)
        
        return item
    
    def update_stats(self):
        """Update todo statistics"""
        self.stats.children.clear()
        
        todos = self.app.state.get("todos", {})
        total = len(todos)
        completed = sum(1 for todo in todos.values() if todo["completed"])
        remaining = total - completed
        
        stats_text = f"Total: {total} | Completed: {completed} | Remaining: {remaining}"
        self.stats.add(Text(stats_text, className="text-sm text-gray-600"))
    
    def on_todos_change(self, new_todos, old_todos):
        """Handle todos state change"""
        self.render_todos()
        self.update_stats()
    
    def run(self):
        self.app.run()

# Usage
todo_app = TodoApp()
todo_app.run()
```

### User Profile Pattern

```python
from oneforall import App, Container, Text, Button, Image

class UserProfileApp:
    def __init__(self):
        self.app = App()
        self.window = self.app.create_window("User Profile", (600, 500))
        
        # Initialize state
        self.app.state.set("user", {
            "name": "John Doe",
            "email": "john@example.com",
            "avatar": "assets/default-avatar.png",
            "bio": "Software developer passionate about Python.",
            "settings": {
                "theme": "light",
                "notifications": True,
                "language": "en"
            }
        })
        
        self.app.state.set("editMode", False)
        
        # Setup UI
        self.setup_ui()
        
        # Observe state changes
        self.app.state.observe("user", self.on_user_change)
        self.app.state.observe("editMode", self.on_edit_mode_change)
    
    def setup_ui(self):
        container = Container(className="p-6")
        
        # Header
        header = Container(className="flex items-center justify-between mb-6")
        header.add(Text("User Profile", className="text-2xl font-bold"))
        
        self.edit_button = Button(
            "Edit",
            className="px-4 py-2 bg-blue-500 text-white rounded",
            onclick=self.toggle_edit_mode
        )
        header.add(self.edit_button)
        
        # Profile content
        self.profile_content = Container(className="space-y-6")
        self.render_profile()
        
        container.add(header)
        container.add(self.profile_content)
        
        self.window.add_child(container)
    
    def render_profile(self):
        """Render the profile content"""
        self.profile_content.children.clear()
        
        user = self.app.state.get("user", {})
        edit_mode = self.app.state.get("editMode", False)
        
        # Avatar and basic info
        profile_header = Container(className="flex items-center space-x-4 mb-6")
        
        avatar = Image(
            src=user.get("avatar", "assets/default-avatar.png"),
            alt="User Avatar",
            className="w-20 h-20 rounded-full"
        )
        
        info = Container(className="flex-1")
        
        if edit_mode:
            # Edit mode - show inputs (simulated)
            name_input = Container(className="mb-2 p-2 border rounded")
            name_input.add(Text(user.get("name", ""), className="font-semibold"))
            
            email_input = Container(className="mb-2 p-2 border rounded")
            email_input.add(Text(user.get("email", ""), className="text-gray-600"))
            
            info.add(name_input)
            info.add(email_input)
        else:
            # View mode
            info.add(Text(user.get("name", ""), className="text-xl font-semibold"))
            info.add(Text(user.get("email", ""), className="text-gray-600"))
        
        profile_header.add(avatar)
        profile_header.add(info)
        
        # Bio section
        bio_section = Container(className="mb-6")
        bio_section.add(Text("Bio", className="text-lg font-semibold mb-2"))
        
        if edit_mode:
            bio_input = Container(className="p-3 border rounded min-h-20")
            bio_input.add(Text(user.get("bio", ""), className="text-gray-700"))
            bio_section.add(bio_input)
        else:
            bio_section.add(Text(user.get("bio", ""), className="text-gray-700"))
        
        # Settings section
        settings_section = Container(className="mb-6")
        settings_section.add(Text("Settings", className="text-lg font-semibold mb-4"))
        
        settings = user.get("settings", {})
        settings_grid = Container(className="grid grid-cols-2 gap-4")
        
        # Theme setting
        theme_setting = Container(className="flex items-center justify-between p-3 bg-gray-50 rounded")
        theme_setting.add(Text("Theme", className="font-medium"))
        
        if edit_mode:
            theme_toggle = Button(
                settings.get("theme", "light").title(),
                className="px-3 py-1 bg-blue-500 text-white rounded text-sm",
                onclick=self.toggle_theme
            )
            theme_setting.add(theme_toggle)
        else:
            theme_setting.add(Text(settings.get("theme", "light").title(), className="text-gray-600"))
        
        # Notifications setting
        notif_setting = Container(className="flex items-center justify-between p-3 bg-gray-50 rounded")
        notif_setting.add(Text("Notifications", className="font-medium"))
        
        if edit_mode:
            notif_toggle = Button(
                "On" if settings.get("notifications", True) else "Off",
                className=f"px-3 py-1 text-white rounded text-sm {
                    'bg-green-500' if settings.get('notifications', True) else 'bg-red-500'
                }",
                onclick=self.toggle_notifications
            )
            notif_setting.add(notif_toggle)
        else:
            notif_setting.add(Text(
                "Enabled" if settings.get("notifications", True) else "Disabled",
                className="text-gray-600"
            ))
        
        settings_grid.add(theme_setting)
        settings_grid.add(notif_setting)
        settings_section.add(settings_grid)
        
        # Add all sections
        self.profile_content.add(profile_header)
        self.profile_content.add(bio_section)
        self.profile_content.add(settings_section)
        
        # Save/Cancel buttons in edit mode
        if edit_mode:
            actions = Container(className="flex space-x-2 justify-end")
            
            save_btn = Button(
                "Save Changes",
                className="px-4 py-2 bg-green-500 text-white rounded",
                onclick=self.save_changes
            )
            
            cancel_btn = Button(
                "Cancel",
                className="px-4 py-2 bg-gray-500 text-white rounded",
                onclick=self.cancel_edit
            )
            
            actions.add(cancel_btn)
            actions.add(save_btn)
            self.profile_content.add(actions)
    
    def toggle_edit_mode(self):
        """Toggle edit mode"""
        current_mode = self.app.state.get("editMode", False)
        self.app.state.set("editMode", not current_mode)
    
    def toggle_theme(self):
        """Toggle theme setting"""
        current_theme = self.app.state.get("user.settings.theme", "light")
        new_theme = "dark" if current_theme == "light" else "light"
        self.app.state.set("user.settings.theme", new_theme)
    
    def toggle_notifications(self):
        """Toggle notifications setting"""
        current_notif = self.app.state.get("user.settings.notifications", True)
        self.app.state.set("user.settings.notifications", not current_notif)
    
    def save_changes(self):
        """Save profile changes"""
        # In a real app, you would validate and save the changes
        self.app.state.set("editMode", False)
    
    def cancel_edit(self):
        """Cancel editing"""
        # In a real app, you would revert any unsaved changes
        self.app.state.set("editMode", False)
    
    def on_user_change(self, new_user, old_user):
        """Handle user data changes"""
        self.render_profile()
    
    def on_edit_mode_change(self, new_mode, old_mode):
        """Handle edit mode changes"""
        self.edit_button.text = "Cancel" if new_mode else "Edit"
        self.render_profile()
    
    def run(self):
        self.app.run()

# Usage
profile_app = UserProfileApp()
profile_app.run()
```

## Advanced State Patterns

### Computed State

```python
class ComputedStateExample:
    def __init__(self):
        self.app = App()
        
        # Base state
        self.app.state.set("items", [
            {"name": "Item 1", "price": 10.99, "quantity": 2},
            {"name": "Item 2", "price": 5.50, "quantity": 1},
            {"name": "Item 3", "price": 15.00, "quantity": 3}
        ])
        
        # Observe base state and compute derived values
        self.app.state.observe("items", self.compute_totals)
        
        # Initial computation
        self.compute_totals(self.app.state.get("items"), [])
    
    def compute_totals(self, new_items, old_items):
        """Compute derived state from base state"""
        total_items = len(new_items)
        total_quantity = sum(item["quantity"] for item in new_items)
        total_price = sum(item["price"] * item["quantity"] for item in new_items)
        
        # Set computed state
        self.app.state.set("computed.totalItems", total_items)
        self.app.state.set("computed.totalQuantity", total_quantity)
        self.app.state.set("computed.totalPrice", total_price)
        self.app.state.set("computed.averagePrice", total_price / total_quantity if total_quantity > 0 else 0)
```

### State Validation

```python
class ValidatedState:
    def __init__(self):
        self.app = App()
        self.validators = {}
        self.setup_validators()
    
    def setup_validators(self):
        """Setup state validators"""
        self.validators = {
            "user.email": self.validate_email,
            "user.age": self.validate_age,
            "user.name": self.validate_name
        }
        
        # Observe all user changes
        self.app.state.observe("user", self.validate_user_state)
    
    def validate_email(self, email):
        """Validate email format"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_age(self, age):
        """Validate age range"""
        return isinstance(age, int) and 0 <= age <= 150
    
    def validate_name(self, name):
        """Validate name"""
        return isinstance(name, str) and len(name.strip()) > 0
    
    def validate_user_state(self, new_user, old_user):
        """Validate user state changes"""
        errors = {}
        
        for field, validator in self.validators.items():
            value = self.app.state.get(field)
            if value is not None and not validator(value):
                errors[field] = f"Invalid {field.split('.')[-1]}"
        
        # Set validation errors
        self.app.state.set("validation.errors", errors)
        self.app.state.set("validation.isValid", len(errors) == 0)
    
    def set_user_field(self, field, value):
        """Set user field with validation"""
        self.app.state.set(f"user.{field}", value)
```

### State Persistence

```python
import json
import os

class PersistentState:
    def __init__(self, storage_file="app_state.json"):
        self.app = App()
        self.storage_file = storage_file
        
        # Load saved state
        self.load_state()
        
        # Observe state changes for auto-save
        self.app.state.observe("", self.auto_save)  # Observe all changes
    
    def load_state(self):
        """Load state from storage"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    saved_state = json.load(f)
                    
                # Restore state
                for key, value in saved_state.items():
                    self.app.state.set(key, value)
                    
            except Exception as e:
                print(f"Error loading state: {e}")
    
    def save_state(self):
        """Save current state to storage"""
        try:
            # Get all state data (this would need to be implemented in the actual state system)
            state_data = self.get_serializable_state()
            
            with open(self.storage_file, 'w') as f:
                json.dump(state_data, f, indent=2)
                
        except Exception as e:
            print(f"Error saving state: {e}")
    
    def auto_save(self, new_value, old_value):
        """Auto-save state on changes"""
        # Debounce saves to avoid excessive I/O
        if hasattr(self, '_save_timer'):
            self._save_timer.cancel()
        
        import threading
        self._save_timer = threading.Timer(1.0, self.save_state)  # Save after 1 second of inactivity
        self._save_timer.start()
    
    def get_serializable_state(self):
        """Get state data that can be serialized to JSON"""
        # This would need to be implemented based on the actual state system
        # For now, return a placeholder
        return {
            "user": self.app.state.get("user", {}),
            "settings": self.app.state.get("settings", {}),
            "data": self.app.state.get("data", {})
        }
```

## Best Practices

### State Organization

```python
# ✅ Good: Organize state hierarchically
app.state.set("user", {
    "profile": {
        "name": "John Doe",
        "email": "john@example.com"
    },
    "preferences": {
        "theme": "dark",
        "language": "en"
    },
    "session": {
        "isLoggedIn": True,
        "lastActivity": "2024-01-15T10:30:00Z"
    }
})

# ✅ Good: Use consistent naming conventions
app.state.set("ui.sidebar.isOpen", True)
app.state.set("ui.modal.currentModal", "settings")
app.state.set("data.todos.items", [])
app.state.set("data.todos.filter", "all")
```

### State Updates

```python
# ✅ Good: Use specific paths for updates
app.state.set("user.profile.name", "Jane Doe")

# ✅ Good: Use update() for partial object updates
app.state.update("user.preferences", {"theme": "light"})

# ❌ Avoid: Overwriting entire objects unnecessarily
# This replaces the entire user object
app.state.set("user", {"profile": {"name": "Jane Doe"}})  # Loses other user data
```

### Observer Management

```python
class ComponentWithObservers:
    def __init__(self, app):
        self.app = app
        self.observers = []
        self.setup_observers()
    
    def setup_observers(self):
        """Setup state observers"""
        # Keep track of observers for cleanup
        observer1 = lambda new, old: self.on_user_change(new, old)
        observer2 = lambda new, old: self.on_settings_change(new, old)
        
        self.app.state.observe("user", observer1)
        self.app.state.observe("settings", observer2)
        
        # Store references for cleanup
        self.observers.extend([
            ("user", observer1),
            ("settings", observer2)
        ])
    
    def cleanup(self):
        """Clean up observers when component is destroyed"""
        for path, observer in self.observers:
            self.app.state.unobserve(path, observer)
        self.observers.clear()
```

### Performance Optimization

```python
# ✅ Good: Batch related updates
def update_user_profile(user_data):
    # Batch updates to avoid multiple re-renders
    app.state.update("user.profile", {
        "name": user_data["name"],
        "email": user_data["email"],
        "bio": user_data["bio"]
    })

# ✅ Good: Use specific observers
app.state.observe("todos.filter", update_todo_display)  # Only observe filter changes
app.state.observe("todos.items", update_todo_list)     # Only observe items changes

# ❌ Avoid: Observing root paths unnecessarily
app.state.observe("", handle_any_change)  # This fires for ALL state changes
```

## Related APIs

- [App API](./app) - Application and state initialization
- [Components API](./components) - UI components that react to state changes
- [Window API](./window) - Window management

## Examples

See the [State Management Tutorial](../tutorial-basics/state-management) for comprehensive examples and usage patterns.

---

The State Management API provides a powerful reactive system for managing application data and automatically updating the UI when state changes occur.