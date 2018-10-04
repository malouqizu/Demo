from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class MyComments():
    #构造函数
    def __init__(self,driver):
        self.driver=driver

    #打开浏览器
    def open(self,url):
        base_url=url
        self.driver.get(base_url)
    #输入姓名
    def type_name(self,n):
        name = self.driver.find_element(By.XPATH, "//input[@name='username']")
        name.send_keys(n)

    #输入密码
    def type_password(self,p):
        password = self.driver.find_element(By.XPATH, "//input[@name='passwords']")
        password.send_keys(p)

    #点击性别男
    def click_male(self):
        male = self.driver.find_element(By.XPATH, "//input[@name='sex']")
        male.click()

    #点击性别女
    def click_female(self):
        female = self.driver.find_element(By.XPATH, "//input[@name='sex'][2]")
        female.click()

    #输入邮箱
    def type_email(self,e):
        email = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email.send_keys(e)

    #选择专业
    def select_profession(self,t):
        profession = self.driver.find_element(By.XPATH, "//select[@name='profession']")
        p1 = Select(profession)
        p1.select_by_visible_text(t)

    #点击影视娱乐
    def click_film(self):
        film = self.driver.find_element(By.XPATH, "//input[@name='film']")
        if film.is_selected() == False:
            film.click()

    #点击绘画书法
    def click_painting(self):
        painting = self.driver.find_element(By.XPATH, "//input[@name='painting']")
        if painting.is_selected() == False:
            painting.click()
    #输入留言
    def type_comments(self,c):
        comments=self.driver.find_element(By.XPATH,"//textarea")
        comments.send_keys(c)
    #点击提交
    def click_submit(self):
        submit = self.driver.find_element(By.XPATH, "//input[@name='submit']")
        submit.click()
    #关闭浏览器
    def bye_bye(self):
        self.driver.quit()