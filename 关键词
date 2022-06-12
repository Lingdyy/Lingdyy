# -*- coding: utf-8 -*-
# @Time    : 2022/6/12 14:58
# @Author  : Ling_dy
# @FileName: 新闻关键词的提取与汇总.py
# @Software: PyCharm

import requests #用于获取网页源代码
from bs4 import BeautifulSoup #用于从网页源代码中提取数据
from jieba import analyse #用于从新闻内容中提取关键词
import os #用于完成文件和文件夹相关操作
import pandas as pd #用于完成数据存储
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
url = 'http://www.centrechina.com/news/jiaodian'
response = requests.get(url,headers) #对今日焦点新闻首页的网址发出请求，获取响应
html_data = response.text #从响应对象中提取网页源代码
soup = BeautifulSoup(html_data,'lxml') #将网页源代码实例化为BeautifulSoup对象
hotnews_url_list = [] #用于存储新闻详情页网址的列表
a_list = soup.select('.ajax-load-con h2 a') #选中每一条新闻的<a>标签
for a in a_list:
    hotnews_url_list.append(a['href']) #从<a>标签中提取网址并添加到列表中
def get_text(url): #请求网址并返回BeautifulSoup对象
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
    response = requests.get(url,headers)
    response.encoding = 'utf-8'
    html_data = response.text
    soup = BeautifulSoup(html_data,'lxml') #封装成BeautifulSoup的对象
    parse_url(soup) #调用BeautifulSoup对象解析函数，提取数据
def parse_url(soup): #解析BeautifulSoup对象
    title = soup.select('.post-title h1')[0].string #获取class属性值为post-title
    print(title)
    p_list = soup.select('.post-content p') #选中class属性值为post-content的
    for p in p_list: #用循环遍历每个<p>标签
        if p.string: #当<p>标签的直系文本不为空时才进行写入
            with open(f'新闻/{title}.txt','a',encoding='utf-8') as fp:
                fp.write(p.string) #将<p>标签的直系写入txt文件
for url in hotnews_url_list:
    get_text(url)

keywords_dict = {'新闻标题':[],'新闻检索关键词':[]} #创建字典用于存储关键词提取
txt_name = os.listdir('新闻') #获取“新闻”文件夹下的所有文件名
for txt_file in txt_name: #循环取出每个文件名
    with open('新闻/' + txt_file,'r+',encoding='utf-8') as fp1: #通过文件名读取
        txt_content = fp1.read()
    keywords = analyse.textrank(txt_content,topK=10,withWeight=False) #
    print(keywords)
    keywords_dict['新闻标题'].append(txt_file) #将文件名也就是新闻标题写入字典
    keywords_dict['新闻检索关键词'].append(keywords) #将提取的关键词写入字典
news_keyswords_info = pd.DataFrame(keywords_dict,columns=['新闻标题','新闻检索关键词'])
news_keyswords_info.to_csv('新闻检索关键词.csv',index=False,encoding='utf-8')

