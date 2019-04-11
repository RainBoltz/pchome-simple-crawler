
import requests
import base64
import urllib.parse
from lxml import html
from pprint import pprint

class pchomeCrawler:
    def __init__(self):
        self.last_result = "<html><head></head><body><title>N/A</title></body></html>"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
        
    def search(self, raw_target: str):
        target = urllib.parse.quote(raw_target).encode('Big5')
        encoded_target = base64.urlsafe_b64encode(target).decode()
        url = 'https://www.pcstore.com.tw/adm/psearch.htm?store_k_word=%s&slt_k_option=1'%encoded_target
        raw_result = requests.get(url, headers=self.headers)
        raw_result.encoding = "Big5"
        self.last_result = raw_result.text
    
    def get_titles(self):
        web = html.fromstring(self.last_result)
        raw_titles = web.xpath("//div[@class='pic2t pic2t_bg']")
        output = []
        for this_raw_title in raw_titles:
            title = this_raw_title.xpath('a//text()')
            output.append(''.join(title))
        return output
        

if __name__ == "__main__":
    myCrawler = pchomeCrawler()
    
    while True:
        keyword = input("請輸入關鍵字：")
        
        myCrawler.search(keyword) #搜索
        titles = myCrawler.get_titles() #取得標題
        
        for title in titles:
            print(title)
        print('...共%2d項'%len(titles))
        print("-")
        
