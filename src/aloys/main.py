import os
import random
import pickle

import click
import pandas

OPEN_AI_API_KEY = "sk-1234567890abcdef1234567890abcdef"


# TODO : Say hello to more people
@click.command()
@click.option(
    "--name",
    prompt="Your name",
    help="The person to greet.",
)
def hello(name):
    click.echo(f"Hello {name}!")


if __name__ == "__main__":

    hello()
