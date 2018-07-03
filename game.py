import requests
import json
import prettytable as pt
import time
from termcolor import colored, cprint


def game():
    gameUrl = "http://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_HOMEPAGE_BMATCH_LIST.js"
    tb = pt.PrettyTable()
    tb.field_names = [colored('时间','red'), colored('比赛', 'red'), colored('比赛类型','red'), colored('赛区','red')]
    # tb.sortby = colored('时间','blue')
    # tb.reversesort = True
    response = requests.get(gameUrl)
    jsonObject = json.loads(response.text)
    for game in jsonObject['msg']:
        tb.add_row([colored(game['MatchDate'], 'cyan'), colored(game['bMatchName'], 'cyan'), colored(game['GameName'], 'cyan'), colored(game['GameTypeName'], 'cyan')])

    tb.align = 'l'
    print(tb)

