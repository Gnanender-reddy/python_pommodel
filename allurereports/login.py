from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestHrm:

    @allure.severity(allure.severity_level.MINOR) #this is for telling severity level in test cases.
    def test_Logo(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status=self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Normally skipping")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        actual_title=self.driver.title
        if actual_title=="OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testloginscreen",attachment_type=AttachmentType.PNG )
            #above will take screen shots and save it to the allure reports.
            self.driver.close()
            assert False

#To run test cases : pytest -v -s --alluredir="/home/admin1/PycharmProjects/UnittestPomBasedProject/allurereports/reports" login.py
#generating allure reports: allure serve /home/admin1/PycharmProjects/UnittestPomBasedProject/allurereports/reports
#to share allure reports: netlify.com
#export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
#export PATH="/home/admin1/Downloads/allure-2.13.0/bin/:$PATH"
#allure --version
