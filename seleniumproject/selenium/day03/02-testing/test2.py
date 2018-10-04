from selenium import webdriver
driver = webdriver.Firefox()
base_url = "file:///E:/02-seleniumwithpython/day02/testing.html"
driver.get(base_url)
driver.find_element_by_id("username").send_keys("1001")
driver.find_element_by_id("password").send_keys("testing")
