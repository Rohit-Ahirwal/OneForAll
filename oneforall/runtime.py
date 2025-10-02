class StateManager:
    def __init__(self):
        self._state = {}
        self._windows = []

    def register_window(self, win):
        if win not in self._windows:
            self._windows.append(win)

    def use_state(self, key, default=None):
        if key not in self._state:
            self._state[key] = default
        return self._state[key]

    def set_state(self, key, value):
        self._state[key] = value
        for win in self._windows:
            win.refresh()
