# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 14:32
# @Author  : Ling_dy
# @FileName: 数据运算.py.py
# @Software: PyCharm
#数据的统计运算
import pandas as pd
data = pd.read_excel('数据.xlsx')
a = data.sum()
print(a)
#指定列求和
b = data['利润'].sum()
print(b)
#求平均值，mean()对所有数值数据进行平均值计算
c = data.mean()
print(c)
d = data['利润'].mean()#指定列进行平均值求和
print(d)
e = data.max()#计算最大值
print(e)
f = data['利润'].max()#指定值进行求最大值
print(f)
#求数值分布状况，用describe()
a = data.describe()
print(a)
#会有count,mean,std,min,25%,50%,75%，max的数据描述

#计算相关系数
import pandas as pd
data = pd.DataFrame('相关性分析.xlsx')
print(data)
a = data.corr()#计算各列之间的相关系数
print(a)
#只看某一列与其他列的相关系数，可以用列标签来指定列
b = data.corr()['年销售额(万元)']
print(b)
#分组汇总数据
import pandas as pd
data = pd.read_excel('数据.xlsx')
a = data.groupby('产品')
print(a)#返回的是DataFrameGroupBy对象，可用mean()，max(),sum()进行计算
b = data.groupby('产品').sum()
print(b)
#分组后对某一列进行汇总运算，可以列标签指定列
c = data.groupby('产品')['利润'].sum()
#也可以选取多列后进行汇总计算
d = data.groupby('产品')['数量','利润'].sum()
print(d)
#创建数据透视表
a = pd.pivot_table(data,values='利润',index='产品',aggfunc='sum')
print(a)
b = pd.pivot_table(data,values=['利润','成本'],index='产品',aggfunc='sum')#两个标签的数据相加
print(b)

