#
# 工具类
#
import time

# 判断是否是负数
def is_negative(str):
  try:
    return (isinstance(int(str), int) or isinstance(float(str), float)) and (str < 0)
  except ValueError:
    return False
  except TypeError:
    return False

# 时间格式化
def formart(str):
  print(str)
  try:
    return time.strftime('%Y-%m-%d', time.strptime(str, '%Y-%m-%d %H:%M:%S.%f'))
  except ValueError:
    return str

print(formart("2020-05-01 00:01:42"))    