#! /usr/bin/env python3
# coding: utf-8


"""Let's play a bit with dynamic construction of the menu.
Do you really need that ? I do not, but it is possible.
"""

from flamewok import Menu, TextBox
from flamewok.menu import ActionBox


menu = Menu()


class Facade:
    def __init__(self):
        menu.add_boxes([
            "\nChoose an option:\n",
            (1, "hello !", self.hello),
            (2, "Gimme a smile !", self.smile),
            (2, "with same choice index", self.smile),
            ("2", "are not implemented", self.smile),
            ("x", "exit", self.exit),
            ])
        menu.ask()

    def hello(self):
        print("Hi there ! here is the callback hello !")
        menu.ask()

    def smile(self):
        print("I'm quite fine, thank you :)")
        box = TextBox(" :D ")
        menu.boxes.append(box)
        box = ActionBox(3, "remove smileys", self.remove_smiley)
        if len(menu.boxes) == 5:
            menu.boxes.insert(3, box)
        menu.ask()

    def remove_smiley(self):
        if len(menu.boxes) > 5:
            menu.boxes.remove(menu.boxes[-1])
        if len(menu.boxes) < 6:
            menu.boxes.remove(menu.boxes[3])
        menu.ask()

    def exit(self):
        print("Goodbye folks !")
        quit()


main = Facade()
