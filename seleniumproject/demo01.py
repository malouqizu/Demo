from selenium import webdriver
import os
import time

req_url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=%E9%B2%9C%E8%8A%B1"
browser=webdriver.Firefox()
time.sleep(10)
browser.get(req_url)
all_ads_li = browser.find_elements_by_css_selector('#e_idea_pp li')
ads_num_current = len(all_ads_li)
print(ads_num_current)
