#! /usr/bin/env python3
# coding: utf-8

from flamewok import Form, Field


"""Let's see how to dynamically change the form"""

form = Form([
    ("name", "what is your name ?"),
    ("age", "how old are you ?"),
    ])

# you can also build fields like this:
new_field = Field("height", "How tall are you ?")

# Form.fields is a simple list, manipulate it as so:
form.fields.insert(1, new_field)


print("Let me ask you :")

response = form.ask()

print("Your answers are:")
print(
    f"name: {response.name}\nheight: {response.height}\nage: {response.age}")
