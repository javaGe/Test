# coding = utf-8


import time
# 导入驱动
from selenium import webdriver

'''
对浏览器的一些操作
1.设置窗口大小
2.刷新浏览器
3.截图
'''

# 创建一个会话
browse = webdriver.Chrome()

# 请求的url
url = 'https://www.baidu.com'
browse.get(url)

time.sleep(2)
# 设置窗口大小
# 窗口最大化
browse.maximize_window()
# 刷新浏览器
browse.refresh()

time.sleep(2)
# 自定义窗口大小
browse.set_window_size(300,200)
#截取当前浏览器对象
browse.get_screenshot_as_file(r'./test.png')

# 打开三秒后关闭
time.sleep(3)

# 关闭会话
browse.quit()