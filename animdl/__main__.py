"""
A one cli for all the anime.
"""

import click

from .core import __version__
from .core.cli.commands import download, grab, schedule, search, stream
from .core.cli.helpers.player import supported_streamers

commands = {
    "download": download.animdl_download,
    "grab": grab.animdl_grab,
    "schedule": schedule.animdl_schedule,
    "search": search.animdl_search,
}

executable = list(supported_streamers())

if executable:
    commands.update({"stream": stream.animdl_stream})


@click.group(commands=commands)
@click.version_option(__version__.__core__, "-v")
def __animdl_cli__():
    pass


if __name__ == "__main__":
    __animdl_cli__()
