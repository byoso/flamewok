# FlameWok

_Very tiny framework to quickly create python terminal apps._

The purpose of this package is to get you rid as much as possible
of the tedious part of creating menus, forms, and CLI, and to help to keep the code clean.


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

yes, that simple !

## Create very quickly a CLI

```python
from flamewok.cli import cli


def main():
    print("main program lanched")


def see(*args):
    """the types are defined in the cli.route"""
    for arg in args:
        print(type(arg), arg)

def multi(*args):
    """the types are not defined in the cli.route, so the args are all str"""
    numbers = [float(arg) for arg in args]
    result = 1
    for num in numbers:
        result *= num
    print(result)


if __name__ == "__main__":
    cli.route(
        "This is a CLI test\n", # this will appear in the help
        ("", main, "Launches the main programm"),
        ("-h", cli.help, "displays this help"),
        ("--help", cli.help, 'Idem'),
        ("see <int:a> <bool:> <str:> <float:>", see, "Show the arguments given in the CLI"),
        ("multi <some_numbers>", multi, "multiply the numbers"),
    )
```

check the [wiki](https://github.com/byoso/flamewok/wiki) to get a better idea of what you can do.



flamewok, docs and exemples are available here:
https://github.com/byoso/flamewok
