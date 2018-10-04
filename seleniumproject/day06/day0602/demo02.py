from selenium import webdriver
from selenium.webdriver.common.by import By
#步骤1：导入WebDriverWait类和expected_conditons模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day06/day0602demo/demo01.html"
driver.get(base_url)

#步骤2：实例化WebDriverWait类
w1=WebDriverWait(driver,10,1)

#步骤3：对页面元素进行定位并操作
#姓名文本框
#(1)调用expected_conditions模块的方法判断元素是否存在
username_locator=(By.XPATH,".//*[@id='username']")
username=expected_conditions.presence_of_element_located(username_locator)
#username=expected_conditions.presence_of_element_located((By.XPATH,".//*[@id='username']"))
#（2）调用WebDriverWait类中的函数进行等待
username=w1.until(username)
#（3）操作页面元素
username.send_keys("张三")

#密码
password_locator=(By.XPATH,".//*[@id='password']")
password=expected_conditions.presence_of_element_located(password_locator)
password=w1.until(password)
password.send_keys("1234")
#留言
comment_locator=(By.XPATH,".//*[@id='comments']")
comments=expected_conditions.presence_of_element_located(comment_locator)
comments=w1.until(comments)
comments.send_keys("软件测试！")
#提交按钮
submit_locator=(By.XPATH,".//*[@id='submit']")
submit=expected_conditions.presence_of_element_located(submit_locator)
submit=w1.until(submit)
submit.click()





