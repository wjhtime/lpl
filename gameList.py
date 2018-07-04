import requests
import json
import prettytable as pt
import time
from termcolor import colored, cprint

# 比赛列表
def game():
    gameUrl = "http://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_HOMEPAGE_BMATCH_LIST.js"
    tb = pt.PrettyTable()
    tb.field_names = [colored('时间','red'), colored('比赛', 'red'), colored('比赛类型','red'), colored('赛区','red'), colored('获胜方', 'red'), colored('队伍A积分', 'red'), colored('队伍B积分', 'red')]
    # tb.sortby = colored('时间','blue')
    # tb.reversesort = True
    response = requests.get(gameUrl)
    jsonObject = json.loads(response.text)
    separate = False
    for game in jsonObject['msg']:
        teamsTwo = game['bMatchName'].split(' vs ')
        # 将结束的比赛分隔
        # ts = time.strptime(game['MatchDate'], "%Y-%m-%d %H:%M:%S")
        # if time.time() > time.mktime(ts) and separate == False:
        #     separate = True
        #     tb.add_row(['-', '-', '-', '-', '-', '-', '-'])
        # 获胜队伍
        winTeam = colored(teamsTwo[int(game['MatchWin']) - 1], 'yellow') if int(game['MatchWin']) >= 1 else '即将开始'
        tb.add_row([colored(game['MatchDate'], 'cyan'), colored(game['bMatchName'], 'cyan'), colored(game['GameName'], 'cyan'), colored(game['GameTypeName'], 'cyan'), colored(winTeam, 'cyan'), colored(game['ScoreA'], 'cyan'), colored(game['ScoreA'], 'cyan')])

    tb.align = 'l'
    print(tb)

