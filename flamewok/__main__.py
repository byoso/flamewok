"""Curenttly, to work with flamewok, you may need to import some of
this objects:

Menu
TextBox
ActionBox
Form
Field
"""

from flamewok.menu import Menu, TextBox, ActionBox
from flamewok.form import Form, Field
from flamewok.validators import check_type
from flamewok.helpers import clear

infos = """
flamewok

version 1.0.3
home page: https://github.com/byoso/flamewok

"""

if __name__ == "__main__":
    print(infos)
    # help(Menu)
    # help(TextBox)
    # help(ActionBox)
    # help(Form)
    # help(Field)
    # help(check_type)
