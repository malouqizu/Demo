from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Firefox()

#打开浏览器
def open(url):
    base_url=url
    driver.get(base_url)

#操作页面函数mycase1
def mycase1():
    name = driver.find_element(By.XPATH, "//input[@name='username']")
    name.send_keys("张晓明")
    password = driver.find_element(By.XPATH, "//input[@name='passwords']")
    password.send_keys("123456")
    male = driver.find_element(By.XPATH, "//input[@name='sex']")
    male.click()
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("xiaoming@126.com")
    profession = driver.find_element(By.XPATH, "//select[@name='profession']")
    p1 = Select(profession)
    p1.select_by_visible_text("法律相关")
    film = driver.find_element(By.XPATH, "//input[@name='film']")
    if film.is_selected() == False:
        film.click()
    painting = driver.find_element(By.XPATH, "//input[@name='painting']")
    if painting.is_selected() == False:
        painting.click()
    comments=driver.find_element(By.XPATH,"//textarea")
    comments.send_keys("软件测试工程师！")
    sleep(1)
    submit = driver.find_element(By.XPATH, "//input[@name='submit']")
    submit.click()

#关闭浏览器
def bye_bye():
    driver.quit()

if __name__=="__main__":
    #打开页面
    my_url="file:///E:/selenium/day08/day0801demo/demo01.html"
    open(my_url)
    mycase1()
    bye_bye()
