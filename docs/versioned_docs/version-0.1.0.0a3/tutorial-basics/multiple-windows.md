---
sidebar_position: 6
---

# Multiple Windows

OneForAll supports creating applications with multiple windows, allowing you to build complex desktop applications with separate interfaces, dialogs, and tool windows. Learn how to create, manage, and coordinate multiple windows effectively.

:::info Alpha Version
Multiple window support is fully functional in OneForAll **alpha** (v0.1.0a3). Window management APIs are stable and ready for use.
:::

## Creating Multiple Windows

### Basic Multi-Window Setup

```python
from oneforall import App, Container, Text, Button

app = App()

# Create main window
main_window = app.create_window(
    title="Main Application",
    size=(800, 600),
    position=(100, 100)
)

# Create secondary window
settings_window = app.create_window(
    title="Settings",
    size=(400, 300),
    position=(200, 200)
)

# Add content to main window
main_content = Container(className="p-6")
main_content.add(Text("Main Application Window", className="text-2xl font-bold mb-4"))
main_content.add(Button("Open Settings", className="px-4 py-2 bg-blue-500 text-white rounded"))

main_window.add_child(main_content)

# Add content to settings window
settings_content = Container(className="p-6")
settings_content.add(Text("Settings Window", className="text-xl font-bold mb-4"))
settings_content.add(Text("Configure your application here.", className="text-gray-600"))

settings_window.add_child(settings_content)

# Run the application
app.run()
```

### Window Configuration Options

```python
# Create windows with different configurations
main_window = app.create_window(
    title="Main Window",
    size=(1000, 700),
    position=(100, 100),
    resizable=True,
    minimizable=True,
    maximizable=True,
    on_top=False
)

# Modal dialog window
dialog_window = app.create_window(
    title="Dialog",
    size=(300, 200),
    position=(400, 300),
    resizable=False,
    minimizable=False,
    maximizable=False,
    on_top=True  # Always on top
)

# Tool window
tool_window = app.create_window(
    title="Tools",
    size=(250, 500),
    position=(50, 100),
    resizable=True,
    minimizable=True,
    maximizable=False
)
```

## Window Communication

### Shared State Between Windows

```python
from oneforall import App, Container, Text, Button

class MultiWindowApp:
    def __init__(self):
        self.app = App()
        
        # Shared application state
        self.shared_state = {
            'user_name': 'John Doe',
            'theme': 'light',
            'settings': {
                'notifications': True,
                'auto_save': True
            }
        }
        
        self.setup_windows()
    
    def setup_windows(self):
        # Main window
        self.main_window = self.app.create_window(
            title="Main Application",
            size=(800, 600)
        )
        
        # Settings window
        self.settings_window = self.app.create_window(
            title="Settings",
            size=(400, 500)
        )
        
        # Profile window
        self.profile_window = self.app.create_window(
            title="User Profile",
            size=(350, 400)
        )
        
        self.build_main_window()
        self.build_settings_window()
        self.build_profile_window()
    
    def build_main_window(self):
        """Build the main application window"""
        container = Container(className="p-6")
        
        # Header with user info
        header = Container(className="flex justify-between items-center mb-6 pb-4 border-b")
        header.add(Text(f"Welcome, {self.shared_state['user_name']}", className="text-xl font-bold"))
        
        # Window controls
        controls = Container(className="flex space-x-2")
        controls.add(Button("Settings", className="px-3 py-1 bg-gray-200 rounded text-sm"))
        controls.add(Button("Profile", className="px-3 py-1 bg-blue-500 text-white rounded text-sm"))
        
        header.add(controls)
        
        # Main content
        content = Container(className="space-y-4")
        content.add(Text("Main Application Content", className="text-lg font-semibold"))
        content.add(Text(f"Current theme: {self.shared_state['theme']}", className="text-gray-600"))
        content.add(Text(f"Notifications: {'On' if self.shared_state['settings']['notifications'] else 'Off'}", className="text-gray-600"))
        
        container.add(header)
        container.add(content)
        self.main_window.add_child(container)
    
    def build_settings_window(self):
        """Build the settings window"""
        container = Container(className="p-6")
        
        container.add(Text("Application Settings", className="text-xl font-bold mb-6"))
        
        # Theme setting
        theme_section = Container(className="mb-6")
        theme_section.add(Text("Theme", className="font-semibold mb-2"))
        
        theme_buttons = Container(className="flex space-x-2")
        theme_buttons.add(Button("Light", className="px-3 py-1 bg-white border rounded text-sm"))
        theme_buttons.add(Button("Dark", className="px-3 py-1 bg-gray-800 text-white rounded text-sm"))
        
        theme_section.add(theme_buttons)
        
        # Notification settings
        notification_section = Container(className="mb-6")
        notification_section.add(Text("Notifications", className="font-semibold mb-2"))
        notification_section.add(Button("Toggle Notifications", className="px-3 py-1 bg-blue-500 text-white rounded text-sm"))
        
        # Auto-save settings
        autosave_section = Container(className="mb-6")
        autosave_section.add(Text("Auto Save", className="font-semibold mb-2"))
        autosave_section.add(Button("Toggle Auto Save", className="px-3 py-1 bg-green-500 text-white rounded text-sm"))
        
        container.add(theme_section)
        container.add(notification_section)
        container.add(autosave_section)
        
        self.settings_window.add_child(container)
    
    def build_profile_window(self):
        """Build the user profile window"""
        container = Container(className="p-6")
        
        container.add(Text("User Profile", className="text-xl font-bold mb-6"))
        
        # Profile info
        profile_info = Container(className="space-y-4")
        profile_info.add(Text(f"Name: {self.shared_state['user_name']}", className="text-gray-700"))
        profile_info.add(Text("Email: john.doe@example.com", className="text-gray-700"))
        profile_info.add(Text("Role: Administrator", className="text-gray-700"))
        
        # Profile actions
        actions = Container(className="mt-6 space-y-2")
        actions.add(Button("Edit Profile", className="w-full px-4 py-2 bg-blue-500 text-white rounded"))
        actions.add(Button("Change Password", className="w-full px-4 py-2 bg-gray-200 rounded"))
        actions.add(Button("Logout", className="w-full px-4 py-2 bg-red-500 text-white rounded"))
        
        container.add(profile_info)
        container.add(actions)
        
        self.profile_window.add_child(container)
    
    def run(self):
        self.app.run()

# Usage
app = MultiWindowApp()
app.run()
```

### Window Events and Callbacks

```python
class WindowManager:
    def __init__(self):
        self.app = App()
        self.windows = {}
        self.setup_main_window()
    
    def setup_main_window(self):
        """Setup the main window with controls for other windows"""
        self.main_window = self.app.create_window(
            title="Window Manager",
            size=(600, 400)
        )
        
        container = Container(className="p-6")
        container.add(Text("Window Manager", className="text-2xl font-bold mb-6"))
        
        # Window controls
        controls = Container(className="space-y-3")
        
        # Create window buttons
        controls.add(Button(
            "Open Dialog", 
            className="w-full px-4 py-2 bg-blue-500 text-white rounded",
            onclick=self.open_dialog
        ))
        
        controls.add(Button(
            "Open Tool Window", 
            className="w-full px-4 py-2 bg-green-500 text-white rounded",
            onclick=self.open_tool_window
        ))
        
        controls.add(Button(
            "Open About", 
            className="w-full px-4 py-2 bg-purple-500 text-white rounded",
            onclick=self.open_about
        ))
        
        # Window status
        status = Container(className="mt-6 p-4 bg-gray-100 rounded")
        status.add(Text("Active Windows:", className="font-semibold mb-2"))
        
        self.status_list = Container(className="space-y-1")
        self.update_window_status()
        status.add(self.status_list)
        
        container.add(controls)
        container.add(status)
        
        self.main_window.add_child(container)
    
    def open_dialog(self):
        """Open a modal dialog window"""
        if 'dialog' not in self.windows:
            dialog = self.app.create_window(
                title="Dialog",
                size=(300, 200),
                position=(350, 250),
                resizable=False,
                on_top=True
            )
            
            content = Container(className="p-6 text-center")
            content.add(Text("This is a dialog window", className="text-lg font-semibold mb-4"))
            content.add(Button(
                "Close", 
                className="px-4 py-2 bg-red-500 text-white rounded",
                onclick=lambda: self.close_window('dialog')
            ))
            
            dialog.add_child(content)
            self.windows['dialog'] = dialog
            self.update_window_status()
    
    def open_tool_window(self):
        """Open a tool window"""
        if 'tools' not in self.windows:
            tools = self.app.create_window(
                title="Tools",
                size=(200, 400),
                position=(50, 100),
                maximizable=False
            )
            
            content = Container(className="p-4")
            content.add(Text("Tool Palette", className="text-lg font-bold mb-4"))
            
            tools_list = Container(className="space-y-2")
            tools_list.add(Button("Tool 1", className="w-full px-3 py-2 bg-gray-200 rounded text-sm"))
            tools_list.add(Button("Tool 2", className="w-full px-3 py-2 bg-gray-200 rounded text-sm"))
            tools_list.add(Button("Tool 3", className="w-full px-3 py-2 bg-gray-200 rounded text-sm"))
            
            content.add(tools_list)
            tools.add_child(content)
            
            self.windows['tools'] = tools
            self.update_window_status()
    
    def open_about(self):
        """Open an about window"""
        if 'about' not in self.windows:
            about = self.app.create_window(
                title="About",
                size=(350, 250),
                position=(300, 200),
                resizable=False,
                maximizable=False
            )
            
            content = Container(className="p-6 text-center")
            content.add(Text("OneForAll Application", className="text-xl font-bold mb-2"))
            content.add(Text("Version 0.1.0a2 (Alpha)", className="text-gray-600 mb-4"))
            content.add(Text("A Python GUI framework powered by pywebview", className="text-sm text-gray-500 mb-4"))
            
            content.add(Button(
                "Close", 
                className="px-4 py-2 bg-blue-500 text-white rounded",
                onclick=lambda: self.close_window('about')
            ))
            
            about.add_child(content)
            self.windows['about'] = about
            self.update_window_status()
    
    def close_window(self, window_name):
        """Close a specific window"""
        if window_name in self.windows:
            # In a real implementation, you would close the window here
            del self.windows[window_name]
            self.update_window_status()
    
    def update_window_status(self):
        """Update the window status display"""
        # Clear current status
        self.status_list.children.clear()
        
        # Add main window
        self.status_list.add(Text("• Main Window (active)", className="text-sm text-green-600"))
        
        # Add other windows
        for window_name in self.windows:
            self.status_list.add(Text(f"• {window_name.title()} Window", className="text-sm text-blue-600"))
        
        if not self.windows:
            self.status_list.add(Text("No additional windows open", className="text-sm text-gray-500"))
    
    def run(self):
        self.app.run()

# Usage
manager = WindowManager()
manager.run()
```

## Common Multi-Window Patterns

### Master-Detail Pattern

```python
class MasterDetailApp:
    def __init__(self):
        self.app = App()
        self.selected_item = None
        self.items = [
            {"id": 1, "name": "Document 1", "content": "Content of document 1..."},
            {"id": 2, "name": "Document 2", "content": "Content of document 2..."},
            {"id": 3, "name": "Document 3", "content": "Content of document 3..."}
        ]
        
        self.setup_windows()
    
    def setup_windows(self):
        # Master window (list)
        self.master_window = self.app.create_window(
            title="Document List",
            size=(300, 500),
            position=(100, 100)
        )
        
        # Detail window
        self.detail_window = self.app.create_window(
            title="Document Details",
            size=(600, 500),
            position=(450, 100)
        )
        
        self.build_master_window()
        self.build_detail_window()
    
    def build_master_window(self):
        """Build the master list window"""
        container = Container(className="p-4")
        container.add(Text("Documents", className="text-xl font-bold mb-4"))
        
        # Document list
        doc_list = Container(className="space-y-2")
        
        for item in self.items:
            doc_item = Container(className="p-3 border rounded hover:bg-gray-50 cursor-pointer")
            doc_item.add(Text(item["name"], className="font-medium"))
            doc_item.add(Text(f"ID: {item['id']}", className="text-sm text-gray-500"))
            
            # In a real implementation, you'd add click handlers here
            doc_list.add(doc_item)
        
        container.add(doc_list)
        self.master_window.add_child(container)
    
    def build_detail_window(self):
        """Build the detail view window"""
        container = Container(className="p-6")
        
        if self.selected_item:
            container.add(Text(self.selected_item["name"], className="text-2xl font-bold mb-4"))
            container.add(Text(self.selected_item["content"], className="text-gray-700"))
        else:
            container.add(Text("No document selected", className="text-gray-500 text-center mt-20"))
        
        self.detail_window.add_child(container)
    
    def run(self):
        self.app.run()
```

### Floating Tool Windows

```python
class IDEApp:
    def __init__(self):
        self.app = App()
        self.setup_ide_windows()
    
    def setup_ide_windows(self):
        # Main editor window
        self.editor_window = self.app.create_window(
            title="Code Editor",
            size=(800, 600),
            position=(200, 100)
        )
        
        # File explorer
        self.explorer_window = self.app.create_window(
            title="File Explorer",
            size=(250, 400),
            position=(50, 100),
            on_top=False
        )
        
        # Properties panel
        self.properties_window = self.app.create_window(
            title="Properties",
            size=(300, 300),
            position=(1050, 100),
            on_top=False
        )
        
        # Output console
        self.console_window = self.app.create_window(
            title="Console",
            size=(800, 200),
            position=(200, 750),
            on_top=False
        )
        
        self.build_editor_window()
        self.build_explorer_window()
        self.build_properties_window()
        self.build_console_window()
    
    def build_editor_window(self):
        """Build the main editor window"""
        container = Container(className="flex flex-col h-full")
        
        # Menu bar
        menu_bar = Container(className="bg-gray-100 border-b p-2 flex space-x-4")
        menu_bar.add(Button("File", className="px-3 py-1 hover:bg-gray-200 rounded"))
        menu_bar.add(Button("Edit", className="px-3 py-1 hover:bg-gray-200 rounded"))
        menu_bar.add(Button("View", className="px-3 py-1 hover:bg-gray-200 rounded"))
        menu_bar.add(Button("Run", className="px-3 py-1 hover:bg-gray-200 rounded"))
        
        # Editor area
        editor_area = Container(className="flex-1 p-4 bg-gray-900 text-green-400 font-mono")
        editor_area.add(Text("# Welcome to OneForAll IDE", className="mb-2"))
        editor_area.add(Text("from oneforall import App, Container, Text", className="mb-1"))
        editor_area.add(Text("", className="mb-1"))
        editor_area.add(Text("app = App()", className="mb-1"))
        editor_area.add(Text("window = app.create_window('My App', (800, 600))", className="mb-1"))
        
        # Status bar
        status_bar = Container(className="bg-gray-200 border-t p-2 flex justify-between text-sm")
        status_bar.add(Text("Ready", className="text-gray-600"))
        status_bar.add(Text("Line 1, Column 1", className="text-gray-600"))
        
        container.add(menu_bar)
        container.add(editor_area)
        container.add(status_bar)
        
        self.editor_window.add_child(container)
    
    def build_explorer_window(self):
        """Build the file explorer window"""
        container = Container(className="p-3")
        container.add(Text("Project Files", className="font-bold mb-3"))
        
        # File tree
        file_tree = Container(className="space-y-1 text-sm")
        file_tree.add(Text("📁 src/", className="font-medium"))
        file_tree.add(Text("  📄 main.py", className="ml-4 text-blue-600 cursor-pointer"))
        file_tree.add(Text("  📄 components.py", className="ml-4 text-blue-600 cursor-pointer"))
        file_tree.add(Text("📁 assets/", className="font-medium"))
        file_tree.add(Text("  🖼️ icon.png", className="ml-4 text-gray-600"))
        file_tree.add(Text("📄 README.md", className="text-blue-600 cursor-pointer"))
        
        container.add(file_tree)
        self.explorer_window.add_child(container)
    
    def build_properties_window(self):
        """Build the properties panel"""
        container = Container(className="p-3")
        container.add(Text("Properties", className="font-bold mb-3"))
        
        # Property list
        props = Container(className="space-y-2 text-sm")
        props.add(Container(className="flex justify-between"))
        props.children[-1].add(Text("Name:", className="font-medium"))
        props.children[-1].add(Text("main.py", className="text-gray-600"))
        
        props.add(Container(className="flex justify-between"))
        props.children[-1].add(Text("Size:", className="font-medium"))
        props.children[-1].add(Text("1.2 KB", className="text-gray-600"))
        
        props.add(Container(className="flex justify-between"))
        props.children[-1].add(Text("Type:", className="font-medium"))
        props.children[-1].add(Text("Python", className="text-gray-600"))
        
        container.add(props)
        self.properties_window.add_child(container)
    
    def build_console_window(self):
        """Build the console window"""
        container = Container(className="p-3 bg-black text-white font-mono text-sm")
        container.add(Text("Console Output", className="text-green-400 font-bold mb-2"))
        container.add(Text(">>> Starting OneForAll application...", className="mb-1"))
        container.add(Text(">>> Application initialized successfully", className="mb-1"))
        container.add(Text(">>> Ready for input", className="text-green-400"))
        
        self.console_window.add_child(container)
    
    def run(self):
        self.app.run()
```

## Window Management Best Practices

### Window Lifecycle Management

```python
class WindowLifecycleManager:
    def __init__(self):
        self.app = App()
        self.active_windows = {}
        self.window_configs = {}
    
    def create_managed_window(self, window_id, title, size, position=None, **kwargs):
        """Create a window with lifecycle management"""
        
        # Store window configuration
        self.window_configs[window_id] = {
            'title': title,
            'size': size,
            'position': position or (100, 100),
            'kwargs': kwargs
        }
        
        # Create the window
        window = self.app.create_window(
            title=title,
            size=size,
            position=position or (100, 100),
            **kwargs
        )
        
        self.active_windows[window_id] = window
        return window
    
    def close_window(self, window_id):
        """Close a managed window"""
        if window_id in self.active_windows:
            # In a real implementation, you would close the window here
            del self.active_windows[window_id]
    
    def is_window_open(self, window_id):
        """Check if a window is currently open"""
        return window_id in self.active_windows
    
    def get_window(self, window_id):
        """Get a window by ID"""
        return self.active_windows.get(window_id)
    
    def restore_window_layout(self, layout_config):
        """Restore windows from a saved layout"""
        for window_id, config in layout_config.items():
            if not self.is_window_open(window_id):
                self.create_managed_window(
                    window_id,
                    config['title'],
                    config['size'],
                    config['position'],
                    **config.get('kwargs', {})
                )
    
    def save_window_layout(self):
        """Save current window layout"""
        layout = {}
        for window_id, window in self.active_windows.items():
            if window_id in self.window_configs:
                layout[window_id] = self.window_configs[window_id].copy()
        return layout
```

### Memory Management

```python
class EfficientMultiWindowApp:
    def __init__(self):
        self.app = App()
        self.window_cache = {}
        self.lazy_windows = {}
    
    def get_or_create_window(self, window_id, factory_func):
        """Get existing window or create new one lazily"""
        
        if window_id not in self.window_cache:
            # Create window only when needed
            self.window_cache[window_id] = factory_func()
        
        return self.window_cache[window_id]
    
    def create_settings_window(self):
        """Factory function for settings window"""
        window = self.app.create_window(
            title="Settings",
            size=(400, 500)
        )
        
        # Build settings content
        container = Container(className="p-6")
        container.add(Text("Settings", className="text-xl font-bold"))
        window.add_child(container)
        
        return window
    
    def show_settings(self):
        """Show settings window (create if needed)"""
        settings_window = self.get_or_create_window(
            'settings',
            self.create_settings_window
        )
        # In a real implementation, you would show/focus the window here
    
    def cleanup_unused_windows(self):
        """Clean up windows that are no longer needed"""
        # Remove windows that haven't been accessed recently
        # This is a simplified example
        pass
```

## Advanced Multi-Window Features

### Window Docking Simulation

```python
class DockableWindowSystem:
    def __init__(self):
        self.app = App()
        self.docked_windows = {
            'left': None,
            'right': None,
            'bottom': None
        }
        self.main_window = None
        self.setup_dockable_system()
    
    def setup_dockable_system(self):
        """Setup a dockable window system"""
        
        # Main window
        self.main_window = self.app.create_window(
            title="Main Application",
            size=(1000, 700),
            position=(100, 100)
        )
        
        # Create docked panels
        self.create_left_panel()
        self.create_right_panel()
        self.create_bottom_panel()
        
        self.build_main_content()
    
    def create_left_panel(self):
        """Create left docked panel"""
        left_panel = self.app.create_window(
            title="Explorer",
            size=(250, 500),
            position=(100, 150),
            resizable=True,
            maximizable=False
        )
        
        content = Container(className="p-3")
        content.add(Text("File Explorer", className="font-bold mb-3"))
        content.add(Text("📁 Project Files", className="text-sm"))
        
        left_panel.add_child(content)
        self.docked_windows['left'] = left_panel
    
    def create_right_panel(self):
        """Create right docked panel"""
        right_panel = self.app.create_window(
            title="Properties",
            size=(250, 500),
            position=(850, 150),
            resizable=True,
            maximizable=False
        )
        
        content = Container(className="p-3")
        content.add(Text("Properties", className="font-bold mb-3"))
        content.add(Text("No selection", className="text-sm text-gray-500"))
        
        right_panel.add_child(content)
        self.docked_windows['right'] = right_panel
    
    def create_bottom_panel(self):
        """Create bottom docked panel"""
        bottom_panel = self.app.create_window(
            title="Console",
            size=(700, 150),
            position=(350, 650),
            resizable=True,
            maximizable=False
        )
        
        content = Container(className="p-3 bg-black text-white font-mono text-sm")
        content.add(Text("Console ready...", className="text-green-400"))
        
        bottom_panel.add_child(content)
        self.docked_windows['bottom'] = bottom_panel
    
    def build_main_content(self):
        """Build main window content"""
        container = Container(className="p-6")
        
        # Header
        header = Container(className="flex justify-between items-center mb-6")
        header.add(Text("Dockable Window System", className="text-2xl font-bold"))
        
        # Panel controls
        controls = Container(className="flex space-x-2")
        controls.add(Button("Toggle Left", className="px-3 py-1 bg-blue-500 text-white rounded text-sm"))
        controls.add(Button("Toggle Right", className="px-3 py-1 bg-green-500 text-white rounded text-sm"))
        controls.add(Button("Toggle Bottom", className="px-3 py-1 bg-purple-500 text-white rounded text-sm"))
        
        header.add(controls)
        
        # Main content area
        content_area = Container(className="bg-gray-50 p-6 rounded-lg min-h-96")
        content_area.add(Text("Main Content Area", className="text-lg font-semibold mb-4"))
        content_area.add(Text("This is the main workspace. Panels can be docked around it.", className="text-gray-600"))
        
        container.add(header)
        container.add(content_area)
        
        self.main_window.add_child(container)
    
    def run(self):
        self.app.run()
```

## Next Steps

Now that you understand multiple windows in OneForAll:

- [API Reference](../api/window) - Complete window API documentation
- [Advanced Patterns](../advanced/custom-components) - Advanced application patterns
- [Deployment](../deployment/building) - Building multi-window applications

---

Master multiple windows to create sophisticated desktop applications with OneForAll!