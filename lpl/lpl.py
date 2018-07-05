import gameList, teamScore, gameNews, webSearch, teamMembers
import click

app_desc = """
                             )`·.                                                                             )`·.   
                  /(      .·´    (                                                                 /(      .·´    (   
          )\      )  `·._):::.    )'            (`·.               )\                     )\      )  `·._):::.    )'
    )\ .·´ .:`·.(:;;  --  ' '\:. :(                )  `·.   .·´( .·´  (     /(        )\ .·´ .:`·.(:;;  --  ' '\:. :(   
.·´  (,): --  ' '              \:·´        .·´( .·´:..::(,(::--   '\::.`·._) `·. .·´  (,): --  ' '              \:·´   
):.::/\                ,..::´/            );; :--  ' '               \::....:::::)):.::/\                ,..::´/       
`·:/::::\...:´/       /:::::/          .·´/\                ,...     ¯¯¯`·:·´ `·:/::::\...:´/       /:::::/        
   \::::/::::/      /;:::-'     '       )/:::'\...:´/       /:::::::::::/     /   '   \::::/::::/      /;:::-'     '     
     \/;::-'/      /              '      \:::/::::/       /;;::;;´-··´´     /          \/;::-'/      /              '   
          /      /                       '\/;::-'/               ,...::::´/                 /      /                   
        '/      /       )`·.         '         /       ,, -::::::::::::::/                '/      /       )`·.         '
   .·´/I       I     .·´ ..(.·´(    '   .·´( '/       /::::::::::;;-··´´'             .·´/I       I     .·´ ..(.·´(    ' 
   )/::I,       ` ·.):::...:::/.·´:('_) ::'/       /;;:::: · ´                     )/::I,       ` ·.):::...:::/.·´:('
   I:::::::.,         ¯¯¯¯¯¯.·´/)..::/       /                                 I:::::::.,         ¯¯¯¯¯¯.·´/
   I::::::::::::.. ______.·´:::/`·:/____ /                                  I::::::::::::.. ______.·´:::/
    ' ·:::;:::::::/::::::::::/::::·´'  /::::::::/                                     ' ·:::;:::::::/::::::::::/::::·´' 
         ' ·::::'/::::::::::/::·´     /::::::::/                                           ' ·::::'/::::::::::/::·´     
                ¯¯¯¯¯¯      '    ¯¯¯¯¯'                                                  ¯¯¯¯¯¯      '    

                                                                            
                                                                             @author wenjianhua(wjhokey@gmail.com)
                                                                                                        2018.7.4
"""

@click.command()
@click.option('-l', '--list', is_flag=True, help='lpl最新赛事')
@click.option('-n', '--new', is_flag=True, help="lpl最新新闻")
@click.option('-s', '--score', is_flag=True, help="队伍积分")
@click.option('-t', '--team', default=8, help="选择队伍 1-EDG, 2-IG, 8-RNG, 9-SS, 12-WE 57-BLG 默认为8")
@click.option('--search', type=str, help="搜索关键词")
@click.option('-m', '--member', is_flag=True, help="俱乐部队员")
def cli(list, new, score, team, search, member):
    # print(search)
    if list:
        gameList.game()
    elif new:
        gameNews.news(team)
    elif score:
        teamScore.score()
    elif search:
        webSearch.search(search)
    elif member:
        teamMembers.searchMember()

def main():
    print(app_desc)
    cli()


if __name__ == '__main__':
    main()