
import requests
import time
import re
import threading
import os
import chardet   #需要导入这个模块，检测编码格式
from urllib import request


print(os.getcwd())

def img_download(url, store_path):
    filename = url.split("/")[-1]
    
    filepath = os.path.join(store_path, filename)
    
    file_data = requests.get(url, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)

class spider91():
    def run(self, page_url):
        self.spider(url=page_url)

    def spider(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',}
        # 伪造http头部
        r = requests.get(url=url, headers=headers)
        html = r.content
        encode_type = chardet.detect(html)  
        html = html.decode(encode_type['encoding']) #进行相应解码，赋给原标识符（变量）
        
        #print(html)
        if r.status_code != 404:
            # 创建标题名的文件夹
            name91 = re.findall('<h1>(.*?)</h1>', html)
            fileName =  'img/'+name91[0]
            
            if not os.path.exists(fileName):
                os.makedirs(fileName)

        img_urls1 = re.findall('file="attachments/(.*?)"', html)
        img_urls2 = re.findall('attachments/(.*?)"', html)
        img_urls = img_urls1+img_urls2
        for img_url in img_urls:
            # 获取真实图片地址
            img_url = 'http://f1113.wonderfulday30.live/attachments'+img_url
            print(img_url)
            img_download(img_url, fileName)
        #time.sleep(2)


aaaa = spider91()

def main():
    for i in range(403605, 403706):  #此处更改爬取的范围
        aaaa.run('http://f1113.wonderfulday30.live/viewthread.php?tid='+str(i))


if __name__ == '__main__':
    main()



