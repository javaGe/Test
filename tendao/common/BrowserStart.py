# coding=utf-8
import time

from test.tendao.common.ReadConfig import getConfigInfo
from selenium import webdriver
from test.tendao.common.CapPicture import capPicture
from test.tendao.common.LogTool import getLogger
'''
根据不同的浏览器名称判断来启动不同的浏览器驱动
'''

# 获取日志对象
log = getLogger('BrowserStart')

# 获取浏览器名称
browser_name = getConfigInfo('browser','BrowserName')
# 获取浏览器请求的url
url = getConfigInfo('browser','Url')

if browser_name == 'Chrome':
    log.info('启动Chrome浏览器')
    driver = webdriver.Chrome()

    log.info('请求网页：'+url)
    driver.get(url)

if browser_name == 'IE':
    driver = webdriver.Ie()
    driver.get(url)
# 进行截图
capPicture(driver)

time.sleep(3)
driver.quit()
log.info('关闭浏览器')
