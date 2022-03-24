
from flamewok import settings


class NoNameError(Exception):
    def __init__(self):
        message = "Field with no name error"
        super().__init__(message)


class Field:
    """a Form needs some Field objects
    only 'name' is a necessary argument.
    """
    def __init__(
        self, name=None, label="", validator=None,
            error_message=None):
        if name:
            self.name = name
            self.label = label
            self.validator = validator
            self.message = error_message
        else:
            raise NoNameError

    def __str__(self):
        return f"<Field | {self.name} -> {self.label}>"

    def __repr__(self):
        return str(self)


class Response:
    """Single empty class used for the Form response"""
    # TODO: __str__ method
    pass


class Form:
    """Give a list of fields
    fields are tuples made of 2 elements:
    - str(the key to register the answer)
    - str(the text to display)
    Optional key words :
    - prompt: str
    - error_message: str
    """
    def __init__(self, fields: tuple, prompt=settings.DEFAULT_FORM_PROMPT,
                 error_message=settings.DEFAULT_FIELD_ERROR):
        self.message = error_message
        self.prompt = prompt
        self.fields = []
        for field in fields:
            new_field = Field(*field)
            self.fields.append(new_field)

    def ask(self):
        response = Response()
        for field in self.fields:
            if field.message:
                message = field.message
            else:
                message = self.message
            checked = False
            while not checked:
                print(f"{field.label}")
                value = input(self.prompt)
                if field.validator is not None:
                    checked = field.validator(value)
                    if not checked:
                        print(message)
                else:
                    checked = True
            setattr(response, field.name, value)
        return response
