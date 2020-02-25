"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: python selenium.
@Description:This code is for python pom(page object model) which has only test cases.
"""
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.insert(0, '/home/admin1/PycharmProjects/UnittestPomBasedProject/')
from pageobj.loginpage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="http://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"
    driver=webdriver.Chrome()

    @classmethod
    def setUpClass(cls) :
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"webpage not working")

    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..//reports'))

