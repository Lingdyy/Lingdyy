# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 18:35
# @Author  : Ling_dy
# @FileName: 双因素方差分析.py
# @Software: PyCharm

import pandas as pd
data = pd.read_excel('销售量.xlsx',index_col='月份')
col_mean = data.mean()
print('各水平平均值为:')
for key,value in col_mean.items():
    print(key,value)
row_data = data.T
row_mean = row_data.mean()
for key,value in row_data.items():
    print(key,value)
print('总平均值为:')
data_mean = col_mean.mean()
print(data_mean)
a = data.shape
n = data.shape[0]
m = data.shape[1]
nm = data.shape[0]*data.shape[1]
print('行列数为:' + str(a))
print('试验次数为:' + str(n))
print('因素个数为:' + str(m))
SST = ((data-data_mean)**2).sum().sum()
SSR = ((data-col_mean)**2*n).sum()
SSC = ((data-row_mean)**2*m).sum()
SSE = SST - SSR -SSC
print('总误差平方和SST为' + str(SST))
print('行因素的误差平方和SSR为' + str(SSR))
print('列因素的误差平方和SSC为 ' + str(SSC))
print('随机误差平方和SSE为' + str(SSE))
MSC = SSC/(m-1)
MSR = SSR/(n-1)
MSE = SSE/((n-1)*(m-1))
FR = MSR/MSE
FC = MSC/MSE
print('行因素的均方为' + str(MSR))
print('列因素的均方为' + str(MSC))
print('随机误差项的均方为' + str(MSE))
print('行因素的统计量FR为' + str(FR))
print('列因素的统计量FC为' + str(FC))



