# coding:gbk
# http://www.cnblogs.com/paisen/p/3312631.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


chromedriver = r"E:\software\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")
driver.find_element_by_id('lb').click()
# driver.find_element_by_id('TANGRAM__PSP_10__unameLoginLink').click()
time.sleep(3)

driver.find_element_by_name('userName').send_keys('lanni654321')
driver.find_element_by_name('password').send_keys('wxy123456')
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()

try:
    dr = WebDriverWait(driver, 10)  # 10����ÿ��500����ɨ��1��ҳ��仯��������ָ����Ԫ�غ����,driver��������ľ��
    '''WebDriverWait�μ��£�
http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver_support/selenium.webdriver.support.wait.html'''
    dr.until(lambda the_driver: the_driver.find_element_by_css_selector('.user-name-top').is_displayed())
except  Exception:
    print '��¼ʧ��'

user = driver.find_element_by_css_selector('.user-name-top')
webdriver.ActionChains(driver).move_to_element(user).perform()  # ��궨λ���û���
driver.find_element_by_css_selector('a.sep').click()