
from flamewok import settings


class NoNameError(Exception):
    def __init__(self):
        message = "Field with no name error"
        super().__init__(message)


class Field:
    """a Form needs some Field"""
    def __init__(self, name=None, label=""):
        if name:
            self.name = name
            self.label = label
        else:
            raise NoNameError

    def __str__(self):
        return f"<Field | {self.name} -> {self.label}>"

    def __repr__(self):
        return str(self)


class Response:
    """Single empty class used for the Form response"""
    pass


class Form:
    """Give a list of fields
    fields are tuples made of 2 elements:
    - str(the key to register the answer)
    - str(the text to display)
    """
    def __init__(self, fields, prompt=settings.DEFAULT_FORM_PROMPT):
        self.prompt = prompt
        self.fields = []
        for el in fields:
            field = Field(el[0], el[1])
            self.fields.append(field)

    def ask(self):
        response = Response()
        for field in self.fields:
            print(f"{field.label}")
            value = input(self.prompt)
            setattr(response, field.name, value)
        return response
