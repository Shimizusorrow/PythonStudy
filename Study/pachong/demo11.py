# 爬虫
import urllib.request

response=urllib.request.urlopen("http://www.baidu.com")
print(response)
html=response.read()
html=html.decode("utf-8")
print(html)
