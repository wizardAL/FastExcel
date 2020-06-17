#-*- coding:utf-8 -*-
FUNC = '@func:'

def exec_rule(value, param):
  '''
  是否是规则
  '''
  expre = get_expre(value)
  for (k, v) in param.items():
    expre = expre.replace('$(' + k + ')', v)
  return eval(expre)

def is_rule(value):
  '''
  是否是规则
  '''
  return str(value).startswith(FUNC)

def get_expre(value):
  return value.replace(FUNC, '')
