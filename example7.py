#! /usr/bin/env python3
# coding: utf-8


"""In this example we'll do the same as in example6, but this time
with validators in the fields to check the validity of the entry.
validators can be any function that returns a booléan"""

from flamewok import Form, Menu
from flamewok import check_type  # check_type is itself a validator


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


menu = Menu()
menu_list = Menu()  # so we have 2 menus


# this is a custom validator as a function:
def war_validator(entry):
    return check_type(entry, int) and int(entry) > 0

# validator must be used in lambda functions in the fields
warrior_form = Form([
    # a validator can also be the lambda itself:
    ("name", "Warrior's name ?", lambda x: len(x) > 0,
        # this gives a custom message for an invalid entry:
        "A warrior needs a real name !"),
    ("str", "Strength",
        lambda entry: check_type(entry, int) and int(entry) > 0),
    # the custom validator is called here:
    ("dex", "Dexterity", lambda entry: war_validator(entry)),
    ("hp", "max health (can be negative)",
    # here is used the flamewok.validators.check_type validator alone:
        lambda entry: check_type(entry, int))
])


class Main:
    def __init__(self):
        # I use methods as callbacks, so I must declare the boxes inside
        #  the class, othewise 'self' would have no meaning.
        menu.add_boxes([
            "\n=== WARRIORZZZZ's ===\n",
            (1, "new warrior", self.new_warrior),
            (2, "see the warriors", self.show_warriors),
            ("x", "close", quit),
        ])

        menu_list.add_boxes([
            f"{'===> sort your heroes <===':^80}\n",
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
        print(f"{'= '*6:>25}{'Warriors list':^30}{'= '*6:<25}")
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
        print("\nend")
