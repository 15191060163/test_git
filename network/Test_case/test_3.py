from selenium import webdriver
import time
import unittest
from common2.shiwubanli import login
from common2.shiwubanli import ADD2
class test_OA(unittest.TestCase):
    def setUp(self):
        self.we = webdriver.Firefox()
        self.we.get("http://192.168.0.126:801/Login.aspx")
        time.sleep(5)
        login(self.we, "tbx_UserName", "adm", "tbx_Password", "adm", "ibtLogin")
    def test_OA1(self):
        ADD2(self.we,"ul:nth-child(6) > li:nth-child(2)")
    def tearDown(self):
        self.we.quit()
if __name__=="__main__":
    unittest.main()
