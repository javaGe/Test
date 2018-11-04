# coding=utf-8

'''
selenium操作frame框架

frame框架的介绍：
这是一种布局方式，一共有三种形式：frameset,frame,iframe
frame一定要在frameset下
iframe不做要求可以单独使用


例如以下案例：
1.并列的frame
<html>
    <head>
        <title>selenium</title>
    </head>
    <body>
        <iframe src="left.html" id="frame1" name="leftname"></iframe>
        <iframe src="right.html" id="frame2" name="rightname"></iframe>
    </body>
</html>


# selenium的切换：
from selenium import webdriver
driver = webdriver.Chrome()

# 通过id定位进行切换,进入frame1的框架
driver.switch_to.frame('frame1')
# 通过name定位
driver.switch_to.frame('frame2')
# 通过索引定位
driver.switch_to.frame(0)


2.嵌套的frame

<html>
    <head>
        <title>selenium</title>
    </head>
    <body>
        <iframe src="left.html" id="frame1" name="leftname">
            <iframe src="right.html" id="frame2" name="rightname"></iframe>
        </iframe>

    </body>
</html>


这种嵌套的frame，需要逐层的进行切换

# 切换到第一层
driver.switch_to.frame('frame1')
# 切换到第二层
driver.switch_to.frame('frame2')

# 从下到上切换回来
driver.switch_to.parent_frame()

# 切换到默认的第一层
driver.switch_to.default_content()
'''

