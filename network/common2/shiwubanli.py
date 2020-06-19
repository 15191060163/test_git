# 公共接口
from selenium import webdriver
from selenium.webdriver.support.select import Select

# 登录
def login(webdriver,element_use,use,element_psw,psw,click_login):

    webdriver.find_element_by_id(element_use).send_keys(use)
    webdriver.find_element_by_id(element_psw).send_keys(psw)
    webdriver.find_element_by_id(click_login).click()
#  进入新建事务
def ADD(webdriver,element_css,switch_frame,element_xpath,sum):
    webdriver.find_element_by_css_selector(element_css).click()
    webdriver.switch_to.frame(switch_frame)
    s = webdriver.find_element_by_xpath(element_xpath)
    Select(s).select_by_index(sum)
#  增加新建事务
def ADD1(webgriver,xpath_dict,click_id):
    for i in xpath_dict.items():
        # print(i)
        webgriver.find_element_by_xpath(i[0]).send_keys(i[1])
    webgriver.find_element_by_id(click_id).click()
# 进入已建事务
def ADD2(webdriver,element_css):
    webdriver.find_element_by_css_selector(element_css).click()




