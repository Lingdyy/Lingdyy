# -*- coding: utf-8 -*-
# @Time    : 15:29
# @Author  : Ling_dy
# @FileName: 练习4.py
# @Software: PyCharm
import requests
import json
from requests.exceptions import RequestException
import re
import time
import urllib.parse
from urllib.request import urlretrieve
import pandas as pd
def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
        # response = requests.get(url,headers)
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        response = urllib.request.urlopen(req)  # 发送请求，获得响应
        text = response.read().decode('utf-8')  # 读取响应，获得文本
        if response.status ==200:
            print(text)
            return text
        return None
    except RequestException:
        return None
def parse_one_page(text):
    for item in json.loads(text)['data']['movies']:

        yield {
            'cat':item['cat'],
            'imag':item['img'],
            'score':item['sc'],
            'name':item['nm'],
            'time':item['pubDesc'],
            'star':item['star'],}
profile_dic = []
def main(offset):

    url = 'https://i.maoyan.com/asgard/asgardapi/mmdb/movieboard/moviedetail/fixedboard/39.json?ci=789&year=0&term=0&limit=10&offset=' + str(offset)
    text = get_one_page(url)
    print(text)
    for item in parse_one_page(text):
        print(item)
        profile_dic.append(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i *10)
        time.sleep(1)
    data_info = pd.DataFrame(profile_dic)
    data_info.to_csv('猫眼电影.csv', encoding='utf-8', index=False)

    
        
