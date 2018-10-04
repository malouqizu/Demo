#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0401demo/06-tagname.html"
driver.get(base_url)

mylink1=driver.find_element(By.TAG_NAME,"a")
sleep(2)
mylink1.click()