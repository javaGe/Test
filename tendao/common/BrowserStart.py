# coding=utf-8
import time

from test.tendao.common.ReadConfig import getConfigInfo
from selenium import webdriver
from test.tendao.common.CapPicture import capPicture
'''
根据不同的浏览器名称判断来启动不同的浏览器驱动
'''

# 获取浏览器名称
browser_name = getConfigInfo('browser','BrowserName')
# 获取浏览器请求的url
url = getConfigInfo('browser','Url')
if browser_name == 'Chrome':
    driver = webdriver.Chrome()
    driver.get(url)
if browser_name == 'IE':
    driver = webdriver.Ie()
    driver.get(url)
capPicture(driver)

time.sleep(3)
driver.quit()
