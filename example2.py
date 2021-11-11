#! /usr/bin/env python3
# coding: utf-8

"""This is the simpliest example of flamewok.Form"""


from flamewok import Form


some_form = Form([
    ("name", "what is your name ?"),
    ("age", "how old are you ?"),
    ])

print("Let me ask you :")

you = some_form.ask()

print(f"So your name is {you.name}, and you are {you.age}.")
