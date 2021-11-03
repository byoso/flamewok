#! /usr/bin/python3 -i
# coding: utf-8


"""Menu example
Here it's roughtly the same as example2, but using the Handler class"""

from flamewok.controllers import Handler
from flamewok.views import Menu


menu = Menu([
    "\n",
    (0, "best", "go_best"),
    (1, "nice", "go_nice"),
    (2, "pretty", "go_pretty"),
    (3, "strong", "go_strong"),
    (4, "funny", "go_funny"),
    ("combo", "a combo of 3 signals", "go_combo", "go_pretty", "go_best"),
    ("x", "exit", "go_end"),
])
# those last 3 are optionnal, try to change them to see what it does


class Facade:
    """Could be the main class of a programm"""

    def __init__(self):
        """The handler connects the signals from the menu to the methods"""
        self.handler = Handler({
            "go_best": self.best,
            "go_nice": self.nice,
            "go_pretty": self.pretty,
            "go_strong": self.strong,
            "go_funny": self.funny,
            "go_combo": self.combo,
            "go_end": self.end,
        })
        # this line is just to use the Handler.handle method
        # in a more convenient way:
        self.handle = self.handler.handle

        # infinite loop as long as the user doesn't choose to exit
        while True:
            response = menu.ask()
            self.handle(response)

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


if __name__ == "__main__":
    try:
        main = Facade()
    except KeyboardInterrupt:
        print("\nInteruption by the user")
