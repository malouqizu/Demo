from selenium import webdriver
from selenium.webdriver.common.by import By
#导入NoSuchElementException异常类
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day06/day0602demo/demo01.html"

#设置implicitly等待
driver.implicitly_wait(10)
driver.get(base_url)
#在try-except结构中定位页面元素并操作
try:
    #定位页面元素并操作
    username=driver.find_element(By.XPATH,"//input[1]")
    password=driver.find_element(By.XPATH,"//input[22]")
    comments=driver.find_element(By.XPATH,"//textarea")
    submit=driver.find_element(By.XPATH,"//input[3]")
    username.send_keys("aaa")
    password.send_keys("bbb")
    comments.send_keys("ccc")
    submit.click()
    print("页面操作正常完成")
except NoSuchElementException as e:
    print("已经等待10秒钟时间")
    print(e)
finally:
    print("程序退出")
    driver.quit()
