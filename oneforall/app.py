import webview

from oneforall.runtime import StateManager

from .bridge import OneForAllBridge
from .renderer import Renderer

class App:
    def __init__(self):
        self.windows = []
        self.bridge = OneForAllBridge()
        self.state = StateManager()

    def run(self, dev_mode=True, dev_tool=False):
        for win in self.windows:
            win.show(self.bridge, dev_mode)
            self.state.register_window(win)
        webview.start(debug=dev_tool)

    def use_state(self, key, default=None):
        return self.state.use_state(key, default)
    
    def set_state(self, key, value):
        return self.state.set_state(key, value)

    def refresh(self):
        for win in self.windows:
            win.refresh()

class Window:
    def __init__(self, title="One For All App", size=(800, 600)):
        self.title = title
        self.size = size
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def add_child(self, component):
        self._assign_window_recursive(component)
        self.children.append(component)

    def _assign_window_recursive(self, component):
        component._window = self
        if hasattr(component, "children"):
            for child in component.children:
                self._assign_window_recursive(child)

    def show(self, bridge, dev_mode=False):
        html = Renderer.render_app(self.title, self.children, dev_mode)
        self._window = webview.create_window(
            self.title,
            html=html,
            width=self.size[0],
            height=self.size[1],
            js_api=bridge
        )
        self.register_events(bridge, self.children)

    def register_events(self, bridge, children):
        for c in children:
            if hasattr(c, "on_click") and c.on_click:
                bridge.register(c.id, c.on_click)
            if hasattr(c, "children") and c.children:
                self.register_events(bridge, c.children)

    def refresh(self):
        # Re-render HTML
        html = Renderer.render_app(self.title, self.children, dev_mode=True)
        # Update webview window content
        self._window.load_html(html)

