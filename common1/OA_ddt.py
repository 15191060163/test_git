import sys,os
sys.path.append(r"C:\Users\000\PycharmProjects\办公\common1")
import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack
from common1.OA_data import Excel_data

path=r"D:\课件\文件\OA.xlsx"
excel=Excel_data()
# excel.OA_data1(path)
@ddt
class office(unittest.TestCase):

    def setUp(self):
        self.we=webdriver.Firefox()
        self.we.get("http://192.168.0.126:801/Login.aspx")
        time.sleep(5)
    @data(*excel.OA_data1(path))
    @unpack
    def test1(self,name1,mname2):
        self.we.find_element_by_id("tbx_UserName").clear()
        self.we.find_element_by_id("tbx_UserName").send_keys(name1)
        self.we.find_element_by_id("tbx_Password").send_keys(mname2)
        self.we.find_element_by_id("ibtLogin").click()
        a = self.we.switch_to.alert.text
        print(a)
        self.assertEqual(a, "失败：用户账号或密码错误！", msg="错误")
        time.sleep(5)

    def tearDown(self):
        # self.we.close()
        self.we.quit()


if __name__ == '__main__':
    unittest.main()
