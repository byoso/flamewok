
from uuid import uuid4

from .controllers import Handler
from flamewok import settings


class Box:
    """A box is an activable element of the menu"""
    def __init__(self, choice, label, signal, func):
        self.choice = choice
        self.label = label
        self.signal = signal
        self.func = func

    def __str__(self):
        return f"<Box| {self.choice} : {self.label} to {self.func}>"

    def __repr__(self):
        return str(self)


class TextBox:
    """A NoBox in a non activable element of the menu, in fact, strings.
    but it has to have a signal, used also as an id"""
    def __init__(self, text, signal):
        self.label = text
        self.signal = signal


class Menu:
    """Menu builds the menu display, and emmits a signal depending on
    the answer."""

    def __init__(
        self,
        sep=" | ",
        box_size=settings.DEFAULT_BOX_SIZE,
        line_length=settings.DEFAULT_LINE_LENGTH,
        prompt=settings.DEFAULT_MENU_PROMPT,
        error_message=settings.DEFAULT_MENU_ERROR,
        handler=None,
            ):
        """boxes is a list of tuples of strings built like this:
        - the tuples (will be the dialog boxes) have 3 or more elements:
        the user's choice to enter,
        a label describing the action,
        1 or more signals returned if choosen by the user
        - some str to insert in the menu (ex: "\n")
        """
        self.sep = sep
        self.line_length = line_length
        self.box_size = box_size
        self.prompt = prompt
        self.body = ""
        self.actions = {}
        self.response = None
        self.error_message = error_message
        self.boxes = []
        self.body = ""
        if handler:
            self.handler = handler
        else:
            self.handler = Handler()

    def build(self):
        # manage the number of dialog boxes per line
        self.body = ""
        self.actions = {}
        self.handler.actions = {}
        box_number = self.line_length // self.box_size
        for el in self.boxes:
            if isinstance(el, TextBox):
                self.body += el.label
                self.actions[el.label.strip()] = el.signal
                self.handler.actions[el.signal] = None
            else:
                if box_number == 0:
                    self.body += "\n"
                    box_number = self.line_length // self.box_size
                box_number -= 1
                box = ""
                box += f"{el.choice} : {el.label}"
                # set actions from the 'boxes' argument
                self.actions[str(el.choice)] = el.signal
                self.handler.actions[el.signal] = el.func
                self.body += (
                    f"{box[:self.box_size]:<{self.box_size}}{self.sep}")

    def ask(self):
        print(self.body)
        return self.input()

    def input(self):
        choice = input(self.prompt)
        if choice in self.actions:
            self.response = self.actions[choice]
            return self.send_response()
        else:
            print(self.error_message)
            return self.ask()

    def send_response(self):
        return self.handler.handle(self.response)

    def __str__(self):
        return f"<Menu | {len(self.actions)} choices>"

    def __repr__(self):
        return str(self)

    def add_boxes(self, boxes):
        """boxes must be:
        - a list of tuple(s):
        (choice, label, function)
        - or a string"""
        for box in boxes:
            signal = str(uuid4())
            if isinstance(box, type(str())):
                new_box = TextBox(box, signal)
                self.handler.connect([(new_box.signal, None), ])
                self.boxes.append(new_box)
            else:
                choice = box[0]
                label = box[1]
                func = box[2]
                new_box = Box(choice, label, signal, func)
                self.handler.connect([(new_box.signal, func), ])
                self.boxes.append(new_box)
        self.build()

    def set_boxes(self, boxes):
        """Overload the former box list and replace with the new one"""
        self.boxes = []
        self.add_boxes(boxes)

    def get_box(self, choice):
        """return the box with its choice code"""
        pass


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
