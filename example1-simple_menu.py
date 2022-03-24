#! /usr/bin/env python3
# coding: utf-8


"""This is the simpliest example of what can be done with flamewok.Menu"""


from flamewok import Menu, clear
# 'clear' is a helper, simply does os.system('clear') on linux/MacOS
# or os.system('cls') on windows, its use is optionnal.

menu = Menu()


def hello():
    clear()
    print("Hi there ! here is the callback hello !")
    menu.ask()


def how():
    clear()
    print("I'm quite fine, thank you :)")
    menu.ask()


def exit():
    clear()
    print("Good Bye folks !")
    quit()


menu.add_boxes([
    "\nChoose an option:\n",
    (1, "hello !", hello),
    (2, "how are you ?", how),
    ("x", "exit", exit),
])

menu.ask()
