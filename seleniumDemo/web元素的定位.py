#coding=utf-8

'''
定位页面元素进行操作
通过html中的标签属性进行位
例如：id，name, class, xpath方法等

'''
import time

from selenium import webdriver

browse = webdriver.Chrome()
# browse = webdriver.PhantomJS()
# url = 'http://www.baidu.com'
url = 'http://vpn.taxcp.com/xxmh/html/index.html'
# 打开链接页面
browse.get(url)

# 获取百度输入框，然后输入内容
# input_button = browse.find_element_by_id('kw').send_keys('python')

# 获取搜索按钮
# search_button = browse.find_element_by_id('su').click()

# 获取登录按钮
# 1.通过link_text获取
# login_button = browse.find_element_by_link_text('登录')
# print(login_button)

# 2.通过class来获取登录按钮
login_button = browse.find_element_by_class_name('login')
login_button.click()

# 进入登录页面,如果有提示界面，获取界面的确定按钮,点击确定按按钮跳过提示页面
hint_win_button = browse.find_element_by_class_name('btn01')
hint_win_button.click()

# 进入登录页面，填写登录信息
# 用户名输入框
user_name_input = browse.find_element_by_name('userName')
user_name_input.clear()
user_name_input.send_keys('44060500000000G')

# 密码输入框
pwd_input = browse.find_element_by_name('passWord')
pwd_input.clear()
pwd_input.send_keys('123456')

# 获取登录按钮
login_button = browse.find_element_by_id('upLoginButton')
login_button.click()

time.sleep(2)
# 退出
browse.quit()

