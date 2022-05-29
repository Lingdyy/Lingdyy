# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 11:23
# @Author  : Ling_dy
# @FileName: 股票数据.py.py
# @Software: PyCharm

import tushare as ts
import pandas as pd
data = ts.get_hist_data('000061',start='2018-01-01',end='2019-01-01')#获取代码为000061的股票且时间为2018到2019的数据
print(data.head(10))#输出前十行数据
pd.set_option('display.max_columns',None)#解决Pycharm使用print()函数打印输出数据结果时可能不会显示所有列
#获取分钟级别的股票数据
data = ts.get_hist_data('000061',ktype='5')
data = ts.get_realtime_quotes('000061')#获取实时的股票数据
print(data)
data = ts.get_realtime_quotes(['000061','000002','000006'])
print(data)
data = ts.get_tick_data('000002',date='2018-12-12',src = 'tt')
print(data)
#获取大盘指数的实时行情信息
# data = ts.get_index() 此处出错，原因不明

