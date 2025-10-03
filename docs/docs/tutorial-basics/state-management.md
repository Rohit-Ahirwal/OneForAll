---
sidebar_position: 2
---

# State Management

State management is at the heart of OneForAll applications. In this tutorial, you'll learn how to effectively manage application state, create reactive UIs, and handle complex state patterns.

## Understanding State

State in OneForAll represents the data that can change over time in your application. When state changes, OneForAll automatically updates only the components that depend on that state.

### Basic State Operations

```python
from oneforall import App

app = App()

# Create state with default value
app.use_state("user_name", "Guest")
app.use_state("counter", 0)
app.use_state("is_logged_in", False)

# Get current state value
current_name = app.use_state("user_name")
current_count = app.use_state("counter")

# Update state (triggers reactive updates)
app.set_state("user_name", "John Doe")
app.set_state("counter", 42)
app.set_state("is_logged_in", True)
```

## Reactive Components

Components automatically re-render when their dependent state changes:

```python
from oneforall import App, Window, Text, Button, Container

app = App()

# Initialize state
app.use_state("message", "Hello")
app.use_state("count", 0)

window = Window(title="Reactive Demo", size=(400, 300))
container = Container(className="p-4 space-y-4")

# This text will automatically update when 'message' state changes
message_text = Text(app.use_state("message"), className="text-xl")
container.add(message_text)

# This text will automatically update when 'count' state changes
count_text = Text(f"Count: {app.use_state('count')}", className="text-lg")
container.add(count_text)

# Buttons to update state
def update_message():
    app.set_state("message", "State updated!")

def increment_count():
    current = app.use_state("count")
    app.set_state("count", current + 1)

container.add(Button("Update Message", on_click=update_message))
container.add(Button("Increment", on_click=increment_count))

window.add_child(container)
app.append(window)
app.run()
```

## State Effects

Use effects to perform side effects when state changes:

```python
# Log when counter changes
def log_counter():
    count = app.use_state("count")
    print(f"Counter is now: {count}")

app.use_effect("count", log_counter)

# Watch multiple state variables
def log_user_info():
    name = app.use_state("user_name")
    logged_in = app.use_state("is_logged_in")
    print(f"User: {name}, Logged in: {logged_in}")

app.use_effect(["user_name", "is_logged_in"], log_user_info)
```

## Complex State Example: Todo List

Let's build a todo list to demonstrate complex state management:

```python
from oneforall import App, Window, Text, Button, Container

app = App()

# Initialize todo state
app.use_state("todos", [])
app.use_state("new_todo_text", "")
app.use_state("filter", "all")  # all, active, completed

window = Window(title="Todo App", size=(500, 600))
main_container = Container(className="p-4 space-y-4")

# Header
main_container.add(Text("Todo List", className="text-2xl font-bold text-center"))

# Add todo section (simplified - in real app you'd have an input component)
add_section = Container(className="flex space-x-2")

def add_todo():
    # In a real app, you'd get this from an input field
    todo_text = "New Todo Item"  # Placeholder
    if todo_text.strip():
        todos = app.use_state("todos")
        new_todo = {
            "id": len(todos) + 1,
            "text": todo_text,
            "completed": False
        }
        app.set_state("todos", todos + [new_todo])

add_section.add(Button("Add Todo", on_click=add_todo, className="bg-blue-500 text-white px-4 py-2 rounded"))
main_container.add(add_section)

# Filter buttons
filter_section = Container(className="flex space-x-2 justify-center")

def set_filter(filter_type):
    def handler():
        app.set_state("filter", filter_type)
    return handler

filter_section.add(Button("All", on_click=set_filter("all"), className="bg-gray-300 px-3 py-1 rounded"))
filter_section.add(Button("Active", on_click=set_filter("active"), className="bg-gray-300 px-3 py-1 rounded"))
filter_section.add(Button("Completed", on_click=set_filter("completed"), className="bg-gray-300 px-3 py-1 rounded"))

main_container.add(filter_section)

# Todo list container
todos_container = Container(className="space-y-2")

# Function to update todo list display
def update_todo_display():
    todos = app.use_state("todos")
    current_filter = app.use_state("filter")
    
    # Clear existing todos
    todos_container.clear_children()
    
    # Filter todos based on current filter
    filtered_todos = todos
    if current_filter == "active":
        filtered_todos = [todo for todo in todos if not todo["completed"]]
    elif current_filter == "completed":
        filtered_todos = [todo for todo in todos if todo["completed"]]
    
    # Create todo items
    for todo in filtered_todos:
        todo_item = Container(className="flex items-center justify-between p-2 border rounded")
        
        # Todo text with conditional styling
        text_class = "line-through text-gray-500" if todo["completed"] else "text-black"
        todo_item.add(Text(todo["text"], className=text_class))
        
        # Action buttons
        button_container = Container(className="flex space-x-1")
        
        # Toggle completion
        def toggle_todo(todo_id):
            def handler():
                todos = app.use_state("todos")
                updated_todos = []
                for t in todos:
                    if t["id"] == todo_id:
                        t = t.copy()
                        t["completed"] = not t["completed"]
                    updated_todos.append(t)
                app.set_state("todos", updated_todos)
            return handler
        
        toggle_text = "✓" if todo["completed"] else "○"
        toggle_btn = Button(
            toggle_text,
            on_click=toggle_todo(todo["id"]),
            className="bg-green-500 text-white px-2 py-1 rounded text-sm"
        )
        button_container.add(toggle_btn)
        
        # Delete todo
        def delete_todo(todo_id):
            def handler():
                todos = app.use_state("todos")
                updated_todos = [t for t in todos if t["id"] != todo_id]
                app.set_state("todos", updated_todos)
            return handler
        
        delete_btn = Button(
            "✗",
            on_click=delete_todo(todo["id"]),
            className="bg-red-500 text-white px-2 py-1 rounded text-sm"
        )
        button_container.add(delete_btn)
        
        todo_item.add(button_container)
        todos_container.add(todo_item)
    
    # Show empty state
    if not filtered_todos:
        empty_text = "No todos found"
        if current_filter == "active":
            empty_text = "No active todos"
        elif current_filter == "completed":
            empty_text = "No completed todos"
        
        todos_container.add(Text(empty_text, className="text-gray-500 text-center py-4"))

# Set up effects to update display when todos or filter changes
app.use_effect(["todos", "filter"], update_todo_display)

# Initialize display
update_todo_display()

main_container.add(todos_container)

# Stats section
stats_container = Container(className="text-center text-sm text-gray-600")

def update_stats():
    todos = app.use_state("todos")
    total = len(todos)
    completed = len([t for t in todos if t["completed"]])
    active = total - completed
    
    stats_container.clear_children()
    stats_container.add(Text(f"Total: {total} | Active: {active} | Completed: {completed}"))

app.use_effect("todos", update_stats)
update_stats()

main_container.add(stats_container)

window.add_child(main_container)
app.append(window)
app.run()
```

## State Best Practices

### 1. Initialize State Early

```python
# ✅ Good - Initialize all state at the beginning
app.use_state("user_profile", {"name": "", "email": ""})
app.use_state("settings", {"theme": "light", "notifications": True})
app.use_state("current_page", "home")

# Create your UI components after state initialization
```

### 2. Use Descriptive State Keys

```python
# ✅ Good - Clear, descriptive keys
app.use_state("shopping_cart_items", [])
app.use_state("user_authentication_status", False)
app.use_state("current_selected_product_id", None)

# ❌ Bad - Vague keys
app.use_state("items", [])
app.use_state("status", False)
app.use_state("selected", None)
```

### 3. Avoid Direct State Mutation

```python
# ✅ Good - Create new objects/arrays
current_items = app.use_state("cart_items")
new_items = current_items + [new_item]
app.set_state("cart_items", new_items)

# ✅ Good - For objects, create copies
user_profile = app.use_state("user_profile")
updated_profile = user_profile.copy()
updated_profile["name"] = "New Name"
app.set_state("user_profile", updated_profile)

# ❌ Bad - Don't mutate state directly
current_items = app.use_state("cart_items")
current_items.append(new_item)  # This won't trigger updates!
```

### 4. Use Effects for Side Effects

```python
# ✅ Good - Use effects for logging, API calls, etc.
def save_user_preferences():
    preferences = app.use_state("user_preferences")
    # Save to file or API
    with open("preferences.json", "w") as f:
        json.dump(preferences, f)

app.use_effect("user_preferences", save_user_preferences)

# ✅ Good - Use effects for computed state
def update_total_price():
    cart_items = app.use_state("cart_items")
    total = sum(item["price"] * item["quantity"] for item in cart_items)
    app.set_state("cart_total", total)

app.use_effect("cart_items", update_total_price)
```

## Advanced State Patterns

### Computed State

Create state that automatically updates based on other state:

```python
# Base state
app.use_state("first_name", "")
app.use_state("last_name", "")
app.use_state("full_name", "")

# Computed state effect
def compute_full_name():
    first = app.use_state("first_name")
    last = app.use_state("last_name")
    full = f"{first} {last}".strip()
    app.set_state("full_name", full)

app.use_effect(["first_name", "last_name"], compute_full_name)

# Initialize computed state
compute_full_name()
```

### State Validation

Add validation when updating state:

```python
def set_validated_age(age):
    if isinstance(age, int) and 0 <= age <= 150:
        app.set_state("user_age", age)
        return True
    else:
        print(f"Invalid age: {age}")
        return False

def set_validated_email(email):
    if "@" in email and "." in email:
        app.set_state("user_email", email)
        return True
    else:
        print(f"Invalid email: {email}")
        return False

# Usage
set_validated_age(25)  # ✅ Valid
set_validated_age(-5)  # ❌ Invalid, won't update state
```

### State Persistence

Save and load state from files:

```python
import json
import os

def save_app_state():
    state_to_save = {
        "user_preferences": app.use_state("user_preferences"),
        "recent_files": app.use_state("recent_files"),
        "window_settings": app.use_state("window_settings")
    }
    
    with open("app_state.json", "w") as f:
        json.dump(state_to_save, f)

def load_app_state():
    if os.path.exists("app_state.json"):
        with open("app_state.json", "r") as f:
            saved_state = json.load(f)
        
        for key, value in saved_state.items():
            app.set_state(key, value)

# Load state on app start
load_app_state()

# Save state when important data changes
app.use_effect(["user_preferences", "recent_files"], save_app_state)
```

## Debugging State

### State Logging

```python
def log_all_state_changes():
    # This would log all state changes (simplified)
    print("State changed!")

# Log specific state changes
def log_user_changes():
    user_name = app.use_state("user_name")
    user_email = app.use_state("user_email")
    print(f"User info: {user_name} ({user_email})")

app.use_effect(["user_name", "user_email"], log_user_changes)
```

### State Inspector

Create a debug component to inspect current state:

```python
def create_state_inspector():
    inspector_container = Container(className="bg-gray-100 p-4 rounded border-2 border-gray-300")
    inspector_container.add(Text("State Inspector", className="font-bold text-lg"))
    
    # Add state displays
    inspector_container.add(Text(f"Counter: {app.use_state('counter')}", className="font-mono"))
    inspector_container.add(Text(f"User: {app.use_state('user_name')}", className="font-mono"))
    inspector_container.add(Text(f"Todos: {len(app.use_state('todos'))}", className="font-mono"))
    
    return inspector_container

# Add to your main container during development
if __name__ == "__main__":
    # Add state inspector in development mode
    main_container.add(create_state_inspector())
```

## Next Steps

You now understand how to:

- ✅ Create and manage state with `use_state()` and `set_state()`
- ✅ Build reactive components that update automatically
- ✅ Use effects to handle side effects and computed state
- ✅ Implement complex state patterns like todo lists
- ✅ Follow best practices for state management
- ✅ Debug and inspect state changes

## What's Next?

- [Creating Layouts](./creating-layouts) - Build complex UI layouts
- [Styling Guide](./styling) - Master Tailwind CSS styling
- [Multiple Windows](./multiple-windows) - Manage multiple windows
- [API Reference: State Management](../api/state-management) - Detailed API documentation