#! /usr/bin/env python3
# coding: utf-8

from flamewok.cli import cli


def main():
    print("main program lanched")


def see(*args):
    """the types are defined in the cli.route"""
    for arg in args:
        print(type(arg), arg)


def multi(*args):
    """the types are not defined in the cli.route, so the args are all str"""
    numbers = [float(arg) for arg in args]
    result = 1
    for num in numbers:
        result *= num
    print(result)


if __name__ == "__main__":
    cli.route(
        "This is a CLI test\n",  # this will appear in the help
        ("", main, "Launches the main programm"),
        ("-h", cli.help, "displays this help"),
        ("--help", cli.help, 'Idem'),
        (
            "see <int:a> <bool:> <str:> <float:>", see,
            "Show the arguments given in the CLI"
        ),
        ("multi <some_numbers>", multi, "multiply the numbers"),
    )
