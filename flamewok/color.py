#! /usr/bin/env python3
# coding: utf-8


"""This module provides some helpers to handle color in terminal

WARNING: the display of the colors is quite hasardous depending on the
terminal you use, and the os you are running. It seems ok in simple line
displayed string, but becomes very messy if used in a menu.

To change a color of a text, use a color mark in the str itself, and the end
mark to get back to normal.

To see a palette, import the function palette from the module,
or execute the module in a terminal:
    python3 -m flamewok.color

ex: import color as c

    title = c.Color(1, 45 ,37)
    print(f"{title.mark}A title{title.end}")

a few marks are ready to use in this module:

end = '\x1b[0m'

info = Color(0, 46, 30).mark
success = Color(0, 42, 30).mark
warning = Color(1, 43, 30).mark
danger = Color(1, 41, 33).mark

"""

# this mark will be user often
end = "\x1b[0m"


class Color:
    """Color object, it requires 3 parameters (int):
    - style: from 0 to 8
    - background: from 0 to 50
    - foreground: from 0 to 50
    """
    def __init__(self, style, foreground, background):
        self.style = style
        self.foreground = foreground
        self.background = background
        self.ref = (
            f"{str(self.style)};"
            f"{str(self.background)};"
            f"{str(self.foreground)}")
        self.mark = f"\x1b[{self.ref}m"
        self.end = "\x1b[0m"

    def __str__(self):
        return f"{self.mark} {self.ref} {end}"

    def __repr__(self):
        return f"<Color | {str(self)}>"


def palette(style_range=(0, 8), bg_range=(30, 38), fg_range=(40, 48)):
    """
    Showes some color references
    """
    for style in range(style_range[0], style_range[1]):
        for background in range(bg_range[0], bg_range[1]):
            show = ''
            for foreground in range(fg_range[0], fg_range[1]):
                color = Color(style, background, foreground)
                show += str(color)
            print(show)
        print('\n')


# Some prebuilt marks

info = Color(0, 46, 30).mark
success = Color(0, 42, 30).mark
warning = Color(1, 43, 30).mark
danger = Color(1, 41, 33).mark


if __name__ == "__main__":

    palette()

    print(f"{info} info {end}")
    print(f"{success} success {end}")
    print(f"{warning} warning {end}")
    print(f"{danger} danger {end}")
