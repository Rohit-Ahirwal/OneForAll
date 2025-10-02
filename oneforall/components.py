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
        self.children: List[Component] = []

    def add(self, child: "Component"):
        self.children.append(child)
        return child

    def render(self) -> str:
        """Override in subclasses to render HTML"""
        raise NotImplementedError


class Text(Component):
    def __init__(self, value: str, className: str = "", default_class: str = ""):
        super().__init__(className)
        self._value = value
        self.default_class = default_class
        self._window = None

    @property
    def text(self):
        return self._value

    @text.setter
    def text(self, value):
        self._value = value
        if self._window:
            self._window.refresh()

    def render(self) -> str:
        return f"<div id='{self.id}' class='{merge_classes(self.default_class, self.className)}'>{html.escape(self.text)}</div>"


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
