from selenium import webdriver
driver = webdriver.Firefox()
base_url = "file:///E:/selenium/day03/04-testing/testing.html"
driver.get(base_url)
driver.find_element_by_id("username").send_keys("1001")
driver.find_element_by_id("password").send_keys("testing")


driver.find_element_by_id("username")
