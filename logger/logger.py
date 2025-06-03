import logging
import os.path
import sys
from logging.handlers import RotatingFileHandler

from logger.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler1 = RotatingFileHandler(LoggerConfig.LOGS_FILE_NAME, maxBytes=LoggerConfig.MAX_BYTES,
                                     backupCount=LoggerConfig.BACKUP_COUNT)
    __handler2 = logging.StreamHandler(sys.stdout)
    __formatter = logging.Formatter(LoggerConfig.FORMAT)
    __handler1.setFormatter(__formatter)
    __handler2.setFormatter(__formatter)
    __logger.addHandler(__handler1)
    __logger.addHandler(__handler2)

    @staticmethod
    def info(message: str):
        Logger.__logger.info(msg=message)

    @staticmethod
    def error(message: str):
        Logger.__logger.error(msg=message)
