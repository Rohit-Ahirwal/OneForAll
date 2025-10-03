from typing import List

import webview

from oneforall.runtime import StateManager

from .bridge import OneForAllBridge
from .components import Component
from .renderer import Renderer


class App:
    def __init__(self):
        self.windows = []
        self.bridge = OneForAllBridge()
        self.state = StateManager()

    def append(self, window):
        self.windows.append(window)
        self.state.register_window(window)

    def run(self, dev_mode=True, dev_tool=False):
        for win in self.windows:
            win.show(dev_mode)
        webview.start(debug=dev_tool)

    def use_state(self, key, default=None):
        return self.state.use_state(key, default)

    def set_state(self, key, value):
        self.state.set_state(key, value)

    def refresh(self):
        for win in self.windows:
            win.refresh()


class Window:
    def __init__(self, title="One For All App", size=(800, 600)):
        self._window = None
        self.title = title
        self.size = size
        self.state = None
        self.bridge = OneForAllBridge()
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

    def show(self, dev_mode=False):
        html = Renderer.render_app(self.title, self.children, dev_mode)
        self._window = webview.create_window(
            self.title,
            html=html,
            width=self.size[0],
            height=self.size[1],
            js_api=self.bridge,
        )
        self.register_events(self.children)

    def register_events(self, children):
        for c in children:
            if hasattr(c, "on_click") and c.on_click:
                self.bridge.register(c.id, c.on_click)
            if hasattr(c, "children") and c.children:
                self.register_events(c.children)

    def get_all_components(self) -> List[Component]:
        """Flatten all components for dependency checking"""
        all_comps = []

        def recurse(c_list):
            for c in c_list:
                all_comps.append(c)
                if hasattr(c, "children"):
                    recurse(c.children)

        recurse(self.children)
        return all_comps

    def refresh(self):
        # Re-render HTML
        html = Renderer.render_app(self.title, self.children, dev_mode=True)
        # Update webview window content
        self._window.load_html(html)
        self.register_events(self.children)
