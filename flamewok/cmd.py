#! /usr/bin/env python3
# coding: utf-8


import flamewok
from flamewok.cli import cli

infos = f"""
=============================  flamewok  ===============================

Very tiny framework to quickly build python terminal applications.

version {flamewok.__version__}
home page: https://github.com/byoso/flamewok
pypi: https://pypi.org/project/flamewok/

"""


def info():
    print(infos)


def cmd():
    cli.route(
        f"Flamewok {flamewok.__version__}",
        "",
        ("", info, "Display informations about flamewok"),
        ("-h", cli.help, "show this help"),
        ("--help", cli.help, "show this help"),
    )


if __name__ == "__main__":
    cmd()
