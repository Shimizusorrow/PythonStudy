import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html

def get_page(url):
    html=url_open(url).decode('utf-8')
# html=response.read().decode('utf-8')

    a=html.find('current-comment-page')+23
    b=html.find(']',a)
    print(html)

    return  html[a:b]
    # print(html[a:b])

def find_imgs(page_url):
    html=url_open(page_url).decode('utf-8')
    img_addrs=[]

    a=html.find('img src=')
    while a!=-1:
        b=html.find('.jpg',a,a+255)
        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b=a+9
        a = html.find('img src=',b)
    # for each in img_addrs:
    #     print(each)
    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        try:
            with open(filename,'wb')as f:
                img=url_open("http:" + each)
                f.write(img)
        except:
            print(each)


def download_mm(folder='ooxx',pages=20):
    # 创建文件夹
    if not os._exists(folder):
        os.mkdir(folder)
    # 改变工作目录
    os.chdir(folder)

    url='http://jandan.net/ooxx/'

    # page_num=int(get_page(url))

    for i in range(pages,-1,-1):
        page_url=url + 'page-'+ str(i) + '#comments'
        try:
            img_addrs=find_imgs(page_url)
            print(img_addrs)
            save_imgs(folder,img_addrs)
            print(page_url)
        except:
            print(page_url)
if __name__=='__main__':
    download_mm()