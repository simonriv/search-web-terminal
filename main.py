import click
import utils

@click.command()
@click.argument('search',nargs=-1)
def wsearch(search):
    if search:
        verifed_text = utils.verify_search(search)
        exec = utils.exec_search(verifed_text)
        if exec != 0:
            click.echo("We were unable to perform the search",err=True,fg='red',bold=True)
    else:
        click.echo("The search cannot be empty",err=True)
    

if __name__ == '__main__':
    wsearch()
