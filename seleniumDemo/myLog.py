#coding=utf-8
import logging # 导入日志模块
import os
import time

def getLogger(name):
    # 创建一个log对象
    logger = logging.getLogger(name)
    # 设置日子打印的级别
    logger.setLevel(logging.INFO)

    # 日志名称
    log_name = name + '-' + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    # 创建日志句柄，日志文件存储的位置
    # log_file_path = os.path.dirname(os.path.abspath('.'))+'\\log\\'+log_name+'.log'
    log_file_path = os.path.abspath('.') + '\\' + name + '.log'
    print(log_file_path)
    fileh = logging.FileHandler(log_file_path)
    # 设置日志级别
    fileh.setLevel(logging.INFO)

    # 创建在终端也输出日志
    consoleh = logging.StreamHandler()
    consoleh.setLevel(logging.INFO)


    # 设置日志打印的格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileh.setFormatter(formatter)
    consoleh.setFormatter(formatter)

    # 创建添加日志的句柄
    logger.addHandler(fileh)
    logger.addHandler(consoleh)

    return logger

    # logger.info('hello python')

log = getLogger('test')
log.info('哈哈哈')
