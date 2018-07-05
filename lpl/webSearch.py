import requests
from lxml import etree
import prettytable as pt
from bs4 import BeautifulSoup
from termcolor import colored

searchUrl = "https://www.baidu.com/s?wd=lol {}"

headers = {
    'Host': 'www.baidu.com',
    'Referer': 'http://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}

# 搜索功能
def search(keyword):
    tb = pt.PrettyTable()
    tb.field_names = [colored('id', 'blue'), colored('标题', 'blue')]
    response = requests.get(searchUrl. format(keyword), headers=headers)

    for k, sel in enumerate(BeautifulSoup(response.text, 'lxml').select("div[class='result c-container ']")):
        tb.add_row([k, colored(sel.h3.a.get_text(), 'red')])
        tb.add_row(['', colored(sel.h3.a.attrs['href'], 'yellow')])
        tb.add_row(['', ''])

    tb.align = 'l'
    print(tb)

if __name__ == "__main__":
    search(keyword = '')