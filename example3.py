#! /usr/bin/env python3
# coding: utf-8


"""Menu example
Here we will create a menu, and use it in a Facade"""

from flamewok.views import Menu


menu = Menu([
    "\n",
    (0, "best", "go_best"),
    (1, "nice", "go_nice"),
    (2, "pretty", "go_pretty"),
    (3, "strong", "go_strong"),
    (4, "funny", "go_funny"),
    ("combo", "a combo of 3 signals", "go_combo", "go_pretty", "go_best"),
    ("stop", "enought of that !", "go_end"),
], box_size=20, line_length=80, prompt="your choice > ")
# those last 3 are optionnal, try to change them to see what it does


class Facade:
    """Could be the main class of a programm"""

    def __init__(self):
        while True:
            response = menu.ask()
            self.handle(response)

    def handle(self, response):
        actions = {
            "go_best": self.best,
            "go_nice": self.nice,
            "go_pretty": self.pretty,
            "go_strong": self.strong,
            "go_funny": self.funny,
            "go_combo": self.combo,
            "go_end": self.end,
        }
        if len(response) == 1:
            actions[response[0]]()
        else:
            actions[response[0]](response[1:])

    def best(self, other=None):
        print("\nYou know you are the best !")
        if other:
            self.handle(other)

    def nice(self, other=None):
        print("\nYou are a very nice person")
        if other:
            self.handle(other)

    def pretty(self, other=None):
        print("\nYou are the prettiest thing i've ever seen")
        if other:
            self.handle(other)

    def strong(self, other=None):
        print("\nYou are sooooo strong !")
        if other:
            self.handle(other)

    def funny(self, other=None):
        print("\nYou'll always be the funniest person on earth !")
        if other:
            self.handle(other)

    def combo(self, other):
        print("\nA fisrt thing, and then :")
        if other:
            self.handle(other)

    def end(self):
        exit()


main = Facade()
