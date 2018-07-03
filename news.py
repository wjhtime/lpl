import requests
import json
import prettytable as pt
import time
from termcolor import colored, cprint


def news():
    newsUrl = "http://lpl.qq.com/web201612/data/LOL_NEWMATCH_FIR_PAGE_TEAM_NEWS_INFO.js"
    tb = pt.PrettyTable()
    tb.field_names = ['标题', '摘要', '时间']
    tb.sortby = '时间'
    response = requests.get(newsUrl)
    # 截取字符串，获取json内容
    news = response.text[response.text.find('=')+1:-1]
    jsonObject = json.loads(news)

    for i in range(2):
        for news in jsonObject['msg'].get('{}'.format(i+1)):
            tb.add_row([news['Title'], news['SubTitle'][0:60], news['indexDate']])
    tb.align = 'l'

    print(tb)

