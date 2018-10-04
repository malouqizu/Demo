#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0401demo/05-classname.html"
driver.get(base_url)

name="testing"
password="abcdef"

#使用classname定位页面元素
myname=driver.find_element(By.CLASS_NAME,"username")
mypassword=driver.find_element(By.CLASS_NAME,"password")
mybutton=driver.find_element(By.CLASS_NAME,"submit")

myname.send_keys(name)
mypassword.send_keys(password)
sleep(2)
mybutton.click()
