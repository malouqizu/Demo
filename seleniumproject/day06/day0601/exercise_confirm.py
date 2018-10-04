from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="http://www.sahitest.com/demo/index.htm"
driver.get(base_url)
#定位超级链接
confirmlink=driver.find_element(By.LINK_TEXT,"Confirm Page")
confirmlink.click()
#定位按钮
sleep(1)
btn1=driver.find_element(By.XPATH,"//input[1]")
btn1.click()
#获得confirm对话框
confirm1=driver.switch_to.alert
sleep(1)
t1=confirm1.text
confirm1.accept()

#定位文本框
txt1=driver.find_element(By.XPATH,"//input[2]")
if txt1.get_attribute("value")=="oked":
    print("点击确定按钮")
    print("提示信息:",t1)
sleep(1)
btn1.click()
c1=driver.switch_to.alert
sleep(1)
c1.dismiss()
if txt1.get_attribute("value")=="canceled":
    print("点击取消按钮")



