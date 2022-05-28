# -*- coding: utf-8 -*-
# @Time    : 2022/5/28 11:04
# @Author  : Ling_dy
# @FileName: tiao.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get('http://www.acd-dialogue.org/dialogue-ministerial-meeting.html')
hrefs = browser.find_elements(By.XPATH,"//*[@id='nav-one']/li[4]/a")

for href in hrefs:
    href = href.get_attribute('href')
    browser = webdriver.Chrome(executable_path='chromedriver.exe')
    browser.get(href)
    a_href = browser.find_elements(By.XPATH,"/html/body/div[1]/div[4]/div/div[1]/h1")
    for a in a_href:
        print(a.get_attribute('textContent'))

browser.quit()
