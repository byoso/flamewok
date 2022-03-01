# FlameWok

_Very tiny framework project to quickly build python apps running
ONLY in terminal._

The purpose of this package is to get you rid as much as possible 
of the tedious part of creating menus and forms, and help to keep
the code clean.

Fully functionnal now. Works great !

## Installation
```sh
pip install flamewok
```

## Create forms
```python
from flamewok import Form

my_form = Form([
    ("name", "what is your name ?"),
    ("age", "how old are you ?"),
    ])
    
response = my_form.ask()    
```
## Create menus
```python
from flamewok import Menu

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


```

yes, that simple.

check the exemples to get a better idea of what you can do.



flamewok, docs and exemples are available here:
https://github.com/byoso/flamewok
