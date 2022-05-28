# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 14:32
# @Author  : Ling_dy
# @FileName: 数据表拼接.py.py
# @Software: PyCharm
import pandas as pd
#读取两个工作表数据
data1 = pd.read_excel('数据.xlsx',sheet_name=0)
data2 = pd.read_excel('数据.xlsx',sheet_name=1)
print(data1)
print(data2)
#使用merge()函数连接数据表data1和data2,merge()函数可以根据一个或多个相同的列将不同数据表连接起来，此函数默认选取相同的列标签进行合并，不同的被筛除在外
a = pd.merge(data1,data2)
print(a)
#合并两个表格所有数据，包括不同的列
b = pd.merge(data1,data2,how = 'outer')
print(b)
#如果相同 的列标签不止一个，可以用on来指定依据哪一列进行合并操作
c = pd.merge(data1,data2,on='国家')
print(c)

#concat可以直接将两个或多个列表合并，不需要两表某些列或索引相同，也可以把数据整合到一起
d = pd.concat([data1,data2])#会保留原有行标签
print(d)
#将ignore_index设置为True，会重置行标签
e = pd.concat([data1,data2],ignore_index=True)
print(e)
#append()直接将一个或多个数据表中的数据合并到其他数据表中
f = data1.append(data2)
print(f)
#在数据表末尾追加数据
g = data1.append({'国家':'法国','网站名称':'xxx(法国)','行业':'智库'},ignore_index = True)
print(g)



