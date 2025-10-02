from .logger import logger

class OneForAllBridge():
    def __init__(self):
        self.callbacks = {}

    def register(self, id, callback):
        self.callbacks[id] = callback
        logger.debug(f"Callback registered for id: {id}")
    
    def call(self, event_name: str, payload=None):
        if event_name in self.callbacks:
            try:
                logger.info(f"Event triggered: {event_name} with payload: {payload}")
                callback = self.callbacks[event_name]

                # Always call callback safely
                callback_args = [payload] if payload is not None else []
                callback(*callback_args)
                return True
            except TypeError:
                # fallback: try calling without any argument
                callback()
                return True
            except Exception as e:
                logger.error(f"Error handling event {event_name}: {e}")
                return f"Error handling event {event_name}: {e}"
        else:
            logger.warning(f"No handler registered for event: {event_name}")
            return False
