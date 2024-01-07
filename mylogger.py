import logging
import sys
from logging.handlers import TimedRotatingFileHandler

LOG_FORMAT = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
LOG_LEVEL = logging.DEBUG
LOG_PROPAGATE = False
LOGGER = None


def get_logger():
    def get_console_handler():
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(LOG_LEVEL)
        console_handler.setFormatter(log_formatter)
        return console_handler

    def get_file_handler():
        file_handler = logging.FileHandler('{0}.log'.format(logger_name))
        file_handler.setLevel(LOG_LEVEL)
        file_handler.setFormatter(log_formatter)
        return file_handler

    global LOGGER
    if LOGGER:
        return LOGGER

    logger_name = "apple_stock"
    LOGGER = logging.getLogger(logger_name)
    LOGGER.setLevel(LOG_LEVEL)
    log_formatter = logging.Formatter(LOG_FORMAT)
    LOGGER.addHandler(get_console_handler())
    LOGGER.addHandler(get_file_handler())
    # it's rarely necessary to propagate the error up to parent
    LOGGER.propagate = LOG_PROPAGATE

    return LOGGER
