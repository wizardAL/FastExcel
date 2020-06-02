#
# 工具类
#
import time
import re

DATE_FORMAT = '%Y-%m-%d'


def is_negative(str):
  '''
  判断是否是负数
  '''
  try:
    return (isinstance(int(str), int) or isinstance(float(str), float)) and (str < 0)
  except ValueError:
    return False
  except TypeError:
    return False


def date_format(_str):
  '''
  # 日期格式化
  '''
  try:
    _str = str(_str)
    # YYYY/MM/DD
    if re.match(r'^\d{4}\/\d{2}\/\d{2}$', _str):
      return time.strftime(DATE_FORMAT, time.strptime(_str, '%Y/%M/%d'))
    # YYYYMMDD
    if re.match(r'^[1|2]\d{3}[0-2]\d{1}[0-6]\d{1}$', _str):
      return time.strftime(DATE_FORMAT, time.strptime(_str, '%Y%m%d'))
    # YYYY/mm/dd hh:mm:ss
    elif re.match(r'^\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}$', _str):
      return time.strftime(DATE_FORMAT, time.strptime(_str, '%Y/%m/%d %H:%M:%S'))
    # YYYY-mm-dd hh:mm:ss
    elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', _str):
      return time.strftime(DATE_FORMAT, time.strptime(_str, '%Y-%m-%d %H:%M:%S'))
    # YYYY/mm/dd hh:mm:ss.ffff
    elif re.match(r'^\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}.\d{4}', _str):
      return time.strftime(DATE_FORMAT, time.strptime(_str, '%Y/%m/%d %H:%M:%S.%f'))
    # YYYY-mm-dd hh:mm:ss.ffff
    elif re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{4}', _str):
      return time.strftime(DATE_FORMAT, time.strptime(_str, '%Y-%m-%d %H:%M:%S.%f'))
    else:
      return _str
  except ValueError:
    return _str


def now_format(): 
  return time.strftime('%Y%m%d-%H%M')
