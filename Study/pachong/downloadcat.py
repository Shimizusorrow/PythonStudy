import urllib.request
# 下载一张猫的图片
req=urllib.request.Request("http://placekitten.com/g/1080/600")
response=urllib.request.urlopen(req)

cat_img=response.read()

# with open('cat_500_600.jpg','wb')as f:
#     f.write(cat_img)
print(response.geturl())
print(response.info())
print(response.getcode())