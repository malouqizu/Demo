#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0402demo/demo10.html"
driver.get(base_url)

mypic1=driver.find_element(By.ID,"pic1")
sleep(2)
driver.set_window_size(1000,800)
mypic1.click()
sleep(2)
driver.back()
sleep(2)
mypic2=driver.find_element(By.ID,"pic2")
mypic2.click()
