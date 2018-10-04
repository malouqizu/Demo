from selenium.webdriver.common.by import By
#定位页面元素信息
findname=(By.XPATH,"//input[@name='username']")
findpassword=(By.XPATH, "//input[@name='passwords']")
findmale=(By.XPATH, "//input[@name='sex']")
findfemale=(By.XPATH, "//input[@name='sex'][2]")
findemail=(By.XPATH, "//input[@name='email']")
findprofession=(By.XPATH, "//select[@name='profession']")
findfilm=(By.XPATH, "//input[@name='film']")
findpainting=(By.XPATH, "//input[@name='painting']")
findcomments=(By.XPATH,"//textarea")
findsubmit=(By.XPATH, "//input[@name='submit']")