import unittest
import time
from selenium import webdriver

class Denglu(unittest.TestCase):
    huohu=webdriver.Firefox()
    def setUp(self):
        self.huohu.get("http://123.57.140.190/manage/index.php")
        time.sleep(3)
    def tearDown(self):
        self.huohu.close()
        self.huohu.quit()
        time.sleep(3)
    # 错误的账号
    def test_02denglu(self):
        self.huohu.find_element_by_name("Username").send_keys("adm")
        self.huohu.find_element_by_name("Password").send_keys("admin999")
        self.huohu.find_element_by_xpath("/html/body/div/section/form/div/input[3]").click()
        time.sleep(1)
        expect =  self.huohu.find_element_by_xpath("/html/body/div[1]/div").text
        print(expect)

        self.assertEqual(expect, "您输入的帐号或密码有误！", msg="账号有误")
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()