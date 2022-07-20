from abc import ABC

from flamewok import settings


class Box(ABC):
    """Box classes must inherit from this"""
    def __init__(self, label=""):
        self.label = label

    def __str__(self):
        return f"<Box| {self.label}>"

    def __repr__(self):
        return str(self)


class ActionBox(Box):
    """An ActionBox is an activable element of the menu"""
    def __init__(self, choice="", label="", func=None):
        super().__init__(label)
        self.choice = str(choice)
        self.func = func

    def __str__(self):
        return f"<ActionBox| {self.choice} : {self.label} to {self.func}>"


class TextBox(Box):
    """A TextBox in a non-activable element of the menu, in fact, strings.
    """
    def __init__(self, label):
        super().__init__(label)

    def __str__(self):
        return f"<TextBox| {self.label} >"


class Menu:
    """Central class of the menu system"""

    def __init__(
        self,
        inside_sep=settings.DEFAULT_INSIDE_SEP,
        sep=settings.DEFAULT_SEP,
        box_size=settings.DEFAULT_BOX_SIZE,
        line_length=settings.DEFAULT_LINE_LENGTH,
        prompt=settings.DEFAULT_MENU_PROMPT,
        error_message=settings.DEFAULT_MENU_ERROR,
            ):
        """boxes is a list of tuples of strings built like this:
        - the tuples (will be the dialog boxes) have 3 or more elements:
        the user's choice to enter,
        a label describing the action,
        1 or more ids returned if choosen by the user
        - some str to insert in the menu (ex: "\n")
        """
        self.inside_sep = inside_sep
        self.sep = sep
        self.line_length = line_length
        self.box_size = box_size
        self.prompt = prompt
        self.response = None
        self.error_message = error_message
        self.boxes = []
        self.body = ""

    def __str__(self):
        return f"<Menu | {len(self._choices)} choices>"

    def __repr__(self):
        return str(self)

    def _build(self):
        """"Builds the aspect of the menu to display"""
        # manage the number of dialog boxes per line
        self.body = ""
        choices = []
        box_number = self.line_length // self.box_size
        for el in self.boxes:
            if isinstance(el, TextBox):
                self.body += el.label
            else:
                if el.choice in choices:
                    self.boxes.remove(el)
                else:
                    if box_number == 0:
                        self.body += "\n"
                        box_number = self.line_length // self.box_size
                    box_number -= 1
                    box = ""
                    box += f"{el.choice}{self.inside_sep}{el.label}"
                    self.body += (
                        f"{box[:self.box_size]:<{self.box_size}}{self.sep}")
                    choices.append(el.choice)

    def _input(self):
        """manage the input"""
        choice = input(self.prompt)
        if choice in self._choices:
            self.response = choice
            self._go_callback(choice)
        else:
            print(self.error_message)
            return self.ask()

    @property
    def _choices(self):
        """returns a list of all the choices used in the menu"""
        choices = []
        for box in self.boxes:
            if isinstance(box, ActionBox):
                choices.append(box.choice)
        return choices

    def _go_callback(self, choice):
        """Calls the box's associated function"""
        box = self.get_action_box(choice)
        return box.func()

    def ask(self):
        """Displays the menu and the prompt"""
        self._build()
        print(self.body)
        return self._input()

    def get_action_box(self, choice):
        """Returns an ActionBox from self.boxes"""
        box = list(filter(lambda b: isinstance(
            b, ActionBox) and b.choice == choice, self.boxes))[0]
        return box

    def get_box(self, index):
        """"Return any box from self.boxes"""
        box = self.boxes[index]
        return box

    def add_boxes(self, boxes):
        """boxes here are :
        - a list of tuple(s):
        [(choice, label, function), ...]
        - or a string"""
        for box in boxes:
            self.add_box(box)

    def add_box(self, box):
        """create and add a box from:
        - a tuple:
        (choice, label, function)
        - a string"""
        if isinstance(box, type(str())):
            new_box = TextBox(box)
            self.boxes.append(new_box)
        else:
            choice = box[0]
            if str(choice) in self._choices:
                pass
            else:
                label = box[1]
                func = box[2]
                new_box = ActionBox(choice, label, func)
                self.boxes.append(new_box)

    def insert(self, index, box):
        """Inserts a box in the menu at the index"""
        self.boxes.insert(index, box)

    def set_boxes(self, boxes):
        """Remove a former box list and replace with a new one"""
        self.boxes = []
        self.add_boxes(boxes)
