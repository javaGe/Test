import time

from selenium import webdriver
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.drvier = webdriver.Chrome()
        self.url = 'https://www.baidu.com'
        self.drvier.get(self.url)

    def test_login_case(self):
        self.drvier.find_element_by_id('kw').send_keys('hhh')
        self.drvier.find_element_by_id('su').click()

    def tearDown(self):
        time.sleep(3)
        self.drvier.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)