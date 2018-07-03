import game
import news
import click



@click.command()
@click.option('-l', '--list', is_flag=True, help='lpl最新赛事')
@click.option('-n', '--new', is_flag=True, help="lpl最新新闻")
def cli(list, new):
    # print(list, new)
    if list:
        game.game()
    elif new:
        news.news()

if __name__ == '__main__':
    cli()