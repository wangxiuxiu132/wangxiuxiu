import unittest
import time
from selenium import webdriver

class Denglu(unittest.TestCase):
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
        self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[1]/a").click()
        self.huohu.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").send_keys("礼券水蜜桃")
        time.sleep(2)
        self.huohu.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input").send_keys("bbbb7845481")
        time.sleep(2)
        self.huohu.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input").send_keys("610425561224")
        time.sleep(2)
        self.huohu.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe").send_keys(
            "又大又甜真好吃")
        time.sleep(2)
        self.huohu.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[9]/div/button").click()
        time.sleep(3)
        try:
            expect = self.huohu.find_element_by_xpath("//*[@id='layui-layer1']").text
            self.assertEqual(expect, "产品条码有重复!", msg="新增失败")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
