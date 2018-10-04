#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0401demo/03-linktext.html"
driver.get(base_url)

#使用linktext方式定位超级链接
mylink1=driver.find_element_by_link_text("链接到01-id.html")
sleep(2)
#点击超级链接
mylink1.click()
sleep(2)
#浏览器后退
driver.back()
mylink2=driver.find_element(By.LINK_TEXT,"链接到02-name.html")
sleep(2)
mylink2.click()

