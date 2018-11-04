# coding = utf-8


import time
# 导入驱动
from selenium import webdriver

# 创建一个会话
browse = webdriver.Chrome()

# 请求的url
url = 'https://www.baidu.com'
browse.get(url)

# 打开三秒后关闭
time.sleep(3)

# 关闭会话
browse.quit()