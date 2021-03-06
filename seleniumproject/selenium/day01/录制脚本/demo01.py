# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Demo01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "file:///E:/Python/demo/seleniumproject/selenium/day01/seleniumday01demo/example01.html"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_demo01(self):
        driver = self.driver
        driver.get(self.base_url + "file:///E:/Python/demo/seleniumproject/selenium/day01/seleniumday01demo/example01.html")
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"李四")
        driver.find_element_by_name("e-mail").clear()
        driver.find_element_by_name("e-mail").send_keys("zhangsan@126.com")
        driver.find_element_by_name("comments").clear()
        driver.find_element_by_name("comments").send_keys(u"张三，你好！")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
