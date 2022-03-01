#! /usr/bin/env python3
# coding: utf-8


"""This showes a more convenient way to work with menus when a project
gets bigger. (does the same as example1)"""


from flamewok import Menu


menu = Menu()


class Main:
    def __init__(self):
        menu.add_boxes([
            "\nChoose an option:\n",
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
        print("Goodbye folks !")
        quit()


main = Main()
