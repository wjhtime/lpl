import requests
import json
import prettytable as pt
import time
from termcolor import colored, cprint

# 积分
def score():
    gameUrl = "http://lpl.qq.com/web201612/data/LOL_MATCH2_GAME_95_1_TEAM_SCORE_TOP_50.js"
    tb = pt.PrettyTable()
    tb.field_names = [colored('队伍ID', 'red'), colored('队伍名称', 'red'), colored('排位','red'), colored('积分','red')]
    response = requests.get(gameUrl)
    jsonObject = json.loads(response.text)
    for game in jsonObject['msg']:
        tb.add_row([colored(game['TeamId'], 'cyan'), colored(game['TeamName'], 'cyan'), colored(game['Rank'], 'cyan'), colored(game['Score'], 'cyan')])

    tb.align = 'l'
    print(tb)

if __name__ == "__main__":
    score()