from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day08/day0801demo/demo01.html"
driver.get(base_url)
#定位信息
name=driver.find_element(By.XPATH,"//input[@name='username']")
password=driver.find_element(By.XPATH,"//input[@name='passwords']")
male=driver.find_element(By.XPATH,"//input[@name='sex']")
female=driver.find_element(By.XPATH,"//input[@name='sex'][2]")
email=driver.find_element(By.XPATH,"//input[@name='email']")
profession=driver.find_element(By.XPATH,"//select[@name='profession']")
computer=driver.find_element(By.XPATH,"//input[@name='computer']")
film=driver.find_element(By.XPATH,"//input[@name='film']")
chess=driver.find_element(By.XPATH,"//input[@name='chess']")
read=driver.find_element(By.XPATH,"//input[@name='read']")
food=driver.find_element(By.XPATH,"//input[@name='food']")
painting=driver.find_element(By.XPATH,"//input[@name='painting']")
comments=driver.find_element(By.XPATH,"//textarea")
submit=driver.find_element(By.XPATH,"//input[@name='submit']")
#测试用例
name.send_keys("张晓明")
password.send_keys("123456")
male.click()
email.send_keys("xiaoming@126.com")
p1=Select(profession)
p1.select_by_visible_text("法律相关")
if film.is_selected()==False:
    film.click()
if painting.is_selected()==False:
    painting.click()
comments.send_keys("软件测试工程师！")
sleep(1)
submit.click()
driver.quit()








