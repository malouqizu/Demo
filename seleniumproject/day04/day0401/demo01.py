#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#对Firefox类进行实例化
driver=webdriver.Firefox()
#打开测试网页
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0401demo/01-id.html"
driver.get(base_url)

#准备测试数据
name="张三"
password="123456"
#使用id定位页面元素
#myname=driver.find_element_by_id("username")
#mypassword=driver.find_element_by_id("password")
#mybutton=driver.find_element_by_id("tijiao")

#使用find_element函数进行定位
myname=driver.find_element(By.ID,"username")
mypassword=driver.find_element(By.ID,"password")
mybutton=driver.find_element(By.ID,"tijiao")

#操作页面元素
myname.send_keys(name)
driver.find_element(By.ID,"username").send_keys("李四")

sleep(2)
mypassword.send_keys(password)
sleep(2)
mybutton.click()
#控制台输出信息
print("我是:",name,"密码：",password)
#关闭浏览器
driver.quit()