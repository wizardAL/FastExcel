# -*- coding:utf-8 -*-
import logging
import logging.config
from os import path
import sys

CONFIG = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simpleFormatter'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'log.txt',
            'mode': "w",
            'encoding': 'utf8',
            'formatter': 'simpleFormatter'
        }
    },
    'formatters': {
        'simpleFormatter': {
            'format': '[%(levelname)s] %(asctime)s - %(message)s'
        }
    },
    'loggers': {
        'root': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],
        },
        'console': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'qualname': 'simple',
            'propagate': 0
        }
    }
}

logging.config.dictConfig(CONFIG)
logger = logging.getLogger('root')


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)


def waring(msg):
    logger.waring(msg)


def error(msg):
    logger.error(msg)


def exception(e):
    logger.exception(e)
