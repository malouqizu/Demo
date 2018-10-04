from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="http://www.sahitest.com/demo/index.htm"
driver.get(base_url)
#获得超级链接并点击
sleep(1)
promptlink=driver.find_element(By.LINK_TEXT,"Prompt Page")
promptlink.click()
#点击按钮
sleep(1)
btn1=driver.find_element(By.XPATH,"//input[1]")
btn1.click()
#获得prompt对象
prompt1=driver.switch_to.alert
#获得prompt中的文本
t1=prompt1.text
#向prompt中输入数据
prompt1.send_keys("张三")
#点击确定按钮
prompt1.accept()
#定位页面文本框
txt1=driver.find_element(By.XPATH,"//input[2]")
if txt1.get_attribute("value")=="张三":
    print("点击确定按钮")
    print("提示信息：",t1)







