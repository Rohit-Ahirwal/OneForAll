---
sidebar_position: 3
---

# State Management

OneForAll provides a powerful reactive state management system that automatically tracks dependencies and updates only the components that need to be refreshed when state changes. This makes building dynamic, interactive applications simple and efficient.

:::info Alpha Version
State management is a core feature in OneForAll **alpha** (v0.1.0a3). The API is stable and performant for most use cases.
:::

## Core Concepts

### What is State?

State represents the data that can change over time in your application. This includes:

- User input values
- Application settings
- UI state (like which tab is active)
- Data from external sources
- Computed values

### Reactive Updates

When state changes, OneForAll automatically:

1. Identifies which components depend on that state
2. Re-renders only those components
3. Updates the UI efficiently without full page refreshes

## Basic State Operations

### Creating State

Use `app.use_state()` to create or access state variables:

```python
from oneforall import App, Text, Button

app = App()

# Create state with initial value
counter = app.use_state('counter', 0)
user_name = app.use_state('user_name', 'Anonymous')
is_logged_in = app.use_state('logged_in', False)

# Display state in components
counter_display = Text(f"Count: {counter}")
greeting = Text(f"Hello, {user_name}!")
```

### Reading State

Access current state values using `app.get_state()`:

```python
def handle_click():
    current_count = app.get_state('counter')
    current_user = app.get_state('user_name')
    print(f"User {current_user} clicked {current_count} times")
```

### Updating State

Use `app.set_state()` to update state and trigger UI updates:

```python
def increment_counter():
    current = app.get_state('counter')
    app.set_state('counter', current + 1)

def update_user():
    app.set_state('user_name', 'John Doe')
    app.set_state('logged_in', True)

increment_btn = Button("Increment", on_click=increment_counter)
login_btn = Button("Login", on_click=update_user)
```

## Practical Examples

### Simple Counter with Multiple Displays

```python
from oneforall import App, Text, Button, Container

app = App()
window = app.create_window(title="Counter App", size=(400, 300))

# Initialize counter state
counter = app.use_state('counter', 0)

# Multiple components showing the same state
main_display = Text(f"Count: {counter}", className="text-3xl font-bold text-blue-600")
small_display = Text(f"Current value: {counter}", className="text-sm text-gray-600")
status_text = Text(
    "Even" if counter % 2 == 0 else "Odd", 
    className="text-lg font-medium text-purple-600"
)

# Event handlers
def increment():
    current = app.get_state('counter')
    app.set_state('counter', current + 1)

def decrement():
    current = app.get_state('counter')
    app.set_state('counter', current - 1)

def reset():
    app.set_state('counter', 0)

# Buttons
increment_btn = Button("+ Increment", on_click=increment)
decrement_btn = Button("- Decrement", on_click=decrement)
reset_btn = Button("Reset", on_click=reset)

# Layout
container = Container(className="p-8 space-y-4 text-center")
container.add(main_display)
container.add(small_display)
container.add(status_text)

button_row = Container(className="flex space-x-4 justify-center")
button_row.add(decrement_btn)
button_row.add(increment_btn)
button_row.add(reset_btn)

container.add(button_row)
window.add_child(container)
```

### User Profile Management

```python
from oneforall import App, Text, Button, Container

app = App()
window = app.create_window(title="User Profile", size=(500, 400))

# User state
user_name = app.use_state('user_name', 'Guest')
user_email = app.use_state('user_email', 'guest@example.com')
is_premium = app.use_state('is_premium', False)
login_count = app.use_state('login_count', 0)

# Display components that react to state changes
name_display = Text(f"Name: {user_name}", className="text-lg font-medium")
email_display = Text(f"Email: {user_email}", className="text-gray-600")
status_display = Text(
    f"Status: {'Premium' if is_premium else 'Free'}", 
    className=f"font-semibold {'text-gold-600' if is_premium else 'text-gray-500'}"
)
login_display = Text(f"Logins: {login_count}", className="text-sm text-blue-600")

# Event handlers
def upgrade_to_premium():
    app.set_state('is_premium', True)

def simulate_login():
    current_count = app.get_state('login_count')
    app.set_state('login_count', current_count + 1)

def update_profile():
    app.set_state('user_name', 'John Doe')
    app.set_state('user_email', 'john.doe@example.com')

# Buttons
upgrade_btn = Button(
    "Upgrade to Premium", 
    on_click=upgrade_to_premium,
    className="px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600"
)

login_btn = Button(
    "Simulate Login", 
    on_click=simulate_login,
    className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
)

update_btn = Button(
    "Update Profile", 
    on_click=update_profile,
    className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
)

# Layout
profile_container = Container(className="p-6 bg-white rounded-lg shadow-lg max-w-md mx-auto mt-8")
profile_container.add(Text("User Profile", className="text-2xl font-bold mb-4"))
profile_container.add(name_display)
profile_container.add(email_display)
profile_container.add(status_display)
profile_container.add(login_display)

button_container = Container(className="mt-6 space-y-2")
button_container.add(update_btn)
button_container.add(upgrade_btn)
button_container.add(login_btn)

profile_container.add(button_container)
window.add_child(profile_container)
```

### Todo List Application

```python
from oneforall import App, Text, Button, Container

app = App()
window = app.create_window(title="Todo List", size=(600, 500))

# Todo state
todos = app.use_state('todos', [])
todo_count = app.use_state('todo_count', 0)

# Helper functions
def add_todo(text):
    current_todos = app.get_state('todos')
    current_count = app.get_state('todo_count')
    
    new_todo = {
        'id': current_count + 1,
        'text': text,
        'completed': False
    }
    
    app.set_state('todos', current_todos + [new_todo])
    app.set_state('todo_count', current_count + 1)

def toggle_todo(todo_id):
    current_todos = app.get_state('todos')
    updated_todos = []
    
    for todo in current_todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
        updated_todos.append(todo)
    
    app.set_state('todos', updated_todos)

def remove_todo(todo_id):
    current_todos = app.get_state('todos')
    filtered_todos = [todo for todo in current_todos if todo['id'] != todo_id]
    app.set_state('todos', filtered_todos)

# Event handlers
def add_sample_todo():
    sample_todos = [
        "Learn OneForAll",
        "Build a desktop app",
        "Deploy to production"
    ]
    import random
    add_todo(random.choice(sample_todos))

def clear_completed():
    current_todos = app.get_state('todos')
    active_todos = [todo for todo in current_todos if not todo['completed']]
    app.set_state('todos', active_todos)

# Create todo list display
def create_todo_list():
    todo_list = Container(className="space-y-2 max-h-64 overflow-y-auto")
    current_todos = app.get_state('todos')
    
    for todo in current_todos:
        todo_item = Container(className="flex items-center space-x-3 p-2 bg-gray-50 rounded")
        
        # Todo text
        todo_text = Text(
            todo['text'],
            className=f"flex-1 {'line-through text-gray-500' if todo['completed'] else 'text-gray-800'}"
        )
        
        # Toggle button
        toggle_btn = Button(
            "✓" if todo['completed'] else "○",
            on_click=lambda tid=todo['id']: toggle_todo(tid),
            className=f"px-2 py-1 rounded {'bg-green-500 text-white' if todo['completed'] else 'bg-gray-200'}"
        )
        
        # Remove button
        remove_btn = Button(
            "✕",
            on_click=lambda tid=todo['id']: remove_todo(tid),
            className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600"
        )
        
        todo_item.add(toggle_btn)
        todo_item.add(todo_text)
        todo_item.add(remove_btn)
        todo_list.add(todo_item)
    
    return todo_list

# Main container
main_container = Container(className="p-6 max-w-lg mx-auto")
main_container.add(Text("Todo List", className="text-3xl font-bold mb-6"))

# Stats
stats_text = Text(
    f"Total: {len(todos)} | Completed: {len([t for t in todos if t.get('completed', False)])}",
    className="text-gray-600 mb-4"
)
main_container.add(stats_text)

# Add todo button
add_btn = Button(
    "Add Sample Todo",
    on_click=add_sample_todo,
    className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 mb-4"
)
main_container.add(add_btn)

# Todo list (this will be recreated on each state change)
todo_list_container = create_todo_list()
main_container.add(todo_list_container)

# Clear completed button
clear_btn = Button(
    "Clear Completed",
    on_click=clear_completed,
    className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600 mt-4"
)
main_container.add(clear_btn)

window.add_child(main_container)
```

## Advanced State Patterns

### Computed State

Create derived state values that automatically update:

```python
# Base state
items = app.use_state('items', [])
filter_type = app.use_state('filter', 'all')  # 'all', 'active', 'completed'

# Computed values (recalculated when dependencies change)
def get_filtered_items():
    all_items = app.get_state('items')
    current_filter = app.get_state('filter')
    
    if current_filter == 'active':
        return [item for item in all_items if not item.get('completed', False)]
    elif current_filter == 'completed':
        return [item for item in all_items if item.get('completed', False)]
    else:
        return all_items

def get_stats():
    all_items = app.get_state('items')
    total = len(all_items)
    completed = len([item for item in all_items if item.get('completed', False)])
    active = total - completed
    
    return {'total': total, 'completed': completed, 'active': active}

# Use computed values in components
filtered_items = get_filtered_items()
stats = get_stats()

stats_display = Text(
    f"Total: {stats['total']} | Active: {stats['active']} | Completed: {stats['completed']}",
    className="text-sm text-gray-600"
)
```

### State Validation

Add validation when updating state:

```python
def set_user_age(age):
    """Set user age with validation"""
    if isinstance(age, int) and 0 <= age <= 150:
        app.set_state('user_age', age)
        app.set_state('age_error', None)
    else:
        app.set_state('age_error', 'Age must be between 0 and 150')

def set_email(email):
    """Set email with basic validation"""
    if '@' in email and '.' in email:
        app.set_state('user_email', email)
        app.set_state('email_error', None)
    else:
        app.set_state('email_error', 'Please enter a valid email address')

# Display validation errors
age_error = app.use_state('age_error', None)
email_error = app.use_state('email_error', None)

if age_error:
    error_display = Text(age_error, className="text-red-500 text-sm")
```

### State Persistence

Save and restore state (basic pattern):

```python
import json
import os

def save_state():
    """Save current state to file"""
    state_data = {
        'user_name': app.get_state('user_name'),
        'settings': app.get_state('settings'),
        'preferences': app.get_state('preferences')
    }
    
    with open('app_state.json', 'w') as f:
        json.dump(state_data, f)

def load_state():
    """Load state from file"""
    if os.path.exists('app_state.json'):
        with open('app_state.json', 'r') as f:
            state_data = json.load(f)
            
        for key, value in state_data.items():
            app.set_state(key, value)

# Load state on app start
load_state()

# Save state button
save_btn = Button("Save Settings", on_click=save_state)
```

## Best Practices

### State Organization

```python
# ✅ Good: Use descriptive state keys
app.use_state('user_profile', {})
app.use_state('app_settings', {})
app.use_state('current_tab', 'home')

# ❌ Avoid: Generic or unclear keys
app.use_state('data', {})
app.use_state('x', 0)
app.use_state('temp', None)
```

### State Updates

```python
# ✅ Good: Update state in event handlers
def handle_form_submit():
    name = get_form_value('name')
    app.set_state('user_name', name)

# ✅ Good: Batch related updates
def login_user(user_data):
    app.set_state('user_name', user_data['name'])
    app.set_state('user_email', user_data['email'])
    app.set_state('is_logged_in', True)
    app.set_state('login_time', datetime.now())

# ❌ Avoid: Direct state mutation
# Don't modify state objects directly
user_data = app.get_state('user_profile')
user_data['name'] = 'New Name'  # This won't trigger updates!

# ✅ Good: Create new objects for updates
user_data = app.get_state('user_profile')
updated_data = {**user_data, 'name': 'New Name'}
app.set_state('user_profile', updated_data)
```

### Performance Tips

```python
# ✅ Good: Use specific state keys for different concerns
app.use_state('ui_theme', 'light')
app.use_state('user_preferences', {})
app.use_state('app_data', {})

# ✅ Good: Minimize state dependencies in components
# Only use state that the component actually needs
user_name = app.use_state('user_name', 'Guest')
welcome_text = Text(f"Welcome, {user_name}!")  # Only depends on user_name

# ❌ Avoid: Unnecessary state dependencies
all_app_state = app.use_state('entire_app_state', {})
welcome_text = Text(f"Welcome, {all_app_state.get('user', {}).get('name', 'Guest')}!")
```

## Next Steps

Now that you understand OneForAll's state management:

- [Create Beautiful Layouts](./creating-layouts) - Build complex UIs with state
- [Style with Tailwind](./styling) - Style components based on state
- [Multiple Windows](./multiple-windows) - Manage state across windows
- [API Reference](../api/state-management) - Complete state management API

---

State management is the heart of interactive OneForAll applications. Master these patterns to build dynamic, responsive desktop applications!