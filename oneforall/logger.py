import logging
import sys

# Central logger for OneForAll
logger = logging.getLogger("OneForAll")
logger.setLevel(logging.DEBUG)  # default level

# Console handler
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s", "%H:%M:%S")
ch.setFormatter(formatter)

# Add handler to logger
if not logger.handlers:
    logger.addHandler(ch)
