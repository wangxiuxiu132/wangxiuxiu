import unittest
import time
from selenium import webdriver

class Denglu(unittest.TestCase()):
    huohu=webdriver.Firefox()
    def login(self):
        self.huohu.get("http://123.57.140.190/manage/index.php")
        time.sleep(1)
        self.huohu.find_element_by_name("Username").send_keys("admin")
        self.huohu.find_element_by_name("Password").send_keys("admin999")
        self.huohu.find_element_by_xpath("/html/body/div/section/form/div/input[3]").click()
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()

