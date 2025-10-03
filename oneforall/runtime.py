import asyncio


class StateManager:
    def __init__(self):
        self._state = {}
        self._windows = []
        self._current_component = None

        self._pending_updates = {}
        self._flush_scheduled = False

    def register_window(self, win):
        if win not in self._windows:
            self._windows.append(win)
            win.state = self

    def use_state(self, key, default=None):
        if key not in self._state:
            self._state[key] = default

        return self._state[key]

    def set_state(self, key, value):
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

    def flush(self):
        """
        Manually flush all pending updates immediately.
        Useful for tests or scripts where event loop is not running.
        """
        if self._flush_scheduled:
            self._flush_updates()

    def _flush_updates(self):
        # Apply all pending updates
        for key, value in self._pending_updates.items():
            self._state[key] = value

        # Refresh affected components
        affected_keys = set(self._pending_updates.keys())
        for win in self._windows:
            for c in win.get_all_components():
                if affected_keys.intersection(getattr(c, "depends_on", [])):
                    c.refresh()  # refresh only affected components

        # Clear pending updates
        self._pending_updates.clear()
        self._flush_scheduled = False
