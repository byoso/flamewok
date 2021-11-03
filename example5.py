#! /usr/bin/env python3
# coding: utf-8


from flamewok.views import Menu
from flamewok.controllers import Handler


menu = Menu([
    (1, "choix n°1", "go_choix1"),
    (2, "choix n°2", "go_choix2"),
    (3, "choix n°3", "go_choix3"),
    ])


handler = Handler()
handle = handler.handle


class Facade:
    def __init__(self):
        handler.connect([
            ("go_choix1", self.choix1),
            ("go_choix2", self.choix2)])
        handler.connect([("go_choix3", self.choix3)])
        handle(menu.ask())

    def choix1(self):
        print("choix numéro 1 selectionné")
        handle(menu.ask())

    def choix2(self):
        print("choix numéro 2 selectionné")
        handle(menu.ask())

    def choix3(self):
        print("choix numéro 3 selectionné")
        handle(menu.ask())


if __name__ == "__main__":
    try:
        main = Facade()
    except KeyboardInterrupt:
        print("\nend")
