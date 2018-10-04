from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
driver=webdriver.Firefox()

#操作frame1
def frame1_play():
    name=driver.find_element(By.XPATH,".//*[@id='username']")
    name.send_keys("Jack")
    password=driver.find_element(By.XPATH,".//*[@id='password']")
    password.send_keys("1234")
    comments=driver.find_element(By.XPATH,".//*[@id='comments']")
    comments.send_keys("软件测试")
    submit=driver.find_element(By.XPATH,".//*[@id='submit']")
    sleep(1)
    submit.click()
    print("在frame1中操作完毕！")

#操作frame2
def frame2_play():
    female=driver.find_element(By.XPATH,".//*[@id='female']")
    female.click()
    wangyin=driver.find_element(By.XPATH,".//*[@id='wangyin']")
    wangyin.click()
    music=driver.find_element(By.XPATH,".//*[@id='music']")
    music.click()
    reading=driver.find_element(By.XPATH,".//*[@id='reading']")
    reading.click()
    sleep(1)
    print("在frame2中操作完毕！")

if __name__=="__main__":
    #main3.html
    base_url="file:///E:/selenium/day06/day0602demo/frame/main3.html"
    driver.get(base_url)
    #切换到frame1,使用Xpath定位后切换
    #driver.switch_to.frame(0)
    frame1=driver.find_element(By.XPATH,"//iframe[1]")
    driver.switch_to.frame(frame1)
    #调用frame1操作函数
    frame1_play()
    #切换回主窗口
    #driver.switch_to.parent_frame()
    driver.switch_to.default_content()

    #切换到frame2，使用xpath定位后切换
    #driver.switch_to.frame(1)
    frame2=driver.find_element(By.XPATH,"//iframe[2]")
    driver.switch_to.frame(frame2)
    #调用frame2操作函数
    frame2_play()

    '''
     #main1.html
    base_url="file:///E:/selenium/day06/day0602demo/frame/main1.html"
    driver.get(base_url)
    #切换到frame1,使用id定位
    driver.switch_to.frame("f1")
    #调用frame1操作函数
    frame1_play()
    #切换回主窗口
    driver.switch_to.parent_frame()
    #切换到frame2，使用name定位
    driver.switch_to.frame("frame2")
    #调用frame2操作函数
    frame2_play()
    '''
    '''
    #main2.html
    base_url="file:///E:/selenium/day06/day0602demo/frame/main2.html"
    driver.get(base_url)
    #切换到frame1,使用索引号定位
    driver.switch_to.frame(0)
    #调用frame1操作函数
    frame1_play()
    #切换回主窗口
    #driver.switch_to.parent_frame()
    driver.switch_to.default_content()

    #切换到frame2，使用索引号定位
    driver.switch_to.frame(1)
    #调用frame2操作函数
    frame2_play()
    
    
    '''
