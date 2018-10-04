# _*_ coding:utf-8 _*_
import requests
import json

params = {'house_code': '106100872048'}
api='api/gethousequestionlist/'
rg = requests.get('http://test5-i.carpo.ke.com/'+api, params)
print(rg.raise_for_status())
print(rg.ok)
print(rg.encoding)
print(rg.url)
print(rg.headers)
print(rg.text)
print(rg.content)
print(rg.json())

headers={'token': '1014120001s'}
data={"query":"","qfs":[],"filters":{"and":[{"or":[{"field":"cityId","action":"match","value":320300}]}]},"fls":[],"sorts":[],"aggregations":[],"spatial":[],"hls":[],"page":0,"size":25}
rp=requests.post('http://10.33.108.46:12243/api/1014120001s/search', headers=headers, data=json.dumps(data, ensure_ascii=False))
#indent=4 将字符串打印成json格式
print(json.dumps(rp.json(),ensure_ascii=False,indent=4))









