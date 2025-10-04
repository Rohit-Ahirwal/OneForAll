from typing import Callable, Dict, Any, Optional, Union

from .logger import logger


class OneForAllBridge:
    def __init__(self) -> None:
        self.callbacks: Dict[str, Callable] = {}

    def register(self, id: str, callback: Callable) -> None:
        self.callbacks[id] = callback
        logger.debug(f"Callback registered for id: {id}")

    def call(self, event_name: str, payload: Optional[Any] = None) -> Union[bool, str]:
        if event_name not in self.callbacks:
            logger.warning(f"No handler registered for event: {event_name}")
            return False

        callback = self.callbacks[event_name]
        try:
            logger.info(f"Event triggered: {event_name} with payload: {payload}")
            if payload is not None:
                callback(payload)
            else:
                callback()
            return True
        except TypeError:
            # fallback: try calling without any argument
            try:
                callback()
                return True
            except Exception as e:
                logger.error(f"Error calling callback {event_name}: {e}")
                return f"Error handling event {event_name}: {e}"
        except Exception as e:
            logger.error(f"Error handling event {event_name}: {e}")
            return f"Error handling event {event_name}: {e}"
