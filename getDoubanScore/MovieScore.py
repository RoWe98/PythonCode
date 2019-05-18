import lxml.html
import requests
import time
from lxml import etree

class MovieScore:
    def __init__(self,movieurl,word):
        self.movieurlBase = movieurl
        self.word = word
        self.movieurl = self.movieurlBase + self.word

    def getItemInfo(self):
        print('地址为: '+self.movieurl)
        r = requests.get(self.movieurl)
        html = etree.HTML(r.text)
        info = html.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/div/span[2]/text()')
        print('评分为: '+info[0])


if __name__=="__main__":
    
    movieUrlBase = "https://www.douban.com/search?cat=1002&q="

    flag = 1
    while flag != 0:
        print("请输入电影的名称,退出输入q  :",end = "")
        word = str(input())
        if word != 'q':
            movie = MovieScore(movieUrlBase,word)
            movie.getItemInfo()
        else:
            flag = 0
            print("谢谢使用！")
            time.sleep(3)
