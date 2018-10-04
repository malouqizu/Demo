#coding:utf-8
import urllib
import urllib2
import sys
import json

def sendPostHttp(sph_url, sph_dictPara):
    try:
        req = urllib2.Request(sph_url, urllib.urlencode(sph_dictPara))
        res_data = urllib2.urlopen(req)
        return res_data.read()
    except urllib2.HTTPError as http_error:
        print http_error

if __name__=="__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")
    if len(sys.argv)<=1:
        print "too few argument"
        exit(-1)

    urlForToken = "https://openapi.baidu.com/oauth/2.0/token?"
    paraDataForToken={
              "grant_type":"client_credentials",
              "client_id":"gQNLHflZmE3vrEEYxaGrc86z",
              "client_secret":"8BE67BO6NPaMSTAElqfQp9uUML30L4L7"
              }
    res = sendPostHttp(urlForToken,paraDataForToken)
    myJson = json.loads(res)
    token = myJson["access_token"]

    targetWord = sys.argv[1]
    paraDataForWav = {
        "tex": targetWord,
        "lan": "zh",
        "cuid": "5679929",
        "ctp": "1",
        "tok": token,
        "per": "0",#0：女声，1：男声
        "spd": "5",#0~9：语速
        "pit": "5",#0~9：语调
        "vol": "5"#0~9：音量
    }
    wavUrl = "http://tsn.baidu.com/text2audio?"
    #这句话将打印全部的http请求
    #print wavUrl+urllib.urlencode(paraDataForWav)
    ens = sendPostHttp(wavUrl, paraDataForWav)
    targetWord = targetWord.replace(" ", "_")
    with open(targetWord + ".wav", "wb") as code:
        code.write(ens)
    print "done ",targetWord,".wav"

