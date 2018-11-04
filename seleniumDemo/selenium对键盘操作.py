#coding=utf-8

'''
selenium对键盘的一些操作
如：
1.键盘输入
2.回车确认
3.删除
4.ctrl键的控制

操作步骤：
打开百度-->获取输入框-->输入搜索内容-->全选输入内容-->删除
-->再次输入内容-->搜索按钮-->按回车

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = 'https://www.baidu.com'
# 请求百度
driver.get(url)

# 获取搜索输入框
input_but = driver.find_element_by_id('kw')
# 模拟键盘输入搜索内容
input_but.send_keys('python')
time.sleep(2)
# 模拟ctrl+a全选操作
input_but.send_keys(Keys.CONTROL,'a')
time.sleep(2)

# 模拟键盘删除操作
input_but.send_keys(Keys.BACKSPACE)
# 重新输入内容
input_but.send_keys('selenium')
# 获取搜索按钮
submit_but = driver.find_element_by_id('su')
# 模拟键盘回车enter
submit_but.send_keys(Keys.ENTER)

time.sleep(3)

driver.quit()




