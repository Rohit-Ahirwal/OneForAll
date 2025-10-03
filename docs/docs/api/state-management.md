---
sidebar_position: 4
---

# State Management

OneForAll provides a powerful reactive state management system that automatically tracks dependencies and updates only the components that need to be refreshed when state changes.

## Core Concepts

### State Variables

State variables are key-value pairs that hold your application's data. When a state variable changes, all components that depend on it are automatically updated.

### Dependency Tracking

OneForAll automatically tracks which components depend on which state variables. When you use `app.use_state(key)` in a component, that component becomes dependent on that state key.

### Reactive Updates

When you call `app.set_state(key, value)`, OneForAll:
1. Updates the state value
2. Finds all components that depend on that state key
3. Re-renders only those components
4. Updates the UI efficiently

## State API

### `use_state(key, default=None)`

Creates or retrieves a state variable.

**Parameters:**
- `key` (str): Unique identifier for the state variable
- `default` (any, optional): Default value if state doesn't exist

**Returns:**
- Current value of the state variable

**Example:**
```python
# Initialize state with default value
count = app.use_state("count", 0)
user_name = app.use_state("user_name", "Anonymous")
items = app.use_state("todo_items", [])

# Retrieve existing state
current_count = app.use_state("count")
```

### `set_state(key, value)`

Updates a state variable and triggers reactive updates.

**Parameters:**
- `key` (str): State key to update
- `value` (any): New value for the state

**Example:**
```python
# Update simple values
app.set_state("count", 42)
app.set_state("user_name", "John Doe")

# Update complex data structures
app.set_state("user_profile", {
    "name": "Jane Smith",
    "email": "jane@example.com",
    "age": 30
})

app.set_state("todo_items", [
    {"id": 1, "text": "Learn OneForAll", "completed": False},
    {"id": 2, "text": "Build an app", "completed": True}
])
```

### `use_effect(key, callback)`

Registers a callback function that runs when specified state changes.

**Parameters:**
- `key` (str or list): State key(s) to watch
- `callback` (function): Function to call when state changes

**Example:**
```python
# Watch single state key
def on_count_change():
    count = app.use_state("count")
    print(f"Count changed to: {count}")

app.use_effect("count", on_count_change)

# Watch multiple state keys
def on_user_data_change():
    name = app.use_state("user_name")
    email = app.use_state("user_email")
    print(f"User data changed: {name} ({email})")

app.use_effect(["user_name", "user_email"], on_user_data_change)
```

## State Patterns

### Simple Counter

```python
from oneforall import App, Window, Text, Button, Container

app = App()

# Initialize counter state
app.use_state("counter", 0)

def increment():
    current = app.use_state("counter")
    app.set_state("counter", current + 1)

def decrement():
    current = app.use_state("counter")
    app.set_state("counter", current - 1)

def reset():
    app.set_state("counter", 0)

# Create UI
window = Window(title="Counter App")
container = Container(className="p-4 space-y-4 text-center")

# Counter display (automatically updates when state changes)
counter_display = Text(
    f"Count: {app.use_state('counter')}", 
    className="text-2xl font-bold"
)
container.add(counter_display)

# Buttons
button_container = Container(className="flex space-x-2 justify-center")
button_container.add(Button("−", on_click=decrement, className="bg-red-500 text-white px-4 py-2 rounded"))
button_container.add(Button("Reset", on_click=reset, className="bg-gray-500 text-white px-4 py-2 rounded"))
button_container.add(Button("+", on_click=increment, className="bg-green-500 text-white px-4 py-2 rounded"))

container.add(button_container)
window.add_child(container)
app.append(window)
app.run()
```

### Todo List

```python
from oneforall import App, Window, Text, Button, Container

app = App()

# Initialize todo state
app.use_state("todos", [])
app.use_state("new_todo", "")

def add_todo():
    new_todo_text = app.use_state("new_todo")
    if new_todo_text.strip():
        current_todos = app.use_state("todos")
        new_todo = {
            "id": len(current_todos) + 1,
            "text": new_todo_text,
            "completed": False
        }
        app.set_state("todos", current_todos + [new_todo])
        app.set_state("new_todo", "")

def toggle_todo(todo_id):
    todos = app.use_state("todos")
    updated_todos = []
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = not todo["completed"]
        updated_todos.append(todo)
    app.set_state("todos", updated_todos)

def delete_todo(todo_id):
    todos = app.use_state("todos")
    updated_todos = [todo for todo in todos if todo["id"] != todo_id]
    app.set_state("todos", updated_todos)

# Create UI
window = Window(title="Todo App", size=(500, 600))
main_container = Container(className="p-4 space-y-4")

# Header
main_container.add(Text("Todo List", className="text-2xl font-bold text-center"))

# Add todo section
add_section = Container(className="flex space-x-2")
# Note: Input component would need to be implemented
add_section.add(Button("Add Todo", on_click=add_todo, className="bg-blue-500 text-white px-4 py-2 rounded"))
main_container.add(add_section)

# Todo list (this would be dynamically generated based on state)
todos_container = Container(className="space-y-2")

# Effect to update todo list when todos change
def update_todo_list():
    todos = app.use_state("todos")
    todos_container.clear_children()
    
    for todo in todos:
        todo_item = Container(className="flex items-center justify-between p-2 border rounded")
        
        # Todo text
        text_class = "line-through text-gray-500" if todo["completed"] else ""
        todo_item.add(Text(todo["text"], className=text_class))
        
        # Buttons
        button_container = Container(className="flex space-x-1")
        
        toggle_btn = Button(
            "✓" if todo["completed"] else "○",
            on_click=lambda tid=todo["id"]: toggle_todo(tid),
            className="bg-green-500 text-white px-2 py-1 rounded text-sm"
        )
        button_container.add(toggle_btn)
        
        delete_btn = Button(
            "✗",
            on_click=lambda tid=todo["id"]: delete_todo(tid),
            className="bg-red-500 text-white px-2 py-1 rounded text-sm"
        )
        button_container.add(delete_btn)
        
        todo_item.add(button_container)
        todos_container.add(todo_item)

app.use_effect("todos", update_todo_list)

main_container.add(todos_container)
window.add_child(main_container)
app.append(window)
app.run()
```

### User Profile Management

```python
from oneforall import App, Window, Text, Button, Container

app = App()

# Initialize user profile state
app.use_state("user_profile", {
    "name": "",
    "email": "",
    "age": 0,
    "bio": ""
})

app.use_state("edit_mode", False)

def toggle_edit_mode():
    current_mode = app.use_state("edit_mode")
    app.set_state("edit_mode", not current_mode)

def update_profile_field(field, value):
    profile = app.use_state("user_profile")
    updated_profile = profile.copy()
    updated_profile[field] = value
    app.set_state("user_profile", updated_profile)

def save_profile():
    # In a real app, you'd save to a database here
    print("Profile saved!")
    app.set_state("edit_mode", False)

# Create UI
window = Window(title="User Profile", size=(400, 500))
container = Container(className="p-4 space-y-4")

# Header
container.add(Text("User Profile", className="text-2xl font-bold text-center"))

# Profile display/edit section
profile_container = Container(className="space-y-3")

# Effect to update profile display when state changes
def update_profile_display():
    profile = app.use_state("user_profile")
    edit_mode = app.use_state("edit_mode")
    
    profile_container.clear_children()
    
    if edit_mode:
        # Edit mode - show form inputs (simplified)
        profile_container.add(Text("Name:", className="font-semibold"))
        # Note: Input components would need to be implemented
        profile_container.add(Text(f"Current: {profile['name']}", className="text-sm text-gray-600"))
        
        profile_container.add(Text("Email:", className="font-semibold"))
        profile_container.add(Text(f"Current: {profile['email']}", className="text-sm text-gray-600"))
        
        # Save button
        profile_container.add(Button(
            "Save Changes",
            on_click=save_profile,
            className="bg-green-500 text-white px-4 py-2 rounded"
        ))
    else:
        # View mode - show profile data
        profile_container.add(Text(f"Name: {profile['name'] or 'Not set'}", className="text-lg"))
        profile_container.add(Text(f"Email: {profile['email'] or 'Not set'}", className="text-lg"))
        profile_container.add(Text(f"Age: {profile['age'] or 'Not set'}", className="text-lg"))
        profile_container.add(Text(f"Bio: {profile['bio'] or 'Not set'}", className="text-lg"))

app.use_effect(["user_profile", "edit_mode"], update_profile_display)

container.add(profile_container)

# Toggle edit button
edit_button = Button(
    "Edit Profile",
    on_click=toggle_edit_mode,
    className="bg-blue-500 text-white px-4 py-2 rounded"
)
container.add(edit_button)

window.add_child(container)
app.append(window)
app.run()
```

## Advanced State Patterns

### Computed State

You can create computed values that automatically update when their dependencies change:

```python
# Base state
app.use_state("first_name", "John")
app.use_state("last_name", "Doe")

# Computed full name
def update_full_name():
    first = app.use_state("first_name")
    last = app.use_state("last_name")
    full_name = f"{first} {last}".strip()
    app.set_state("full_name", full_name)

app.use_effect(["first_name", "last_name"], update_full_name)

# Initialize computed state
update_full_name()

# Now full_name will automatically update when first_name or last_name changes
```

### State Persistence

You can persist state to local storage or files:

```python
import json
import os

def save_state_to_file():
    state_data = {
        "user_preferences": app.use_state("user_preferences"),
        "recent_files": app.use_state("recent_files"),
        "window_position": app.use_state("window_position")
    }
    
    with open("app_state.json", "w") as f:
        json.dump(state_data, f)

def load_state_from_file():
    if os.path.exists("app_state.json"):
        with open("app_state.json", "r") as f:
            state_data = json.load(f)
            
        for key, value in state_data.items():
            app.set_state(key, value)

# Load state on app start
load_state_from_file()

# Save state when important data changes
app.use_effect(["user_preferences", "recent_files"], save_state_to_file)
```

### State Validation

You can add validation when setting state:

```python
def set_validated_state(key, value, validator=None):
    if validator and not validator(value):
        print(f"Invalid value for {key}: {value}")
        return False
    
    app.set_state(key, value)
    return True

# Validators
def validate_email(email):
    return "@" in email and "." in email

def validate_age(age):
    return isinstance(age, int) and 0 <= age <= 150

# Usage
set_validated_state("user_email", "user@example.com", validate_email)
set_validated_state("user_age", 25, validate_age)
```

## Best Practices

### 1. Use Descriptive State Keys

```python
# ✅ Good
app.use_state("user_profile_name", "")
app.use_state("shopping_cart_items", [])
app.use_state("is_loading_data", False)

# ❌ Bad
app.use_state("name", "")
app.use_state("items", [])
app.use_state("loading", False)
```

### 2. Initialize State Early

```python
# ✅ Good - Initialize all state at app startup
app.use_state("counter", 0)
app.use_state("user_name", "Guest")
app.use_state("settings", {"theme": "light"})

# Create UI components that use the state
```

### 3. Use Effects for Side Effects

```python
# ✅ Good - Use effects for logging, API calls, etc.
def log_counter_changes():
    count = app.use_state("counter")
    print(f"Counter changed to: {count}")

app.use_effect("counter", log_counter_changes)

# ✅ Good - Use effects for derived state
def update_counter_display():
    count = app.use_state("counter")
    display_text = f"Count: {count} ({'even' if count % 2 == 0 else 'odd'})"
    app.set_state("counter_display", display_text)

app.use_effect("counter", update_counter_display)
```

### 4. Avoid Direct State Mutation

```python
# ✅ Good - Create new objects/arrays
current_items = app.use_state("items")
new_items = current_items + [new_item]
app.set_state("items", new_items)

# ❌ Bad - Don't mutate state directly
current_items = app.use_state("items")
current_items.append(new_item)  # This won't trigger updates
```

## See Also

- [App](./app) - Main application class with state methods
- [Components](./components) - How components interact with state
- [Tutorial: State Management](../tutorial-basics/state-management) - Step-by-step state tutorial