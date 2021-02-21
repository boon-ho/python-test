#!/usr/bin/env python

import click
from hello import with_input
import sys

@click.command()
@click.option('--color', help="help")
def callcolor(color):
    result = with_input(color)
    statement = f"""My color is: {result["old"]}, 
    but I also like {result["new"]}"""
    click.echo(click.style(statement, bg=result["old"], fg="white"))
    sys.exit(0)
    #click.echo(result)
    #click.echo(click.style(f'{result}', bg='green')) 

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    callcolor()
