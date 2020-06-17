import logging
import logging.config
from os import path
import sys

log_file_path = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'conf/logger.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger()

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