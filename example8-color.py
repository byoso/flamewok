#! /usr/bin/env python3
# coding: utf-8


"""In this example we'll do the same as in example7, but we'll use
some color form the color module.
It is still a module to test, but honestly, color can quickly turn
your interface into a visual mess. One should not abuse of that."""

from flamewok import Form, Menu
from flamewok import check_type  # check_type is itself a validator
from flamewok import color as c




########################### MOCK ####################################
# don't care about this part, it is just to populate the app with some
# datas.
class Data:  # this will emulate our warriors
    def __init__(self, args):
        self.name = args[0]; self.str = args[1]; self.dex = args[2]
        self.hp = args[3]
datas_for_mock = [
    ("Grororo", 15, 78, 55),
    ("Buzzador", 56, 7, 155),
    ("Malkrafter", 15, 25, 98),
    ("Ze Bizu", 45, 73, 67),
]
mock_datas = []
for data in datas_for_mock:
    mock_datas.append(Data(data))
############################ Enought with mock, back to buisness !####


# using color, it is wise to 'kill' the color setting in the prompt:
menu = Menu(prompt=f"{c.end}?> ") 
menu_list = Menu(prompt=f"{c.end}?> ")


def war_validator(entry):
    return check_type(entry, int) and int(entry) > 0

warrior_form = Form([
    ("name", "Warrior's name ?", lambda x: len(x) > 0,
        f"{c.warning}A warrior needs a real name !{c.end}"),

    ("str", "Strength",
        lambda entry: check_type(entry, int) and int(entry) > 0),
    ("dex", "Dexterity", war_validator),
    ("hp", "max health (can be negative)",
        lambda entry: check_type(entry, int))
], error_message=f"{c.warning}Warrior Error ! Do Better !{c.end}")


# a color
title = c.Color(1, 44, 37)


class Main:
    def __init__(self):
        menu.add_boxes([
            f"{title.mark}\n=== WARRIORZZZZ's ==={c.end}\n", c.end,
            (1, "new warrior", self.new_warrior),
            (2, "see the warriors", self.show_warriors),
            ("x", f"{c.danger}close{c.end}", quit),
            c.end,
        ])

        menu_list.add_boxes([
            f"{title.mark}===> sort your heroes <==={c.end}\n",
            (0, "back", self.main_menu),
            (1, "strongest", self.sort_str),
            (2, "dexterious", self.sort_dex),
            (3, "Endurous", self.sort_hp),
        ])

        self.warriors = mock_datas  # mock again here
        self.main_menu()

    def main_menu(self):
        menu.ask()

    def new_warrior(self):
        self.warriors.append(warrior_form.ask())
        menu.ask()

    def show_warriors(self):
        print("\n"+"_"*80)
        print(f"{'= '*6:>25}{title.mark}{'Warriors list':^30}{c.end}{'= '*6:<25}")
        print(f"{'Name':<40}{'Strength':^15}{'Dexterity':^15}{'HP':^10}")
        print("_ "*40)
        for w in self.warriors:
            print(f"{w.name:<40}{w.str:^15}{w.dex:^15}{w.hp:^10}")

        menu_list.ask()

    def sort_str(self):
        self.warriors = sorted(self.warriors, key=lambda w: -int(w.str))
        self.show_warriors()

    def sort_dex(self):
        self.warriors = sorted(self.warriors, key=lambda w: -int(w.dex))
        self.show_warriors()

    def sort_hp(self):
        self.warriors = sorted(self.warriors, key=lambda w: -int(w.hp))
        self.show_warriors()


if __name__ == "__main__":
    try:
        main = Main()
    except KeyboardInterrupt:
        print(f"\nend{c.end}")
