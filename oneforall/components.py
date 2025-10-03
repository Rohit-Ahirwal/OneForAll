import html
import uuid
from typing import Callable, List, Optional, Union

from oneforall.tailwind_merge import merge_classes
from oneforall.vnode import VNode


class Component:
    """Base class for all UI components"""

    def __init__(self, className: str = "", attrs: Optional[dict] = None):
        self._vnode: Optional[VNode] = None
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

    def render(self, refreshing=False) -> VNode:
        """Override in subclasses to render HTML"""
        raise NotImplementedError

    def refresh(self):
        """Update this component's HTML in webview"""
        if not self._window or not self._window._window:
            return
        new_node = self.render(refreshing=True)
        patches = self.diff(self._vnode, new_node)
        self.apply_patches(patches)
        self._vnode = new_node

    def diff(self, old_node, new_node):
        patches = []

        # Text node handling
        if isinstance(old_node, str) or isinstance(new_node, str):
            old_text = str(old_node) if old_node is not None else ""
            new_text = str(new_node) if new_node is not None else ""
            if old_text != new_text:
                patches.append(("update-text", new_text, getattr(self, "id", "root")))
            return patches

        if old_node is None:
            patches.append(("insert", new_node))
        elif new_node is None:
            patches.append(("remove", old_node))
        elif old_node.tag != new_node.tag:
            patches.append(("replace", new_node))
        else:
            if old_node.props != new_node.props:
                patches.append(("update-props", new_node))
            for i in range(max(len(old_node.children), len(new_node.children))):
                old_child = old_node.children[i] if i < len(old_node.children) else None
                new_child = new_node.children[i] if i < len(new_node.children) else None
                patches.extend(self.diff(old_child, new_child))

        return patches

    def apply_patches(self, patches):
        if not patches or not self._window or not self._window._window:
            return

        js_commands = []
        for action, node, *rest in patches:
            node_id = rest[0] if rest else getattr(node, "props", {}).get("id", self.id)
            if action in ["replace", "insert"]:
                js_commands.append(
                    f'document.getElementById("{node_id}").outerHTML = `{node.to_html()}`;'
                )
            elif action == "update-props":
                for k, v in node.props.items():
                    js_commands.append(
                        f'document.getElementById("{node_id}").setAttribute("{k}", "{v}");'
                    )
            elif action == "update-text":
                js_commands.append(
                    f'document.getElementById("{node_id}").innerText = `{node}`;'
                )
            elif action == "remove":
                js_commands.append(f'document.getElementById("{node_id}").remove();')

        self._window._window.evaluate_js("\n".join(js_commands))


class Container(Component):
    """Container to group other components"""

    def __init__(self, className: str = "", default_class: str = ""):
        super().__init__(className)
        self.children = []
        self.default_class = default_class

    def add(self, child: Component):
        self.children.append(child)

    def render(self, refreshing=False) -> VNode:
        children_vnodes: list[Union[VNode, str]] = [
            child.render() for child in self.children
        ]
        vnode = VNode(
            tag="div",
            props={
                "id": self.id,
                "class": merge_classes(self.default_class, self.className),
            },
            children=children_vnodes,
        )
        if not refreshing:
            self._vnode = vnode
            return vnode
        else:
            return vnode


class Text(Component):
    def __init__(
        self, value: str, tag: str, className: str = "", default_class: str = ""
    ):
        super().__init__(className)
        self._value = value
        self._tag = tag
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

    def render(self, refreshing=False) -> VNode:
        vnode = VNode(
            tag=self._tag,
            props={
                "id": self.id,
                "class": merge_classes(self.default_class, self.className),
            },
            children=[html.escape(str(self.text))],
        )
        if not refreshing:
            self._vnode = vnode
            return vnode
        else:
            return vnode


class Image(Component):
    def __init__(
        self, src: str, alt: str, className: str = "", default_class: str = ""
    ):
        super().__init__(className)
        self.src = src
        self.alt = alt
        self.default_class = default_class

    def render(self, refreshing=False) -> VNode:
        vnode = VNode(
            tag="img",
            props={
                "id": self.id,
                "src": self.src,
                "alt": self.alt,
                "class": merge_classes(self.default_class, self.className),
            },
        )
        if not refreshing:
            self._vnode = vnode
            return vnode
        else:
            return vnode


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

    def render(self, refreshing=False) -> VNode:
        vnode = VNode(
            tag="button",
            props={
                "id": self.id,
                "class": merge_classes(self.default_class, self.className),
                "onclick": f"window.pywebview.api.call('{self.id}', {{}})",
            },
            children=[html.escape(self.label)],
        )
        if not refreshing:
            self._vnode = vnode
            return vnode
        else:
            return vnode
