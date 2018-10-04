from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day05/day0501demo/demo03.html"
driver.get(base_url)

h1=driver.find_element(By.XPATH,"//input[@checked]")

sleep(1)
h1.click()