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
        un élément à taper,
        une descrition de l'action
        un ou plusieurs signaux renvoyés
        - des str à inserer (ex: "\n")
        """
        self.prompt = prompt
        self.affichage = ""
        self.action = {}
        self.response = None

        for el in liste:
            box_number = 0
            if type(el) == str:
                self.affichage += el
            else:
                if box_number >= line_length // box_size:
                    self.affichage += "\n"
                    box_number = 0
                else:
                    box_number += 1
                    box = ""
                    box += f"{el[0]} : {el[1]}"
                    self.action[str(el[0])] = el[2:]
                    self.affichage += f"{box[:box_size]:<{box_size}}{sep}"

        self.affiche()

    def affiche(self):
        print(self.affichage)
        self.input()

    def input(self):
        choice = input(self.prompt)
        if choice in self.action:
            self.response = self.action[choice]
            self.send_response()
        else:
            self.affiche()

    def send_response(self):
        if self.response:
            return self.response
        else:
            self.affiche()
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
    - str(question à afficher)
    - str(clé d'enregistrment de la réponse)
    """
    def __init__(self, liste, prompt="> "):
        self.response = Response()
        for el in liste:
            print(f"{el[0]}")
            value = input(prompt)
            self.response.__setattr__(el[1], value)

    def get(self):
        return self.response
