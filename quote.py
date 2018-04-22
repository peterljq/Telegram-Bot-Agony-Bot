#十年计科两茫茫 小bug 坑千行
#注释一下 否则今晚写的明早起来就看不懂了
import requests
from bs4 import BeautifulSoup

class Quote(object):
    def getHTML(self, url):
        r = requests.get(url)
        return r.content


#import大法好，万事不发愁。并定义提取网页HTML内容的函数。

    def parseHTML(self, html):
        soup = BeautifulSoup(html,'html.parser')
        body = soup.body
#以下进入爬虫检索网页阶段，高度依靠网页编写者的良心。
        layer_one = body.find('strong',attrs={'style':'color: #0b5394;'})
        layer_two = body.find('div',attrs={'style':'text-align: center; margin-top: -18px; margin-bottom: 18px;'})
        writer = layer_two.get_text()
        quote = layer_one.get_text()
        return writer, quote
#8.16：睡觉前灵光一现，完善函数：第二种方法：直接爬取layer_two所有子项的文字（包括内容及作者），而且不涉及具体地址，可以长久发展更新。
#至此函数定义结束

quote = Quote()
URL = 'http://www.dailyenglishquote.com'
html = quote.getHTML(URL)
writer, quote = quote.parseHTML(html)
