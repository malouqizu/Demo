from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day06/day0601demo/demo05.html"
driver.get(base_url)
link1=driver.find_element(By.XPATH,"//a[1]")
print("当前页面的标题：",driver.title)
print("当前页面地址：",driver.current_url)
sleep(1)
link1.click()

sleep(1)
driver.refresh()
sleep(2)
driver.set_window_size(1200,500)
print("当前页面的标题：",driver.title)
print("当前页面地址：",driver.current_url)
sleep(1)
driver.close()
