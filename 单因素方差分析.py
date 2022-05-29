# -*- coding: utf-8 -*-
# @Time    : 2022/5/29 16:36
# @Author  : Ling_dy
# @FileName: 单因素方差分析.py.py
# @Software: PyCharm
import pandas as pd
def ONE_WAY_AVOVA(data):
    #计算各水平的样本平均值
    col_mean = data.mean()
    print('各水平的样本平均值')

    for index,value in col_mean.items():
        print(index,str(value))
    #计算所有样本平均值
    data_mean = col_mean.mean()
    print('所有 样本的平均值为' + str(data_mean))

    #计算样本数
    a = data.shape
    n = data.shape[0]
    m = data.shape[1]
    nm = data.shape[0]*data.shape[1]
    print('数据行列数为' + str(a))
    print('试验次数为' + str(n))
    print('因素水平个数为' + str(m))
    print('总样本数为' + str(nm))
    #计算总误差平方和、组间误差和组内误差平方和
    SST = ((data-data_mean)**2).sum().sum()
    SSA = ((col_mean-data_mean)**2*n).sum()
    SSE = ((data-col_mean)**2).sum().sum()
    print('总误差平方和SST为' + str(SST))
    print('组间误差平方和SSA为' + str(SSA))
    print('组内误差平方和为' + str(SSE))

    #计算统计量
    MSA = SSA/(m-1)
    MSE = SSE/(nm-m)
    F = MSA/MSE
    print('组间误差平方和MSA为' + str(MSA))
    print('组间均值平方和MSE为' + str(MSE))
    print('统计量F值为' + str(F))
data_city = pd.read_excel('销量统计.xlsx',index_col='月份')
print(data_city.head())
ONE_WAY_AVOVA(data_city)
