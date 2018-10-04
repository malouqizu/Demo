from day08.day0802.demo01_v2.demo01_v2_locator import findname,findpassword,findmale,findfemale,findemail
from day08.day0802.demo01_v2.demo01_v2_locator import findprofession,findfilm,findpainting,findcomments,findsubmit
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
        self.name = self.driver.find_element(*findname)
        self.name.send_keys(n)

    #输入密码
    def type_password(self,p):
        self.password = self.driver.find_element(*findpassword)
        self.password.send_keys(p)

    #点击性别男
    def click_male(self):
        self.male = self.driver.find_element(*findmale)
        self.male.click()

    #点击性别女
    def click_female(self):
        self.female = self.driver.find_element(*findfemale)
        self.female.click()

    #输入邮箱
    def type_email(self,e):
        self.email = self.driver.find_element(*findemail)
        self.email.send_keys(e)

    #选择专业
    def select_profession(self,t):
        self.profession = self.driver.find_element(*findprofession)
        self.p1 = Select(self.profession)
        self.p1.select_by_visible_text(t)

    #点击影视娱乐
    def click_film(self):
        self.film = self.driver.find_element(*findfilm)
        if self.film.is_selected() == False:
            self.film.click()

    #点击绘画书法
    def click_painting(self):
        self.painting = self.driver.find_element(*findpainting)
        if self.painting.is_selected() == False:
            self.painting.click()
    #输入留言
    def type_comments(self,c):
        self.comments=self.driver.find_element(*findcomments)
        self.comments.send_keys(c)
    #点击提交
    def click_submit(self):
        self.submit = self.driver.find_element(*findsubmit)
        self.submit.click()
    #关闭浏览器
    def bye_bye(self):
        self.driver.quit()