import unittest
import time
from selenium import webdriver

class Denglu(unittest.TestCase()):
    huohu = webdriver.Firefox()

    def login(self):
        self.huohu.get("http://123.57.140.190/manage/index.php")
        time.sleep(1)
        self.huohu.find_element_by_name("Username").send_keys("admin")
        self.huohu.find_element_by_name("Password").send_keys("admin999")
        self.huohu.find_element_by_xpath("/html/body/div/section/form/div/input[3]").click()
        time.sleep(2)

class Chanpin(Denglu):
    def setUp(self):
        self.login()

    def tearDown(self):
        self.huohu.close()
        self.huohu.quit()

    def test_01chanpin(self):
        self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
        self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
        time.sleep(2)
        self.huohu.find_element_by_xpath(
            "/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/a").click()
        self.huohu.find_element_by_class_name("form-control").clear()
        self.huohu.find_element_by_class_name("form-control").send_keys("迁西贡栗")
        time.sleep(2)
        try:
            self.huohu.find_element_by_xpath(
                "/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button").click()
            time.sleep(1)
            self.assertEqual("产品更新成功！", self.huohu.find_element_by_css_selector("#layui-layer1").text, msg="更新失败")
            time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    unittest.main()
