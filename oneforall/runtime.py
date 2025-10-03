class StateManager:
    def __init__(self):
        self._state = {}
        self._windows = []
        self._current_component = None

    def register_window(self, win):
        if win not in self._windows:
            self._windows.append(win)
            win.state = self

    def use_state(self, key, default=None):
        if key not in self._state:
            self._state[key] = default

        return self._state[key]

    def set_state(self, key, value):
        self._state[key] = value
        for win in self._windows:
            for c in win.get_all_components():
                if key in getattr(c, "depends_on", []):
                    c.refresh()  # only refresh affected components
