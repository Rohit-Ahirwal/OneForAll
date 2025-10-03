import html
import uuid
from typing import Callable, List, Optional

from oneforall.tailwind_merge import merge_classes


class Component:
    """Base class for all UI components"""

    def __init__(self, className: str = "", attrs: Optional[dict] = None):
        self.id = f"c_{uuid.uuid4().hex[:8]}"
        self.className = className
        self.attrs = attrs or {}
        self._window = None
        self.depends_on: List[str] = []
        self.children: List[Component] = []

    def add(self, child: "Component"):
        self.children.append(child)
        child._window = self._window
        return child

    def render(self) -> str:
        """Override in subclasses to render HTML"""
        raise NotImplementedError

    def refresh(self):
        """Update this component's HTML in webview"""
        if self._window and self._window._window:
            html_content = self.render()
            js = f'document.getElementById("{self.id}").outerHTML = `{html_content}`;'
            self._window._window.evaluate_js(js)


class Text(Component):
    def __init__(self, value: str, className: str = "", default_class: str = ""):
        super().__init__(className)
        self._value = value
        self.default_class = default_class

    @property
    def text(self):
        if (
            isinstance(self._value, str)
            and self._window
            and self._value in self._window.state._state
        ):
            if self._value not in self.depends_on:
                self.depends_on.append(self._value)
            return self._window.state._state[self._value]
        return self._value

    @text.setter
    def text(self, value):
        self._value = value
        if self._window:
            self.refresh()

    def render(self) -> str:
        return f"<div id='{self.id}' class='{merge_classes(self.default_class, self.className)}'>{html.escape(str(self.text))}</div>"


class Button(Component):
    def __init__(
        self,
        label: str,
        on_click: Optional[Callable] = None,
        className: str = "",
        default_class: str = "",
    ):
        super().__init__(className)
        self.default_class = default_class
        self.label = label
        self.on_click = on_click

    def render(self) -> str:
        return (
            f"<button id='{self.id}' class='{merge_classes(self.default_class, self.className)}' onclick=\"window.pywebview.api.call('{self.id}', {{}})\">"
            f"{html.escape(self.label)}</button>"
        )


class Container(Component):
    """Container to group other components"""

    def __init__(self, className: str = "", default_class: str = ""):
        super().__init__(className)
        self.children = []
        self.default_class = default_class

    def add(self, child: Component):
        self.children.append(child)

    def render(self) -> str:
        inner_html = "".join([child.render() for child in self.children])
        return f"<div id='{self.id}' class='{merge_classes(self.default_class, self.className)}'>{inner_html}</div>"
