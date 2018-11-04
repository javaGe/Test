#coding=utf-8

'''
模拟鼠标的操作：
1.点击
2.双击
3.右键点击
4.拖拽
'''
import time

from selenium import webdriver
# 导入模拟鼠标操作的模块
from selenium.webdriver.common.action_chains import ActionChains
browse = webdriver.Chrome()

url = 'http://www.baidu.com'

# 打开链接页面
browse.get(url)

# 获取百度输入框，然后输入内容
# input_button = browse.find_element_by_id('kw').send_keys('python')

# 获取搜索按钮
# search_button = browse.find_element_by_id('su')
# 单击事件
# search_button.click()

#点击右键操作,获取当前的会话，移动到需要点击的元素上，执行点击操作
# ActionChains(browse).move_to_element(search_button).context_click().perform()

# 双击鼠标操作
# ActionChains(browse).move_to_element(search_button).double_click().perform()

# 鼠标的拖拽演示，拖拽的是元素
aa = browse.find_element_by_id('kw')
bb = browse.find_element_by_id('su')

# 将aa退拽到bb
ActionChains(browse).double_click().perform()
ActionChains(browse).drag_and_drop(aa,bb).perform()


time.sleep(2)
# 退出
browse.quit()

