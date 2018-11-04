# coding=utf-8
'''
该py文件用来读取所用到的配置文件
'''

import configparser
import os

def getConfigInfo(info, key):
    '''
    定义一个函数用来获取配置文件中的信息
    :param name: 配置文件中key
    :return: 返回配置文件中key对应的值
    '''

    # 创建一个配置解析器
    cf = configparser.ConfigParser()
    # 获取当前文件路径 os.path.dirname(path):获取path的上一级目录
    curr_path = os.path.dirname(os.path.abspath('.'))
    # 获取配置文件的坐在位置，并读取配置文件内容
    config_path = curr_path + r'\config\config.ini'
    cf.read(config_path)
    # 读取配置文件内容
    browser_name = cf.get(info, key)
    return browser_name



#print(getConfigInfo('browser','BrowserName'))