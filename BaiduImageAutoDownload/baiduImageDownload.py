import os
import requests
import re

class BadiuImage():
    def __init__(self, word,start_url):
        self.word = word
        self.start_url = start_url + self.word

    def tuPian(self,word):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }

        r = requests.get(self.start_url,headers)
        ret = r.content.decode()
     
        # "objURL":"http://image.zp365.com/news/images/q1/169399028306124.jpg",
        result = re.findall('"objURL":"(.*?)",', ret)

        for i in result:
            end = re.search('(.jpg|.png|.jpeg|.gif)$', i) 
            if end == None:
                i = i + '.jpg'
            try:
                with open('./' + word + '/{}'.format(i[-10:]), 'wb') as f:
                    img = requests.get(i, headers=headers, timeout=3)
                    f.write(img.content) 
                    print('正在下载第%d张图片' % (result.index(i) + 1))
            except Exception:
                pass


if __name__ == '__main__':
    word = input('请输入你想要的图片：')
    start_url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&ctd=1535722081191%5E00_994X751&word="
    downloads = BadiuImage(word,start_url)
    if not os.path.exists(word):
        os.mkdir(word)  
    downloads.tuPian(word)
