import asyncio
from typing import Optional, Any, TypeVar, Dict, List, Callable, Union

T = TypeVar("T")

class StateManager:
    def __init__(self) -> None:
        from .app import Window
        self._state: Dict[str, Any] = {}
        self._windows: List["Window"] = []

        self._pending_updates: Dict[str, Any] = {}
        self._flush_scheduled = False
        self._effects: List[Dict[str, Any]] = []

    # ---------- Window registration ----------
    def register_window(self, win: Any) -> None:
        from .app import Window
        if isinstance(win, Window):
            if win not in self._windows:
                self._windows.append(win)
                win.state = self

    # ---------- State ----------
    def use_state(self, key: str, default: T) -> T:
        if key not in self._state:
            self._state[key] = default

        return self._state[key] #type: ignore

    def set_state(self, key: str, value: T) -> None:
        self._pending_updates[key] = value

        if not self._flush_scheduled:
            self._flush_scheduled = True
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    loop.call_soon(self._flush_updates)
                else:
                    # If no loop running, flush immediately
                    self._flush_updates()
            except RuntimeError:
                # No event loop exists
                self._flush_updates()

    # ---------- Effect ----------
    def use_effect(self, keys: Union[str, List[str]], callback: Callable, run_on_mount: Optional[bool]=True) -> None:
        """
        Register a callback to run when any of the given keys change.
        `keys` can be a string or list of strings.
        """
        if isinstance(keys, str):
            keys = [keys]

        effect = {
            "keys": set(keys),
            "callback": callback,
            "last_values": {k: self._state.get(k) for k in keys},
            "cleanup": None,
        }
        self._effects.append(effect)
        if run_on_mount:
            self._run_effect(effect)

    # ---------- Flush updates ----------
    def flush(self) -> None:
        """
        Manually flush all pending updates immediately.
        Useful for tests or scripts where event loop is not running.
        """
        if self._flush_scheduled:
            self._flush_updates()

    def _flush_updates(self) -> None:
        # Apply all pending updates
        for key, value in self._pending_updates.items():
            self._state[key] = value

        # Refresh affected components
        affected_keys = set(self._pending_updates.keys())
        for win in self._windows:
            for c in win.get_all_components():
                if affected_keys.intersection(getattr(c, "depends_on", [])):
                    c.refresh()  # refresh only affected components

        # Run effects
        for effect in self._effects:
            # Check if any key actually changed value
            if affected_keys.intersection(effect["keys"]):
                self._run_effect(effect)

        # Clear pending updates
        self._pending_updates.clear()
        self._flush_scheduled = False

    # ---------- Run individual effect ----------
    def _run_effect(self, effect: Dict[str, Any]) -> None:
        # Check if any key changed
        changed = False
        for k in effect["keys"]:
            old = effect["last_values"].get(k)
            new = self._state.get(k)
            if old != new:
                changed = True
                effect["last_values"][k] = new

        # Run effect if mount or keys changed
        if changed or not hasattr(effect, "_mounted"):
            # Run cleanup first
            if effect["cleanup"]:
                try:
                    res = effect["cleanup"]()
                    if asyncio.iscoroutine(res):
                        asyncio.create_task(res)
                except Exception:
                    pass

            # Run effect callback
            try:
                result = effect["callback"]()
                if asyncio.iscoroutine(result):
                    try:
                        loop = asyncio.get_event_loop()
                        loop.create_task(result)
                    except RuntimeError:
                        asyncio.run(result)
                # Save cleanup if returned
                if callable(result):
                    effect["cleanup"] = result
                else:
                    effect["cleanup"] = None
            except Exception as e:
                print(f"Error in use_effect callback: {e}")

        # Mark as mounted
        effect["_mounted"] = True
