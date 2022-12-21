#! /usr/bin/env python3
# coding: utf-8


import flamewok
from flamewok.cli import cli


def cmd():
    cli.route(
        f"Flamewok {flamewok.__version__}",
        "",
        (["", "-h", "--help"], cli.help, "show this help"),
        "_"*78,
        "About",
        'doc: https://github.com/byoso/flamewok/wiki',
        'home page: https://github.com/byoso/flamewok',
        'pypi: https://pypi.org/project/flamewok/',

    )


if __name__ == "__main__":
    cmd()
