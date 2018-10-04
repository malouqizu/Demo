from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day06/day0601demo/demo02.html"
driver.get(base_url)
#定位并点击提交按钮
submit=driver.find_element(By.XPATH,"//input[2]")
submit.click()

#定位alert
alert1=driver.switch_to.alert
#获取alert中的文本
txt1=alert1.text
print("提示信息:",txt1)
#点击确定按钮
sleep(2)
alert1.accept()