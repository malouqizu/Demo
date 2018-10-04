#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0401demo/04-partiallinktext.html"
driver.get(base_url)

mylink=driver.find_element(By.PARTIAL_LINK_TEXT,"自")
sleep(2)
mylink.click()