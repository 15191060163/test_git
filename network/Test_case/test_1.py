import sys,os
sys.path.append(r"C:\Users\000\PycharmProjects\network")
from selenium import webdriver
import time
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from common2.shiwubanli import login
class office(unittest.TestCase):
    def setUp(self):
        self.we=webdriver.Firefox()
        self.we.get("http://192.168.0.126:801/Login.aspx")
        time.sleep(5)
    def test_1(self):
        login(self.we, "tbx_UserName", "adm", "tbx_Password", "adm", "ibtLogin")
        a1 = self.we.find_element_by_css_selector("div.collapse:nth-child(1)").text
        self.assertEqual(a1, "电子邮件", msg="错误")
    def test_2(self):
        login(self.we,"tbx_UserName", "adm", "tbx_Password", "123", "ibtLogin")
        a = self.we.switch_to.alert.text
        self.assertEqual(a, "失败：用户账号或密码错误！", msg="错误")
    def tearDown(self):
        self.we.quit()
if __name__=="__main__":

    unittest.main()