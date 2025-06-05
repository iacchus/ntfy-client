from abc import abstractstaticmethod
from argparse import Action
import json
from ntpath import isjunction

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
priority_option = \
        click.option("--priority",
                     envvar="NTFY_PRIORITY")
tags_option = \
        click.option("--tags",
                     envvar="NTFY_TAGS")
delay_option = \
        click.option("--delay",
                     envvar="NTFY_DELAY")
click_option = \
        click.option("--click",
                     envvar="NTFY_")
markdown_option = \
        click.option("--markdown",
                     envvar="NTFY_")
action_option = \
        click.option("--action",
                     envvar="NTFY_")
file_option = \
        click.option("--file",
                     envvar="NTFY_FILE")
attach_option = \
        click.option("--attach",
                     envvar="NTFY_ATTACH")
firebase_option = \
        click.option("--firebase",
                     envvar="NTFY_FIREBASE")
unifiedpush_option = \
        click.option("--unifiedpush",
                     envvar="NTFY_UNIFIEDBASE")
filename_option = \
        click.option("--filename",
                     envvar="NTFY_FILENAME")
email_option = \
        click.option("--email",
                     envvar="NTFY_EMAIL")
call_option = \
        click.option("--call",
                     envvar="NTFY_CALL")
cache_option = \
        click.option("--cache",
                     envvar="NTFY_CACHE")
poll_id_option = \
        click.option("--poll-id",
                     envvar="NTFY_POLL_ID")
content_type_option = \
        click.option("--content-type",
                     envvar="NTFY_CONTENT_TYPE")

@click.group
def cli():
    pass

@cli.command()
@server_hostname_option
@topic_option
@token_option
@message_option
@title_option
@priority_option
@tags_option
@delay_option
@click_option
@markdown_option
@action_option
@file_option
@attach_option
@firebase_option
@unifiedpush_option
@filename_option
@email_option
@call_option
@cache_option
@poll_id_option
@content_type_option
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

