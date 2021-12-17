import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
list = []
url_List = []
server = "http://i.258zw.com/"
def get_title():
    for url in url_List:
        req = requests.get(url)
        bs = BeautifulSoup(req.content,'lxml')
        chapters = bs.find('ul',class_ = 'chapter')
        chapters = chapters.find_all('a')
        for i in chapters:
            chapter_name = i.text
            chapter_name = chapter_name.replace('\r\n','')
            chapter_url = server+i.get('href')
            list.append([chapter_name,chapter_url])
    print(list)
def get_content(url):
    req = requests.get(url)
    html = req.text.encode('iso-8859-1') # 以txt形式存储
    bs = BeautifulSoup(html, 'lxml')  #
    texts = bs.find('div', id='nr1')  # 筛选id=content的div
    content = texts.text.strip().replace('258中文阅读网www.2 5 8zw.com','').replace('    ',' ').split('\xa0' * 1) # 去除换行和缩进
    return content

if __name__ == '__main__':
    url = "http://i.258zw.com/wapbook-1852_"
    for i in range(1,211):
        url_List.append(url+'%d'%i)
    print(url_List)
    get_title()
    for i in tqdm(list):
        content = get_content(i[1])
        with open('test.txt','a',encoding='utf-8') as f: #保存文件
            f.write(i[0])
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
