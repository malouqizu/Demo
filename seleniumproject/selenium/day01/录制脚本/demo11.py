# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Demo11(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "file:///E:/Python/demo/seleniumproject/selenium/day01/seleniumday01demo/example05.htmll"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_demo11(self):
        driver = self.driver
        driver.get(self.base_url + "file:///E:/Python/demo/seleniumproject/selenium/day01/seleniumday01demo/example05.html")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(u"李蒙蒙")
        driver.find_element_by_name("passwords").clear()
        driver.find_element_by_name("passwords").send_keys("1234")
        driver.find_element_by_name("sex").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("mengmengli@rdamicro.com")
        Select(driver.find_element_by_name("profession")).select_by_visible_text(u"教育/研究")
        driver.find_element_by_name("computer").click()
        driver.find_element_by_name("textfield3").clear()
        driver.find_element_by_name("textfield3").send_keys("jjjjjj")
        self.assertEqual(u"达内测试学院请您留言", driver.title)
        try: self.assertEqual("on", driver.find_element_by_name("sex").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_name("computer").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "1234" == driver.find_element_by_name("passwords").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "on" == driver.find_element_by_xpath("(//input[@name='sex'])[2]").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"达内测试学院请您留言", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if u"艺术/设计" == driver.find_element_by_name("profession").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "on" == driver.find_element_by_name("computer").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if "on" == driver.find_element_by_name("read").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("Submit").click()
    
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
