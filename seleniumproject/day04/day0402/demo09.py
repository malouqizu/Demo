#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0402demo/demo09.html"
driver.get(base_url)

mylink1=driver.find_element(By.LINK_TEXT,"链接到demo07")
print(mylink1.text)
sleep(2)
mylink1.click()
sleep(1)
driver.back()
sleep(1)
mylink2=driver.find_element(By.LINK_TEXT,"链接到demo08")
print(mylink2.text)
mylink2.click()
