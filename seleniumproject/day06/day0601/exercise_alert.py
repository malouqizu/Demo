from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="http://www.sahitest.com/demo/index.htm"
driver.get(base_url)

#定位超级链接并点击
alertlink=driver.find_element(By.XPATH,"//td[3]/a")
alertlink.click()

#在文本框中输入提示信息，点击第一个按钮
sleep(2)
alertmsg=driver.find_element(By.XPATH,"//input")
alertmsg.clear()
alertmsg.send_keys("请输入姓名！")
button1=driver.find_element(By.XPATH,"//input[2]")
sleep(1)
button1.click()

#获取alert
alert1=driver.switch_to.alert
#获取alert中的文本
a1=alert1.text
print(a1)
sleep(1)
#点击确定按钮
alert1.accept()

#点击第二个按钮
sleep(1)
button2=driver.find_element(By.XPATH,"//input[3]")
button2.click()
alert2=driver.switch_to.alert
print(alert2.text)
sleep(1)
alert2.accept()





