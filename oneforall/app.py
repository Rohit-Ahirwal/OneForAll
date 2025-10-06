from typing import Any, Callable, List, Optional, Tuple, TypeVar

import webview

from oneforall.runtime import StateManager

from .bridge import OneForAllBridge
from .components import Component
from .renderer import Renderer

T = TypeVar("T")


class App:
    def __init__(self) -> None:
        self.windows: List[Window] = []
        self.bridge = OneForAllBridge()
        self.state = StateManager()

    def append(self, window: "Window") -> None:
        self.windows.append(window)
        self.state.register_window(window)

    def run(self, dev_mode: bool = True, dev_tool: bool = False) -> None:
        for win in self.windows:
            win.show(dev_mode)
        webview.start(debug=dev_tool)

    def use_state(self, key: str, default: Optional[T] = None) -> Optional[T]:
        return self.state.use_state(key, default)

    def set_state(self, key: str, value: T) -> None:
        self.state.set_state(key, value)

    def use_effect(self, key: str, callback: Callable) -> None:
        self.state.use_effect(key, callback)

    def refresh(self) -> None:
        for win in self.windows:
            win.refresh()


class Window:
    def __init__(
        self, title: str = "One For All App", size: Tuple[int, int] = (800, 600)
    ) -> None:
        self._window: Optional[webview.window.Window] = None
        self.title: str = title
        self.size: Tuple[int, int] = size
        self.state: Optional[StateManager] = None
        self.bridge = OneForAllBridge()
        self.children: List[Component] = []

    def __enter__(self) -> "Window":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass

    def add_child(self, component: Component) -> None:
        self._assign_window_recursive(component)
        self.children.append(component)

    def _assign_window_recursive(self, component: Component) -> None:
        component._window = self
        if hasattr(component, "children"):
            for child in component.children:
                self._assign_window_recursive(child)

    def show(self, dev_mode: bool = False) -> None:
        html = Renderer.render_app(self.title, self.children, dev_mode)
        self._window = webview.create_window(
            self.title,
            html=html,
            width=self.size[0],
            height=self.size[1],
            js_api=self.bridge,
        )
        self.register_events(self.children)

    def register_events(self, children: List[Component]) -> None:
        for c in children:
            if hasattr(c, "on_click") and c.on_click:
                self.bridge.register(c.id, c.on_click)
            if hasattr(c, "children") and c.children:
                self.register_events(c.children)

    def get_all_components(self) -> List[Component]:
        """Flatten all components for dependency checking"""
        all_comps: List[Component] = []

        def recurse(c_list: List[Component]) -> None:
            for c in c_list:
                all_comps.append(c)
                if hasattr(c, "children"):
                    recurse(c.children)

        recurse(self.children)
        return all_comps

    def refresh(self) -> None:
        window = self._window
        # Re-render HTML
        html = Renderer.render_app(self.title, self.children, dev_mode=True)
        # Update webview window content
        if window is not None:
            window.load_html(html)
        self.register_events(self.children)
