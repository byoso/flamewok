#! /usr/bin/env python3
# coding: utf-8


"""Ce module facilite la mise en place de vues dans un programme en
console, grâce au classes Menu et Form"""


class Menu:
    """Menu construit l'affichage d'un menu et emmet un signal en fonction
    de la réponse"""
    def __init__(
        self, liste, sep=" | ",
        box_size=20,
        line_length=80,
        prompt="?> "
            ):
        """La liste doit contenir:
        - des tuples construits ainsi:
        un élément à taper pour faire son choix,
        une descrition de l'action,
        un ou plusieurs signaux renvoyés
        - des str à inserer (ex: "\n")
        """
        self.prompt = prompt
        self.body = ""
        self.action = {}
        self.response = None

        # manage the number of dialog boxes per line
        box_number = line_length // box_size
        for el in liste:
            if type(el) == str:
                self.body += el
            else:
                if box_number == 0:
                    self.body += "\n"
                    box_number = line_length // box_size

                box_number -= 1
                box = ""
                box += f"{el[0]} : {el[1]}"
                self.action[str(el[0])] = el[2:]
                self.body += f"{box[:box_size]:<{box_size}}{sep}"

        self.show()

    def show(self):
        print(self.body)
        self.input()

    def input(self):
        choice = input(self.prompt)
        if choice in self.action:
            self.response = self.action[choice]
            self.send_response()
        else:
            self.show()

    def send_response(self):
        if self.response:
            return self.response
        else:
            self.show()
            self.input()


class Handler:
    """Redirects a signal to a function. This class is expected to be
    inherited from"""
    pass


class Response:
    """Single empty class used for the Form response"""
    pass


class Form:
    """Fournir une liste de tuples de 2 éléments:
    - str(clé d'enregistrment de la réponse)
    - str(question à afficher)
    """
    def __init__(self, liste, prompt="> "):
        self.prompt = prompt
        self.liste = liste

    def ask(self):
        response = Response()
        for el in self.liste:
            print(f"{el[1]}")
            value = input(self.prompt)
            response.__setattr__(el[0], value)
        return response
