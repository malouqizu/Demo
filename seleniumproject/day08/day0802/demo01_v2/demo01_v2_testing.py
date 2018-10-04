from selenium import webdriver
from day08.day0802.demo01_v2.demo01_v2_register import MyComments
from time import sleep
#导入csv，处理csv格式的文件
import csv
if __name__=="__main__":
    driver = webdriver.Firefox()
    #打开页面
    my_url="file:///E:/selenium/day08/day0801demo/demo01.html"
    test=MyComments(driver)
    test.open(my_url)
    # 测试数据
    f=open('E:/selenium/day08/day0801demo/mydata2.csv','r')
    data=csv.reader(f)

    for mydata in data:
        print(mydata)
        test.type_name(mydata[0])
        test.type_password(mydata[1])
        test.click_male()
        test.type_email(mydata[2])
        test.select_profession(mydata[3])
        test.click_film()
        test.click_painting()
        test.type_comments(mydata[4])
        sleep(1)
        test.click_submit()

    test.bye_bye()
