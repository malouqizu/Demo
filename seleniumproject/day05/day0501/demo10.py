from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day05/day0501demo/demo06.html"
driver.get(base_url)
h1=driver.find_element(By.XPATH,"//a[text()='链接到demo1']")

sleep(2)
h1.click()

sleep(1)
driver.back()
sleep(1)
h2=driver.find_element(By.XPATH,"//a[text()='链接到demo2']")
h2.click()



