# import necessary packages
import unittest
from selenium import webdriver
from time import sleep
import random
import sys

class LaunchWebPage(unittest.TestCase):
    def __init__(self, testName, arg1, arg2):
        super(LaunchWebPage, self).__init__(testName)
        self.myExtraArg1 = arg1
        self.myExtraArg2 = arg2

    def setUp(self):
        print("initialize web driver")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.shipt.com")
        self.driver.maximize_window()

    def test_launch_webpage(self):
        print("Step1: Launch www.shipt.com in Chrome browser")
        self.webElement=self.driver.find_element_by_class_name("header")
        self.assertIn("SIGN UP", self.webElement.text)
        sleep(5)

    def click_on_signup_button(self):
        print("Step2: Click on the SignUp button and Verify")
        self.ele = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/header/nav/ul[2]/li[2]/a')
        self.ele.click()
        self.assertIn("Let's get started with your membership!",self.driver.find_element_by_tag_name("h1").text)

    def enter_email_zipcode(self,email,zipcode):
        print("Step3: Enter the email and Zipcode")
        try:
            self.email=self.driver.find_element_by_xpath('//*[@id="email"]')
            self.email.clear()
            self.email.send_keys(email)
            self.zipcode=self.driver.find_element_by_xpath('//*[@id="zip"]')
            self.zipcode.clear()
            self.zipcode.send_keys(zipcode)
            self.submit=self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/form/div[3]/p[1]/button')
            self.submit.click()
            sleep(10)
        except Exception:
            print("In error-"+Exception.with_traceback())

    def test_click_on_signup_button_valid_credntials(self):
        self.click_on_signup_button()
        self.enter_email_zipcode(self.myExtraArg1, self.myExtraArg2)
        self.assertIn("Try Free for 2 Weeks!",self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[1]/div/div/div[1]/a/div[1]/h4').text)
       
    def test_click_on_signup_button_invalid_zipcode(self):
        self.click_on_signup_button()
        self.enter_email_zipcode(self.myExtraArg1, self.myExtraArg2)
        self.assertIn("Please enter a valid zip code",self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/form/div[3]/p[1]').text)

    def test_click_on_signup_button_registered_emailid(self):
        self.click_on_signup_button()
        self.enter_email_zipcode(self.myExtraArg1, self.myExtraArg2)
        self.assertIn("We noticed there is an account with that email. Please Login.",self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/form/div[1]/p').text)

    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LaunchWebPage("test_launch_webpage","",""))
    #generate some dummy email (for now, as I don't know  this email exists in your database or not)
    #85001 is the zip where we serve, 950 is invalid zip
    email='dummy_email_'+ str(random.randint(0,1809080)) + '@ourdomain.com'
    suite.addTest(LaunchWebPage("test_click_on_signup_button_valid_credntials",email,"85001"))
    suite.addTest(LaunchWebPage("test_click_on_signup_button_invalid_zipcode",email ,"950"))
    suite.addTest(LaunchWebPage("test_click_on_signup_button_registered_emailid", "ushasarthi@gmail.com", "85001"))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
