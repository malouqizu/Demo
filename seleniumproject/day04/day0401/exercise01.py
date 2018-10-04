from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
driver.get("http://192.168.23.128:8060")
#准备测试数据
loginname="admin"
password="12"

#使用id定位页面元素
#myname=driver.find_element_by_id("username")
#mypassword=driver.find_element_by_id("password")
#mylogin=driver.find_element_by_id("submit")

#使用find_element函数进行定位
#myname=driver.find_element(By.ID,"username")
#mypassword=driver.find_element(By.ID,"password")
#mylogin=driver.find_element(By.ID,"submit")

#使用name方式进行定位
myname=driver.find_element(By.NAME,"username")
mypassword=driver.find_element(By.NAME,"password")
mylogin=driver.find_element(By.NAME,"submit")

#操作页面元素
sleep(2)
myname.send_keys(loginname)
sleep(2)
mypassword.send_keys(password)
sleep(2)
mylogin.click()

#在控制台输出信息
print("用户名：",loginname,"密码:",password)