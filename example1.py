#! /usr/bin/env python3
# coding: utf-8

"""Form example
Here we will build a single form, and use it multiple times"""


from flamewok.views import Form


form = Form([
    ("name", "Enter your name"),
    ("size", "Enter your size"),
    ("age", "Enter you age")
])

print("Player 1")
player1 = form.ask()
print("Player 2")
player2 = form.ask()

print(
    f"{player1.name}, aged {player1.age}, height: {player1.size} Vs "
    f"{player2.name}, aged {player2.age}, height: {player2.size}"
    )
