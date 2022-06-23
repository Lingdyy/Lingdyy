# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 21:07
# @Author  : Ling_dy
# @FileName: 自然语言练习.py.py
# @Software: PyCharm
import numpy as np
import re
text_string = '文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫抓取到网络中的信息。爬取的策略有广度爬取和深度爬取。根据用户需求，爬虫可以有主题爬虫和通用爬虫之分。'
regex = '爬虫'
p_string = text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None: #search方法是用来查找匹配当前行是否匹配这个regex，返回的是一个match对象
        print(line)
regex = '文本'
p_string= text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)
regex = '爬.'
p_string = text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)
regex = '^文本'
p_string = text_string.split('。')
for line in p_string:
    if re.search(regex,line) is not None:
        print(line)
text_string = ['[重要的]今年第七号台风23日登录广东东部沿海地区','上海发布车库销售监管通知:违规者暂停网签资格','[紧要的]中国对印连发强硬信息，印度急切需要结束对峙']
regex = '^\[[重紧]..\]'
for line in text_string:
    if re.search(regex,line) is not None:
        print(line)
if re.search('\\\\','I have one nee\dle') is not None:
    print('match it')
else:
    print('not match')
if re.search(r'\\',"I have one mee\dle") is not None:
    print('match it')
else:
    print("not match")
strings = ['War of 1812','There are 5280 feet to a mile','Happy New Year 2016!']
year_strings= []
for string in strings:
    if re.search('[1-2][0-9]{3}',string):
        year_strings.append(string)
print(year_strings)
vector = np.array([1,2,3,4])
matrix = np.array([[1,'Tim'],[2,'Joey'],[3,'Johnny'],[4,'Frank']])
a = np.arange(15).reshape(3,5) #代表3行5列
print(a)
a = np.arange(15).reshape(3,5)
nf1 = np.genfromtxt('price.csv',delimiter = ',')#获取数据集
print(nf1)
nf1 = np.genfromtxt('price.csv',dtype='U75',skip_header=1,delimiter=',')#dtype关键字要设定为'U75'.表示每个值都是75type的unijcode
#skip_header关键字可以设置为整数，这个参数可以跳过文件开头的对应的行数，然后再执行其他操作
print(nf1)
matrix = np.array([[1,2,3],[20,30,40]])
print(matrix[0,1])#0代表第一行，1代表第二列。
matrix= np.array([[5,10,15],[20,25,30],[35,40,45]])
print(matrix[:,1])#所有行，列的索引1
print(matrix[:,0:2])#所有行，列的索引0和1
print(matrix[1:3,:])#所有列，行的索引1和2
print(matrix[1:3,0:2])#行的索引为1和2，列的索引为0和1
second_colunm_25 = (matrix[:1]==25)
print(second_colunm_25)
print(matrix[second_colunm_25,:])#返回代表True那一行的数据
vector = np.array([5,10,11,12])
equal_to_five_and_ten = (vector==5)&(vector==10)
equal_to_five_or_ten = (vector==5)|(vector==10)
vector = np.array([5,10,15,20])
equal_to_five_or_ten = (vector==5)|(vector==10)
vector[equal_to_five_or_ten] = 50
print(vector)
matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])
second_colunm_25 = matrix[:1] == 25
matrix[second_colunm_25,1] = 10
print(matrix)
#把空值替换为0
second_colunm_25 = (matrix[:2]=='')
matrix[second_colunm_25,2] = '0'
print(matrix)
#数据类型转换
vector  = np.array(['1','2','3'])
vector = vector.astype(float)
vector = np.array([5,10,15,20])
vector.sum()
matrix=np.array([[5,10,15],[20,10,30],[35,40,45]])
matrix.sum(axis=1)#计算的是行的和
matrix.sum(axis=0)

