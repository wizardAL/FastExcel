import openpyxl
import os
import lib.util as util

# 打开文件
def open_file(path):
  return openpyxl.load_workbook(path)


# sheet读取
def read_rows(sheet):
  return tuple(sheet.rows)


# 获取所有单元格的标题
def get_titles(sheet):
  list = []
  for i, row in enumerate(tuple(sheet.rows)):
    if i != 0: return list
    for cell in row:
      if cell.value == None: continue
      list.append(cell.value)
  return list


# 获取指定后缀的文件列表
def get_filelist(dir, suffix):
  list = []
  for home, dirs, files in os.walk(dir):
    files = [f for f in files if not f[0] == '~']
    dirs[:] = [d for d in dirs if d not in ['input','build','dist']] # 忽略当前目录下的子目录
    for filename in files:
      if filename.endswith(suffix):
        list.append(filename)
  return list


# 获取指定单元格的标题
def get_title(sheet, cell, _row):
  return sheet.cell(row=_row, column=cell.column).value


# 写入cell
def append(sheet, col, row, val):
  sheet.cell(column=col, row=row, value= val)


# 获取cell值
def get_value(title, cell):
  value = abs(cell.value) if util.is_negative(cell.value) else cell.value
  
  if value == None or value == '':
    return ""
  elif title == "时间":  
    return util.date_format(value) # 格式化时间
  elif (title == "收入" or title == "支出") and (isinstance(value, str)): 
    return float(value.replace(',', ''))  # 格式化金额
  else:
    return value