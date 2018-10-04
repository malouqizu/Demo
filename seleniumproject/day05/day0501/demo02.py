from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day05/day0501demo/demo02.html"
driver.get(base_url)

#使用绝对路径xpath定位方式
#myname=driver.find_element(By.XPATH,"/html/body/form/input[@value='姓名']")
#mypassword=driver.find_element(By.XPATH,"/html/body/form/input[@id='password']")
#mycomments=driver.find_element(By.XPATH,"/html/body/form/textarea")
#mysubmit=driver.find_element(By.XPATH,"/html/body/form/input[@type='submit']")

#使用相对路径xpath定位方式
#使用标记的属性名=属性值方式进行筛选说明
#myname=driver.find_element(By.XPATH,"//input[@value='姓名']")
#mypassword=driver.find_element(By.XPATH,"//input[@id='password']")
#mycomments=driver.find_element(By.XPATH,"//textarea")
#mysubmit=driver.find_element(By.XPATH,"//input[@type='submit']")


#使用标记的索引号进行筛选说明
myname=driver.find_element(By.XPATH,"//input[1]")
mypassword=driver.find_element(By.XPATH,"//input[2]")
mycomments=driver.find_element(By.XPATH,"//textarea")
mysubmit=driver.find_element(By.XPATH,"//input[3]")

myname.clear()
myname.send_keys("aaa")
mypassword.clear()
mypassword.send_keys("abcd")
mycomments.clear()
mycomments.send_keys("你好")
sleep(2)
mysubmit.click()
sleep(2)
driver.quit()

