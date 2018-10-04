from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
driver.get("http://192.168.23.128:8060")

#mylink=driver.find_element(By.LINK_TEXT,"游客进入")

mylink=driver.find_element_by_partial_link_text("游客")

mylink.click()

#准备测试数据
name="王小明"
mail="wangxiaoming@126.com"
comments="你好，小明！"

#定位class方式页面元素
myname=driver.find_element(By.CLASS_NAME,"name")
mymail=driver.find_element(By.CLASS_NAME,"mail")
mycomments=driver.find_element(By.CLASS_NAME,"comments")
mysubmit=driver.find_element(By.CLASS_NAME,"submit1")

#发布留言
myname.clear()
myname.send_keys(name)
mymail.clear()
mymail.send_keys(mail)
mycomments.clear()
mycomments.send_keys(comments)
mysubmit.click()
