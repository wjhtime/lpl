import requests
import json
import prettytable as pt
import time
from termcolor import colored, cprint

# 新闻
def news(teamId):
    newsUrl = "http://lpl.qq.com/web201612/data/LOL_NEWMATCH_FIR_PAGE_TEAM_NEWS_INFO.js"
    tb = pt.PrettyTable()
    tb.field_names = [colored('标题','red'), colored('摘要', 'red'), colored('时间', 'red')]
    # tb.sortby = '时间'
    response = requests.get(newsUrl)
    # 截取字符串，获取json内容
    news = response.text[response.text.find('=')+1:-1]
    jsonObject = json.loads(news)

    for news in jsonObject['msg'].get(str(teamId)):
        tb.add_row([colored(news['Title'], 'cyan'), colored(news['SubTitle'][:60], 'cyan'), colored(news['indexDate'], 'cyan')])
        tb.add_row([colored('链接', 'red'),colored(news['sUrl'], 'yellow'), ''])

    tb.align = 'l'

    print(tb)

