#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0401demo/02-name.html"
driver.get(base_url)

#准备测试数据
count="mytesting"
nickname="东东"

#使用name方式定位页面元素
#mycount=driver.find_element_by_name("count")
#mynickname=driver.find_element_by_name("nicheng")
#mybutton=driver.find_element_by_name("submit")

mycount=driver.find_element(By.NAME,"count")
mynickname=driver.find_element(By.NAME,"nicheng")
mybutton=driver.find_element(By.NAME,"submit")

#操作页面元素
sleep(2)
mycount.send_keys(count)
sleep(2)
mynickname.send_keys(nickname)
sleep(2)
mybutton.click()

#关闭浏览器
driver.quit()