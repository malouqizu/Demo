#coding:utf-8
import urllib
from urllib import quote
from urllib import unquote
import urllib2
import sys
import json

default_encoding = 'utf-8'
reload(sys)
sys.setdefaultencoding(default_encoding)

targetWord = sys.argv[1]
targetWord = targetWord.replace(" ","%20")
url = "https://openapi.baidu.com/oauth/2.0/token?"
grant_type="grant_type=client_credentials&"
client_id="client_id=gQNLHflZmE3vrEEYxaGrc86z&"
client_secret="client_secret=8BE67BO6NPaMSTAElqfQp9uUML30L4L7"

TTSUrl = url+grant_type+client_id+client_secret
print TTSUrl
try:
    req = urllib2.Request(TTSUrl)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
except urllib2.HTTPError as http_error:
    print http_error
myJson = json.loads(res)
print myJson["access_token"]
token = myJson["access_token"]

wavUrl = "http://tsn.baidu.com/text2audio?tex="+targetWord+"&lan=zh&cuid=5679929&ctp=1&tok="+token
print wavUrl
try:
    req = urllib2.Request(wavUrl)
    res_data = urllib2.urlopen(req)
    ens =  res_data.read()
except urllib2.HTTPError as http_error:
    print http_error
targetWord = targetWord.replace("%20"," ")
with open(targetWord+".wav", "wb") as code:
    code.write(ens)
print "done"