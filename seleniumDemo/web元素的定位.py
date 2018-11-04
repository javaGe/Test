#coding=utf-8

'''
定位页面元素进行操作
通过html中的标签属性进行位
例如：id，name, class, xpath方法等

'''
import time

from selenium import webdriver

browse = webdriver.Chrome()

url = 'http://www.baidu.com'

# 打开链接页面
browse.get(url)

# 获取百度输入框，然后输入内容
input_button = browse.find_element_by_id('kw').send_keys('python')

# 获取搜索按钮
search_button = browse.find_element_by_id('su').click()

time.sleep(2)
# 退出
browse.quit()

