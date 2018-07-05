import requests
from lxml import etree
import prettytable as pt

searchUrl = "https://www.baidu.com/s?wd=lol {}"

headers = {
    'Host': 'www.baidu.com',
    'Referer': 'http://www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}

def search(keyword):
    tb = pt.PrettyTable()
    tb.field_names = ['id', '标题']
    response = requests.get(searchUrl. format(keyword), headers=headers)
    for k, sel in enumerate(etree.HTML(response.text).xpath("//div[@class='result c-container ']")):
        tb.add_row([k, sel.xpath("h3/a/text()")[0]])
        tb.add_row(['', sel.xpath("h3/a/@href")[0]])
        tb.add_row(['', ''])

    tb.align = 'l'
    print(tb)

if __name__ == "__main__":
    search(keyword = '')