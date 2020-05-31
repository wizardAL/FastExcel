# 
# 数据字典
#

# 标题映射
title_dict = {
  "交易日": "时间",
  "交易日期": "时间",
  "交易时间": "时间",
  "发生时间": "时间",
  "入账时间": "时间",
  "贷方金额": "收入",
  "汇入金额": "收入",
  "收入(贷)": "收入",
  "收入金额（+元）": "收入",
  "收入（+元）": "收入",
  "借方金额": "支出",
  "汇出金额": "支出",
  "支出金额（-元）": "支出",
  "支出(借)": "支出",
  "支出（-元）": "支出",
  "收/付方名称": "对方名称",
  "对方户名": "对方名称",
  "交易对手名称": "对方名称",
  "收/付方帐号": "交易账号", 
  "对方账号": "交易账号",
  "交易对手账号": "交易账号",
  "流水号": "交易流水号",
  #"对方账号": "交易流水号",
  "业务类型": "摘要",
  "费用类别": "费用类型",
  "二级费用": "二级类型"
}

# 行首映射，用于判断是否是首行
headfirst_dic = {
  "序号": True,
  "交易日": True,
  "流水号": True,
  "账务流水号": True,
  "交易日期": True,
  "交易时间": True
}

trans_dic = {
  "流水号": "流水号",
  "交易日": "交易时间",
  "交易日期": "交易时间",
  "交易时间": None,
  "收/付方名称": "对方名称",
  "对方户名": "对方名称",
  "汇入金额": "金额",
  "贷方金额": "金额"
}

# 判断是否在标题映射中，没有返回title
def get_title_dic(title):
  return title_dict.get(title, title)


# 判断是否是首行
def is_head_first(title):
  return headfirst_dic.get(title) == True

# 
def get_trans_dic(title):
  return trans_dic.get(title)