import click
import utils

@click.command()
@click.option('--browser','-b',help='Choose between Opera, Chrome, Firefox, Edge, Brave or Explorer')
@click.option('--engine','-e',help='Choose between Google,Yahoo,Bing,DuckDuckGo')
@click.argument('search',nargs=-1)
def wsearch(browser,engine,search):
    if search and not browser and not engine:
        verifed_text = utils.verify_search(search)
        exec = utils.exec_search(verifed_text)
        if exec != 0:
            click.echo("We were unable to perform the search",err=True)
    elif not search and browser and engine:
        data = {
            'browser':browser,
            'engine':engine
        }
        config = utils.set_config(data)

        if config == False:
            click.echo("you must use the allowed options for Opera, Chrome, Firefox, Edge, Brave or Explorer browsers and Google, Yahoo, Bing, DuckDuckGo search engines.")
        else:
            click.echo("Configuration successfully created.")
    else:
        click.echo("The search cannot be empty",err=True)

if __name__ == '__main__':
    wsearch()
