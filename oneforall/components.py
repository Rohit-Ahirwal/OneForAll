import html
import uuid
from typing import Any, Callable, List, Optional, Tuple, Union

from oneforall.image_resolver import embed_image
from oneforall.tailwind_merge import merge_classes
from oneforall.vnode import VNode

# Define patch types
Patch = Union[
    Tuple[str, VNode],
    Tuple[str, Any, Any],  # e.g., ("update-text", value, id)
]


class Component:
    """Base class for all UI components"""

    def __init__(
            self,
            className: str = "",
            depends_on: Union[List[str], None] = None,
            attrs: Optional[dict] = None,
    ) -> None:
        from .app import Window

        self.id: str = f"c_{uuid.uuid4().hex[:8]}"
        self.className: str = className
        self.attrs: dict = attrs or {}
        self._window: Optional[Window] = None
        self.depends_on: List[str] = [] if depends_on is None else depends_on
        self.children: List["Component"] = []
        self._vnode: Optional[VNode] = None  # Initialized after first render

    def add(self, child: "Component") -> "Component":
        self.children.append(child)
        child._window = self._window
        return child

    def remove(self, child: "Component") -> "Component":
        self.children.remove(child)

    def clear(self) -> None:
        self.children = []

    def render(self, refreshing: bool = False) -> VNode:
        """Override in subclasses"""
        raise NotImplementedError

    def refresh(self) -> None:
        """Update this component's HTML in webview"""
        if not self._window:
            return
        new_node = self.render(refreshing=True)
        if self._vnode is None:
            # First render
            self._vnode = new_node
            return
        patches = self.diff(self._vnode, new_node)
        self.apply_patches(patches)
        self._vnode = new_node

    def diff(
            self,
            old_node: Optional[Union[str, VNode]],
            new_node: Optional[Union[str, VNode]],
            parent_id: Optional[str] = None,
    ) -> List[Patch]:
        patches: List[Patch] = []

        # Text node handling
        if isinstance(old_node, str) or isinstance(new_node, str):
            old_text = str(old_node or "")
            new_text = str(new_node or "")
            if old_text != new_text:
                patches.append(("update-text", new_text, parent_id))
            return patches

        # Insert/remove cases
        if old_node is None and new_node is not None:
            patches.append(("insert", new_node, parent_id))
            return patches
        if new_node is None and old_node is not None:
            patches.append(("remove", old_node, parent_id))
            return patches

        if old_node is None or new_node is None:
            return patches  # both None, nothing to do

        # Both VNodes
        if old_node.tag != new_node.tag:
            patches.append(("replace", new_node, parent_id))
            return patches

        # Prop diff
        if old_node.props != new_node.props:
            node_id = new_node.props.get("id", parent_id)
            patches.append(("update-props", new_node, node_id))

        # Diff children recursively
        max_len = max(len(old_node.children), len(new_node.children))
        for i in range(max_len):
            old_child = old_node.children[i] if i < len(old_node.children) else None
            new_child = new_node.children[i] if i < len(new_node.children) else None
            # Pass down parent id properly
            child_parent_id = new_node.props.get("id", parent_id)
            patches.extend(self.diff(old_child, new_child, child_parent_id))

        return patches

    def apply_patches(self, patches: List[Patch]) -> None:
        if (
                not patches
                or not self._window
                or not getattr(self._window, "_window", None)
        ):
            return

        # Separate patches by type for safe order
        safe_patches = []
        destructive_patches = []

        for patch in patches:
            action, *rest = patch
            if action in ("remove", "replace", "insert"):
                destructive_patches.append(patch)
            else:
                safe_patches.append(patch)

        ordered_patches = safe_patches + destructive_patches

        js_commands: List[str] = []
        for patch in ordered_patches:
            action, node, *rest = patch

            node_id: str = (
                rest[0]
                if rest
                else getattr(getattr(node, "props", {}), "get", lambda k, d=None: d)("id", self.id)
            )

            if not node_id:
                continue  # Skip patches with no target ID

            # Defensive: ensure element exists before changing
            js_check = f"var el = document.getElementById('{node_id}'); if (!el) {{ console.warn('Missing element {node_id}'); }} else {{ "

            if action == "insert":
                parent_id = rest[0] if rest else None
                if parent_id:
                    js_commands.append(
                        f'document.getElementById("{parent_id}").insertAdjacentHTML("beforeend", `{node.to_html()}`);'
                    )

            elif action == "replace":
                js_commands.append(
                    js_check + f'el.outerHTML = `{node.to_html()}`; }}'
                )

            elif action == "update-props":
                for k, v in node.props.items():
                    js_commands.append(
                        js_check + f'el.setAttribute("{k}", "{v}"); }}'
                    )

            elif action == "update-text":
                js_commands.append(
                    js_check + f'el.innerText = `{node}`; }}'
                )

            elif action == "remove":
                js_commands.append(
                    js_check + f'el.remove(); }}'
                )

        if not js_commands:
            return

        webview_window = getattr(self._window, "_window", None)
        if webview_window is None:
            return

        # Apply all patches safely
        webview_window.evaluate_js("\n".join(js_commands))


class Container(Component):
    """Container to group other components"""

    def __init__(
            self,
            className: str = "",
            depends_on: Union[List[str], None] = None,
            default_class: str = "",
    ) -> None:
        super().__init__(className, depends_on)
        self.default_class: str = default_class

    def add(self, child: Component) -> Component:
        self.children.append(child)
        child._window = self._window
        return child

    def render(self, refreshing: bool = False) -> VNode:
        children_vnodes: List[Union[VNode, str]] = [
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


class Text(Component):
    def __init__(
            self,
            value: Union[str, Callable],
            tag: str,
            className: str = "",
            depends_on: Union[List[str], None] = None,
            default_class: str = "",
    ) -> None:
        super().__init__(className, depends_on)
        self._value: Union[str, Callable] = value
        self._tag: str = tag
        self.default_class: str = default_class

    @property
    def text(self) -> Any:
        window = self._window
        if callable(self._value):
            return str(self._value())
        elif self.depends_on is not None and len(self.depends_on) > 0 and window:
            state_dict = getattr(window.state, "_state", {})
            return state_dict[self.depends_on[0]]
        elif isinstance(self._value, str) and window and getattr(window, "state", None):
            state_dict = getattr(window.state, "_state", {})
            if self._value in state_dict:
                if self._value not in self.depends_on:
                    self.depends_on.append(self._value)
                return state_dict[self._value]
        return self._value

    @text.setter
    def text(self, value: Any) -> None:
        self._value = value
        if self._window:
            self.refresh()

    def render(self, refreshing: bool = False) -> VNode:
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


class Image(Component):
    def __init__(
            self,
            src: str,
            alt: str,
            className: str = "",
            depends_on: Union[List[str], None] = None,
            default_class: str = "",
    ) -> None:
        super().__init__(className, depends_on)
        self.src: str = src
        self.alt: str = alt
        self.default_class: str = default_class

    def render(self, refreshing: bool = False) -> VNode:
        src = embed_image(self.src)
        vnode = VNode(
            tag="img",
            props={
                "id": self.id,
                "src": src,
                "alt": self.alt,
                "class": merge_classes(self.default_class, self.className),
            },
        )
        if not refreshing:
            self._vnode = vnode
        return vnode


class Button(Component):
    def __init__(
            self,
            label: str,
            on_click: Optional[Callable[[], None]] = None,
            className: str = "",
            depends_on: Union[List[str], None] = None,
            default_class: str = "",
    ) -> None:
        super().__init__(className, depends_on)
        self.label: str = label
        self.on_click: Optional[Callable[[], None]] = on_click
        self.default_class: str = default_class

    def render(self, refreshing: bool = False) -> VNode:
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
