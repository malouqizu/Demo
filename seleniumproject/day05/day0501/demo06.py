from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
base_url="file:///E:/selenium/day05/day0501demo/demo04.html"
driver.get(base_url)

#标记存在某个子标记
h1=driver.find_element(By.XPATH,"//ul[lable]")

#标记中的子标记的文本值
h1=driver.find_element(By.XPATH,"//ul[li='历史']")

str1=h1.text
print(str1)
list1=list(str1)
print(list1)
list2=str1.split("\n")
print(list2)