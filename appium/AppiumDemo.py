import time
# 导入driver对象
from appium import webdriver

# 配置操作app的参数
'''
desired_capabilities是一个字典，配置的是自动化测试的一些必要信息，
包含了本次测试的平台名称及版本号、启动的是浏览器还是app等，
客户端将这些告诉服务器，服务器根据这些信息创建自动化会话。
这里只介绍跟Android平台相关并且常用的几个

automationName：定义测试引擎，使用的android-sdk版本小于17时，使用Selendroid，大于等于17时使用Appium，默认是Appium

platformName：测试平台，通常用于移动设备，值有：Android、IOS、FirefoxOS

platformVersion：测试平台版本，根据设备的固件版本指定，例如Android的4.2、IOS的7.1

deviceName：设备名称

app：要安装的app的文件路径，可以是本地的绝对路径，也可以是远程网络路径

browserName：启动的浏览器名称，测试的是web应用时指定，Android平台设置为Chrome

newCommandTimeout：为了结束Appium会话，会设置一个等待从客户端发送命令的超时时间，默认为60秒，一般不需要设置

autoLaunch：测试时是否需要自动运行app

appPackage：设置app的包名，告诉Appium需要启动的app

appActivity：设置启动的Activity

appWaitActivity：要等待的Activity

appWaitPackage：要等待的appPackage

unicodeKeyboard：是否使用unicode键盘输入，在输入中文字符和unicode字符时设置为true

resetKeyboard：是否将键盘重置为初始状态，设置了unicodeKeyboard时，在测试完成后，设置为true，将键盘重置

'''

#com.android.contacts  包名
#com.android.contacts.activities.PeopleActivity 启动名
# com.tencent.mm/com.tencent.mm.ui.LauncherUI

# 设置启动需要的参数
desired_caps={
    'platformName':'Android', # 平台名称
    'platformVersion':'4.4', # 平台版本
    'deviceName':'XiaoMi', #驱动名称
    'appPackage':'com.android.contacts', # 包名
    'appActivity':'com.android.contacts.activities.PeopleActivity' #启动名
}


# 声明手机的驱动对象 desired_capabilities：服务端的启动参数
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

#脚本内启动其他app

driver.start_activity(app_package='', app_activity='')

time.sleep(5)

# 关闭驱动
driver.quit()
