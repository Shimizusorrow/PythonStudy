import urllib.request

url='http://www.whatismyip.com/'

proxy_support=urllib.request.ProxyHandler({'http':'119.6.144.73:81'})

opener=urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)

html=response.read().decode('utf-8')
print(html)
