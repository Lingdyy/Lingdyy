# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 11:04
# @Author  : Ling_dy
# @FileName: tiao.py
# @Software: PyCharm
#查找数据
import pandas as pd
data = pd.read_excel('数据.xlsx')#下面所有操作都基于这第一二行
print(data)
#用isin()查看DataFrame是否包含某个值
data1 = data.isin(['英国','新闻'])
#用isin()判断数据某一列是否有某个值
data2 = data['国家'].isin(['英国'])
#对数据 进行替换，用replace(),一对一替换
data.replace('英国','xxx(英国)',inplace=True)
print(data)
data.replace('old','new',inplace = True)
print(data)
data = pd.DataFrame(data)
data.to_csv('xxx.csv',encoding='utf-8',index=False)
#用replace()进行多对一替换
data.replace(['英国','England'],'xxx(英国)',inplace = True)
print(data)
#多对多替换
data.replace({'英国':'xxx(英国)','美国':'xxx(美国)','新西兰':'xxx(新西兰)'},inplace=True)
print(data)
#插入数据
data['国家'] = ['英国','英国','美国','新西兰']
print(data)
#指定位置插入数据
data.insert(2,'国家',['英国','英国','美国','新西兰'])
print(data)
a = data.drop(['成本价(元/个)','成本(元)'],axis=1)#axis为0表示删除行，axis为1表示删除列
b = data.drop(data.columns([2,5],axis = 1))# 删除第2和5列
print(b)
#通过 将列标签以列表的形式传递给drop()函数的参数colunms来删除列
c = data.drop(columns=['成本价(元/个)','成本(元)'])
print(c)
#通过行标签以行的形式传递给drop()函数的参数index来删除行
c = data.drop(index = ['a001','a004'])
print(c)
#查看缺失值
print(data.info())
#查看缺失值位置
a = data.isnull()
print(a)
#删除缺失值
b = data.dropna()#会删除所有有空白数据的行
print(b)
c= data.dropna(how = 'all')#当整行是空的时候才会删除
print(c)
#填充缺失值，fillna()
d = data.fillna(0)#缺失的数据全部填充为0
print(d)
#删除重复行
a = data.drop_duplicates()
print(a)
#删除某一列 的重复值
b = data.drop_duplicates(subset = '国家')
print(b)
c = data.drop_duplicates(subset ='国家',keep = 'first' )#keep()设置为first表示保留第一个重复值所在行，不设置也会默认保留第一个，若设置为last，则会保留最后一个
print(c)
#若把keep设置为False,则会把重复值一个不保留的全部删除
#获取唯一值unique()
f = data['国家'].unique()
print(f)
#对数据进行排序
a = data.sort_values(by='国家',ascending=True)#对国家进行升序排序，若为False,则为降序排序
print(a)
c = data['国家'].rank(method = 'average',ascending=False)#method设置为average表示数值遇到重复值取重复值排序的平均值，ascending设置为False表示降序排序
print(c)
#若把method设置为first，则越靠前的名越靠前
#筛选数据
a= data[data['国家']=='英国']
print(a)
b = data[data['数量']>60]
print(b)
#筛选多个条件
c = data[(data['国家']=='英国')&(data['数量']>60)]#筛选国家为英国且数量大于60的数据
print(c)
#转置数据表行列
a= data.T
print(T)
#将数据表转换为树形结构，二维表格建立层次化的索引
a = data.stack()
print(a)





