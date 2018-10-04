from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day05/day0501demo/demo05.html"
driver.get(base_url)

#使用多条件定位
#h1=driver.find_element(By.XPATH,"//a[@title='链接'][@target='_blank']")
#h1=driver.find_element(By.XPATH,"//a[@title='链接' and @target='_blank']")

#使用last函数定位
h1=driver.find_element(By.XPATH,"//a[last()]")
sleep(2)
h1.click()