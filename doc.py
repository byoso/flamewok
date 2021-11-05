#! /usr/bin/env python3
# coding: utf-8


from flamewok import Menu


menu_main = Menu()
menu_menu = Menu()
menu_form = Menu()


class Main:
    def __init__(self):
        menu_main.add_boxes([
            (1, "Menu doc", DocMenu),
            (2, "Form doc", DocForm),
            ("x", "close", quit),
        ])
        self.main()

    def main(self):
        menu_main.ask()


class DocMenu:
    def __init__(self):
        menu_menu.add_boxes([
            (0, "back", Main),
            (1, "Form", DocForm)
        ])
        self.main()

    def main(self):
        menu_menu.ask()


class DocForm:
    def __init__(self):
        menu_form.add_boxes([
            (0, "back", Main),
            (1, "Form", DocMenu)
        ])
        self.main()

    def main(self):
        menu_form.ask()

if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print("\nend")
