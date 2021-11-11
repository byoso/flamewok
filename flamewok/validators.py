#! /usr/bin/env python3


"""This module provides some validators to use in the forms or else.
validators are functions that always return a boolean
"""


def check_type(value, a_type):
    """Takes 2 parameters : a value and a type (bool, int or float)
    The fonction returns a boolean.
    check_type does NOT convert the value of the input,
    that remains a string.
    """
    if a_type == bool:
        if value.lower() in ["true", "false"]:
            return True
        else:
            return False
    else:
        try:
            a_type(value)
        except ValueError:
            return False
        return True

