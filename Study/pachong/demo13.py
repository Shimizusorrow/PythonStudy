import urllib.request
import urllib.parse
import json
while True:
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    context=input("请输入待翻译的内容:")
    if context=='q':
        break;
    # head={}
    # head['User-A']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

    data={}
    data['i']=context
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

    req=urllib.request.Request(url,data)
    req.add_header('User-A','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')

    response=urllib.request.urlopen(req)
    html =response.read().decode('utf-8')

    # print(html)
    target=json.loads(html)

    # print(json.loads(html))
    print(target['translateResult'][0][0]['tgt'])

    # print(req.headers)
