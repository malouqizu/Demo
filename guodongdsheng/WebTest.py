#encoding:utf-8

import sys
import os
import time
import urllib
default_encoding = 'utf-8'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
'''
CLOASE_AFTER_TEST = False
GBK = "gbk"
UTF8 = "utf8"

def output(x):
    print encoding(x)

def resultMsg(x):
    if x == True:
        print 'pass'
    else:
        print '[X]not pass'


def checkresult(x):
    resultMsg(browser.is_text_present(x))

def testLogin(desc, username, password, result):
    output(desc)
    browser.fill('TPL_username',username.decode(UTF8))
    browser.fill('TPL_password',password.decode(UTF8))
    browser.find_by_value('登录').first.click()
    checkresult(result)


reload(sys)
sys.setdefaultencoding(UTF8)
encoding = lambda x: x.encode('gbk')
'''

if __name__=="__main__":
    reload(sys)
    sys.setdefaultencoding(default_encoding)
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "D:\\"}
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_experimental_option("prefs", prefs)

    chromedriver = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chrome_options=options)

    time.sleep(1)
    driver.maximize_window()
    driver.set_page_load_timeout(1000)
    driver.set_script_timeout(1000)

    time.sleep(1)
    # js = 'window.open("file:///D:/ide_tool_202/ide_tool/index.html#/");'
    # driver.execute_script(js)
    driver.get("file:///D:/ide_tool_202/ide_tool/index.html#/")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"main\"]/div[2]/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"action-list\"]/li/select").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"action-list\"]/li/select/option[5]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"coordinate\"]/input").send_keys("200,300")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"sdeapp\"]/div/input[1]").click()
    time.sleep(1)

    driver.find_element_by_xpath("//*[@id=\"button-Click-*\"]/input[2]").click()
    time.sleep(1)

    print "nihao"
    

    res =  driver.switch_to.alert.text
    urllib.urlretrieve(res, "click.xml")

    driver.quit()
    print "333333"

    #driver.switch_to_window(handles[1])
    #driver.switch_to.window(handles)

    # driver.find_element_by_tag_name("span").send_keys(Keys.CONTROL,"s")
    # time.sleep(1)
    # driver.find_element_by_tag_name("span").send_keys(Keys.ENTER)

    # ActionChains(driver).send_keys(Keys.CONTROL,"s").perform()
    # time.sleep(3)
    # ActionChains(driver).send_keys(Keys.ENTER).perform()


    #builder.move_by_offset(1201,186).click()
    #builder.move_by_offset(1201,186).click()
    #driver.find_element_by_class_name("wrapper").send_keys(Keys.CONTROL)
    #builder.send_keys(Keys.CONTROL).perform()
    #builder.key_down(Keys.CONTROL, 'M').perform()
    #driver.find_element_by_class_name("content").send_keys(Keys.F12)
    #imgList = driver.find_elements_by_tag_name("img")
    #driver.find_element_by_link_text()
    #driver.find_element_by_xpath("/html/body/footer/dl[2]/dd").click()


    '''
    driver.find_element_by_id('kw').send_keys('python')
    time.sleep(3)
    driver.find_element_by_id('su').click()
    time.sleep(3)
    '''
    '''
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    '''
    '''
    i=0
    while i< 8:
       driver.find_element_by_id("su").send_keys(Keys.DOWN)
       time.sleep(1)
       i+=1
    driver.find_element_by_link_text("Python_百度百科").click()
    '''


    #driver.close()
'''
   ie = PAMIE()
   ie.navigate("https://www.so.com/")
   ie.setTextBox("q","nihao")
   ie.clickButton("搜一下")
   ie.clickLink("你好")
'''