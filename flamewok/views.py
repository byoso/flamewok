
"""The views module contains the elements concerning the views.
You should import in your main program:

Menu
Form

"""


class Menu:
    """Menu builds the menu display, and emmits a signal depending on
    the answer."""
    def __init__(
        self, boxes, sep=" | ",
        box_size=20,
        line_length=80,
        prompt="?> "
            ):
        """boxes is a list of tuples of strings built like this:
        - the tuples (will be the dialog boxes) have 3 or more elements:
        the user's choice to enter,
        a label describing the action,
        1 or more signals returned if choosen by the user
        - some str to insert in the menu (ex: "\n")
        """
        self.prompt = prompt
        self.body = ""
        self.actions = {}
        self.response = None

        # manage the number of dialog boxes per line
        box_number = line_length // box_size
        for el in boxes:
            if type(el) == str:
                self.body += el
            else:
                if box_number == 0:
                    self.body += "\n"
                    box_number = line_length // box_size

                box_number -= 1
                box = ""
                box += f"{el[0]} : {el[1]}"
                # set actions from the 'boxes' argument
                self.actions[str(el[0])] = el[2:]
                self.body += f"{box[:box_size]:<{box_size}}{sep}"
        # self.ask()

    def ask(self):
        print(self.body)
        return self.input()

    def input(self):
        choice = input(self.prompt)
        if choice in self.actions:
            self.response = self.actions[choice]
            return self.send_response()
        else:
            return self.ask()

    def send_response(self):
        return self.response

    def __str__(self):
        return f"<Menu | {len(self.actions)} choices>"


class Response:
    """Single empty class used for the Form response"""
    pass


class Form:
    """Give a list of fields
    fields are tuples made of 2 elements:
    - str(the key to register the answer)
    - str(the text to display)
    """
    def __init__(self, fields, prompt="> "):
        self.prompt = prompt
        self.fields = fields

    def ask(self):
        response = Response()
        for el in self.fields:
            print(f"{el[1]}")
            value = input(self.prompt)
            setattr(response, el[0], value)
        return response
