from selenium import webdriver
import unittest
import time

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        self.url = 'http://demo.zentao.net/user-login.html'
        self.driver.get(self.url)

    def test_login_case(self):
        # 获取用户名输入框
        account = self.driver.find_element_by_name('account')
        account.clear()
        account.send_keys('demo')

        # 获取密码输入框
        pwd = self.driver.find_element_by_name('password')
        pwd.clear()
        pwd.send_keys('123456')

        # 点击登录按钮，进行登录
        submit = self.driver.find_element_by_id('submit')
        submit.click()
        

    def tearDown(self):

        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':

    unittest.main(verbosity=2)
