#coding=utf-8
import urllib
import re
import time


def getHtml(url):
    pape = urllib.urlopen(url)
    html = pape.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imgList = re.findall(imgre,html)
    x= 0
    for img in imgList:
        try:
            urllib.urlretrieve(img, "./pic/%s.jpg" %x)
        except Exception as e:
            print e
        time.sleep(3)
        x+=1
        print x
    return imgList

if __name__=="__main__":
    html = getHtml("http://tieba.baidu.com/p/2460150866")
    print getImg(html)


