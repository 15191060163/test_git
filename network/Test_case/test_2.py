# 添加新增事务
import sys,os
sys.path.append(r"C:\Users\000\PycharmProjects\network")
from selenium import webdriver
import time
import unittest
from common2.shiwubanli import login
from common2.shiwubanli import ADD
from common2.shiwubanli import ADD1

class test_OA(unittest.TestCase):
    def setUp(self):
        self.we=webdriver.Firefox()
        self.we.get("http://192.168.0.126:801/Login.aspx")
        time.sleep(5)
        login(self.we, "tbx_UserName", "adm", "tbx_Password", "adm", "ibtLogin")
        self.we.implicitly_wait(10)
        ADD(self.we, " ul:nth-child(6) > li:nth-child(1)", "tab_OaAffairPost_ifm", "//*[@id='kind']", 0)
    def test_1(self):
        # ADD(self.we," ul:nth-child(6) > li:nth-child(1)","tab_OaAffairPost_ifm","//*[@id='kind']",5)
        dict1={"//*[@id='subject']":"费用报销","/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input":
            "2020-06-01","/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input":"1",
               "/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input":"餐费","/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input":
               "500","/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input":"500"}
        ADD1(self.we,dict1,"save")
        self.we.implicitly_wait(10)
        t = self.we.switch_to.alert.text
        time.sleep(3)
        # print(t)
        self.assertEqual(t, "成功：当前事务创建成功！", msg="错误")
    def test_2(self):
        dict1 = {"//*[@id='subject']": "", "/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input":
            "2020-06-01", "/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input": "1",
                 "/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input": "餐费",
                 "/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input":
                     "500", "/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input": "500"}
        ADD1(self.we, dict1, "save")
        s = self.we.find_element_by_css_selector("body > div:nth-child(3)").text
        print(s)
        self.we.implicitly_wait(10)
        self.assertEqual(s, "◆\n◆\n!请填写此字段。", msg="错误")
    def tearDown(self):
        self.we.quit()

if __name__=="__main__":
    unittest.main()
