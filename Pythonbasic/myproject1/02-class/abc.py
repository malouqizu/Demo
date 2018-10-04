# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Demo1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "file:///E:/selenium/day01/seleniumday01demo/example01.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_demo1(self):
        driver = self.driver
        driver.get(self.base_url + "file:///E:/selenium/day01/seleniumday01demo/example01.html")
        myname = u"张三"
        mymail = "zhangsan@tedu.cn"
        mycomments = u"你好，Selenium！"
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(myname)
        driver.find_element_by_name("e-mail").clear()
        driver.find_element_by_name("e-mail").send_keys(mymail)
        driver.find_element_by_name("comments").clear()
        driver.find_element_by_name("comments").send_keys(mycomments)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        mytitle = driver.title
        print(u"页面标题：" + mytitle)
        myliuyanbo = driver.find_element_by_css_selector("th").text
        print(u"页面题目：" + myliuyanbo)
        myemail = driver.find_element_by_xpath("//tr[3]/td").text
        print("E-Mail:" + myemail)
        self.assertEqual(u"留言簿a", driver.title)
        self.assertEqual(u"张三", driver.find_element_by_name("name").get_attribute("value"))
        self.assertEqual(u"完 成", driver.find_element_by_css_selector("input[type=\"submit\"]").get_attribute("value"))
        self.assertEqual(u"留言簿a", driver.find_element_by_css_selector("th").text)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        print(u"我是：" + myname + u",邮箱:" + mymail + u",留言内容：" + mycomments)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
