import gameList
import gameNews
import teamScore
import click

@click.command()
@click.option('-l', '--list', is_flag=True, help='lpl最新赛事')
@click.option('-n', '--new', is_flag=True, help="lpl最新新闻")
@click.option('-s', '--score', is_flag=True, help="队伍积分")
@click.option('-t', '--team', default=8, help="选择队伍 1-EDG, 2-IG, 8-RNG, 9-SS, 12-WE 57-BLG")
def cli(list, new, score, team):
    # print(list, new)
    if list:
        gameList.game()
    elif new:
        gameNews.news(team)
    elif score:
        teamScore.score()

if __name__ == '__main__':
    cli()