#! /usr/bin/env python3
# coding: utf-8

from flamewok import Menu


"""This is the simpliest example of what can be done with flamewok"""


menu = Menu()


def hello():
    print("Hi there ! here is the callback hello !")
    menu.ask()


def how():
    print("I'm quite fine, thank you :)")
    menu.ask()


def exit():
    print("Good Bye folks !")
    quit()


menu.add_boxes([
    "\nChoose an option:\n",
    (1, "hello !", hello),
    (2, "how are you ?", how),
    ("x", "exit", exit),
])

menu.ask()
