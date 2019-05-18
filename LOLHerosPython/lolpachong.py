import requests
import re
import json

def getLoLImages():

    url_js = 'http://lol.qq.com/biz/hero/champion.js'

    html = requests.get(url_js).text

    req = r'"keys":(.*?),"data"'

    list_js = re.findall(req,html)

    
    
    dict_js = json.loads(list_js[0])

    pic_list = []
    for hero_id in dict_js:
        for i in range(20):
            num = str(i)
            if len(num) == 1:  
                hero_number = '00' + num
            elif len(num) == 2:
                hero_number = '0' + num
            numstr = hero_id + hero_number
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big' + numstr + '.jpg'
            pic_list.append(url)

    list_filepath = []

    path = r'C:\Users\34586\Desktop\PythonCode\LOLPic\\'

    for name in dict_js.values():
        
        for i in range(20):
            file_path = path + name + str(i) + '.jpg'
            list_filepath.append(file_path)


    n = 0
    for picurl in pic_list:
        res = requests.get(picurl)
        n = n + 1
        if res.status_code == 200:
            print('正在下载%s'%list_filepath[n])
            
            with open(list_filepath[n],'wb') as f:
                f. write(res.content)
    

if __name__ == '__main__':
    getLoLImages()