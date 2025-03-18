import logging
from pathlib import Path

def setup_logger(name, log_path):
    Path(log_path).parent.mkdir(exist_ok=True)
    logger = logging.getLogger(name)
    handler = logging.FileHandler(log_path)
    logger.addHandler(handler)
    return logger
