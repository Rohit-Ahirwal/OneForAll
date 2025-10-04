import logging
import sys

RESET = "\033[0m"
COLOR_MAP = {
    "DEBUG": "\033[94m",    # Blue
    "INFO": "\033[92m",     # Green
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",    # Red
    "CRITICAL": "\033[95m", # Magenta
}

class ColoredFormatter(logging.Formatter):
    """Formatter that colors the entire log message based on level"""
    def format(self, record):
        color = COLOR_MAP.get(record.levelname, RESET)
        message = super().format(record)
        return f"{color}{message}{RESET}"

# Central logger for OneForAll
logger = logging.getLogger("OneForAll")
logger.setLevel(logging.DEBUG)  # default level

# Console handler
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

# Formatter
formatter = ColoredFormatter("[%(levelname)s] %(asctime)s - %(message)s", "%H:%M:%S")
ch.setFormatter(formatter)

# Add handler to logger
if not logger.handlers:
    logger.addHandler(ch)
