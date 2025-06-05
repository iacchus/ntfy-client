import json

import click

from . import NTFYClient

from . import NTFY_SERVER_HOSTNAME
from . import NTFY_TOPIC
from . import NTFY_TOKEN

from . import args

server_hostname_option = \
        click.option("--server-hostname",
                     envvar="NTFY_SERVER_HOSTNAME")
topic_option = \
        click.option("--topic",
                     envvar="NTFY_TOPIC")
token_option = \
        click.option("--topic",
                     envvar="NTFY_TOKEN")
message_option = \
        click.option("--message",
                     envvar="NTFY_DEFAULT_MESSAGE")
title_option = \
        click.option("--title",
                     envvar="NTFY_DEFAULT_TITLE")
@click.group
def cli():
    pass

@cli.command()
def pub():

    ntfy_client = NTFYClient(hostname=NTFY_SERVER_HOSTNAME,
                            topic=NTFY_TOPIC,
                            token=NTFY_TOKEN,
                            args=args)

    r = ntfy_client.pub()
    response_data = json.dumps(r.json(), indent=2)
    print("Response data:", response_data, sep="\n")

if __name__ == "__main__":

    cli()

