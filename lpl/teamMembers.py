import requests
import json
import prettytable as pt

memberUrl = "http://lpl.qq.com/web201612/data/LOL_MATCH2_TEAM_MEMBER_LIST.js"

# 队员
def searchMember():
    response = requests.get(memberUrl)
    tb = pt.PrettyTable()
    tb.field_names = ['id', '昵称', '姓名', '队伍内昵称', '头像链接']
    members = response.text[response.text.find('=')+1:-1]
    jsonObject = json.loads(members)
    for k, member in jsonObject['msg'].items():
        tb.add_row([member['MemberId'], member['NickName'], member['RealName'], member['GameName'], member['UserIcon']])

    tb.align = 'l'
    print(tb)

if __name__ == "__main__":
    searchMember()