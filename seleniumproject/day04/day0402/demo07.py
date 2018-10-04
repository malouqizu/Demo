#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#实例化Firefox类
driver=webdriver.Firefox()
#打开页面
base_url="file:///E:/Python/demo/seleniumproject/day04/seleniumday0402demo/demo07.html"
driver.get(base_url)
#准备测试数据
mydata1={"姓名":"testing","密码":"test123","留言":"I am a tester!"}
mydata2={}

#定位页面元素
myname=driver.find_element(By.ID,"username")
mypassword=driver.find_element(By.ID,"password")
mycomments=driver.find_element(By.ID,"comments")
mybutton=driver.find_element(By.ID,"submit")
#操作页面元素
myname.clear()
myname.send_keys(mydata1["姓名"])
mypassword.clear()
mypassword.send_keys(mydata1["密码"])
mycomments.clear()
mycomments.send_keys(mydata1["留言"])
sleep(2)
#获得文本框填写的内容
mydata2["姓名"]=myname.get_attribute("value")
mydata2["密码"]=mypassword.get_attribute("value")
mydata2["留言"]=mycomments.get_attribute("value")
print("姓名:",mydata2["姓名"],"长度:",len(mydata2["姓名"]))
print("密码:",mydata2["密码"],"长度:",len(mydata2["密码"]))
print("留言内容:",mydata2["留言"],"长度:",len(mydata2["留言"]))
#判断输入的姓名是否正确
if mydata2["姓名"]==mydata1["姓名"]:
    print("姓名正确！")
else:
    print("姓名错误！")

#判断提交按钮是否可用，如果可用，点击，如果不可用，提示信息
p1=mybutton.get_attribute("value")
if mybutton.is_enabled():
    print("点击",p1,"按钮")
    mybutton.click()
else:
    print("按钮不可用！")







