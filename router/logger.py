import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

BASE_DIR = Path(__file__).parent


def setup_logger(name, level=logging.INFO):
    """
    Set up a logger with the specified name and logging level.

    Args:
        name (str): The name of the logger.
        level (int): The logging level (default is logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    log_file = BASE_DIR / "logs" / f"{name}.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    handler = TimedRotatingFileHandler(str(log_file), when="midnight", interval=5, backupCount=0, encoding="utf-8")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Custom format
    handler.setFormatter(formatter)  # Set the formatter for the handler

    logger = logging.getLogger(name)  # Create a logger with the specified name
    logger.setLevel(level)  # Set the logging level
    logger.addHandler(handler)  # Add the handler to the logger

    return logger
