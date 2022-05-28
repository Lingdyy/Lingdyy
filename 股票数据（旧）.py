# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 14:32
# @Author  : Ling_dy
# @FileName: 旧版本.py
# @Software: PyCharm
#From python书籍例子
import pandas as pd
tianye = ts.get_k_data(code= '600807',start='1994-01-01')
print(tianye)
tianye.to_csv('tianye.csv')
Tianye  = pd.read_csv('tianye.csv',index_col='date',parse_dates=['date'])
print(Tianye)
Tianye = Tianye['2010':'2019'] #使用行标签做切片获取2010-2019年的数据
month_first = Tianye.resample('M').first() #获取每月第一天的股票数据
month_first_money = month_first['open'].sum()*1000 #计算每月第一天开盘价卖出的总价
month_max = Tianye.resample('M').last() #获取每月最后一天的股价票据
month_max_money = month_max['close'].sum()*1000 #计算每月最后一天以收盘价卖出的总价
get_money = month_max_money - month_first_money #计算10年的收益
print(get_money)
