# coding=utf-8
import time
import os
from selenium import webdriver
def capPicture(driver):
    '''
    把截取的图片保存到固定目录中
    :param driver: 浏览器驱动
    :return:
    '''

    # 格式化时间
    pt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # 图片保存的路径
    pt_name = os.path.dirname(os.path.abspath('.')) + '\\picture\\' + pt + r'.png'
    # 保存截取的图片
    driver.get_screenshot_as_file(pt_name)