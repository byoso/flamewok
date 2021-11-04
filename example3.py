#! /usr/bin/env python3
# coding: utf-8

from flamewok import Menu


"""This showes a more convenient way to work with menus when a project
gets bigger. (does the same as example1)"""


menu = Menu()
# here I split the menu.add_boxes work in 2 parts just to show you that
# it's possible, it seems useless but can be used to adapt an existing
# menu to a new context.
menu.add_boxes([
    "\nChoose an option:\n",
])


class Facade:
    def __init__(self):
        menu.add_boxes([
            (1, "hello !", self.hello),
            (2, "how are you ?", self.how),
            ("x", "exit", self.exit),
            ])
        menu.ask()

    def hello(self):
        print("Hi there ! here is the callback hello !")
        menu.ask()

    def how(self):
        print("I'm quite fine, thank you :)")
        menu.ask()

    def exit(self):
        print("Good Bye folks !")
        quit()


main = Facade()
