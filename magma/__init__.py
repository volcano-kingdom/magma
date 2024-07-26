import json

import click

from . import chat as mchat


@click.group()
def cli():
    pass

@cli.group()
def chat():
    pass

@chat.command('decode')
@click.argument('input', default='-', type=click.File('rb'))
@click.argument('output', default='-', type=click.File('w', encoding='utf8'))
def chat_decode(input, output):
    json.dump(
        mchat.decode(input),
        output,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    )

