import urllib.request
import urllib.parse
import json
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

data={}
data['i']=input("请输入要翻译的英文")
# data['i']='I love you!'
data['type']='AUTO'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='15596168166136'
data['sign']='239be85d0457f3e420562377e74d5c84'
data['ts']='1559616816613'
data['bv']='f4d62a2579ebb44874d7ef93ba47e822'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_REALTlME'
data=urllib.parse.urlencode(data).encode('utf-8')

response=urllib.request.urlopen(url,data)
html =response.read().decode('utf-8')

# print(html)
target=json.loads(html)

# print(json.loads(html))
print(target['translateResult'][0][0]['tgt'])
