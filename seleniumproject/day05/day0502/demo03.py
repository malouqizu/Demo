from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#导入Keys类
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day05/day0502demo/demo03.html"
driver.get(base_url)

#定位页面元素
username=driver.find_element(By.XPATH,"//*[@id='username']")
count=driver.find_element(By.XPATH,"//*[@id='count']")
comments=driver.find_element(By.XPATH,"//*[@id='beizhu']")

username.send_keys("张三a")
#输入backspace
sleep(1)
username.send_keys(Keys.BACKSPACE)
#输入字母，同时按下
sleep(1)
count.send_keys(Keys.SHIFT,"abcdefg")

#全选姓名
sleep(1)
username.send_keys(Keys.CONTROL,"a")
#复制姓名
username.send_keys(Keys.CONTROL,"C")

#在备注中粘贴姓名
comments.send_keys("姓名:")
sleep(1)
comments.send_keys(Keys.CONTROL,"v")

count.send_keys(Keys.CONTROL,"A")
count.send_keys(Keys.CONTROL,"X")

sleep(1)
#输入回车键
comments.send_keys(Keys.ENTER)
comments.send_keys("账号:")
comments.send_keys(Keys.CONTROL,"v")
comments.send_keys(Keys.ENTER)
comments.send_keys("软件测试")
#移动光标
sleep(2)
comments.send_keys(Keys.ARROW_LEFT)
sleep(2)
comments.send_keys(Keys.HOME)
sleep(2)
comments.send_keys(Keys.ARROW_UP)
sleep(2)
comments.send_keys(Keys.END)






