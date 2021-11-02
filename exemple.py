#! /usr/bin/env python3
# coding: utf-8


# exemple d'utilisation :
# un handler renvoie vers la fonction apropriée


from flamewok.views import Menu, Form


def handler(response):
    """renvoie vers diverses fonctions suivant la reponse"""
    print(f"<< {response} >>")

    actions = {
        # dans un vrai programme, chaque clé renvoie un nom de
        # fonction exemple:
        # "go_fonction_truc" : fonction_truc,
        "go_back": "back",
        "go_choice1": "action1",
        "go_choice2": "action2",
        "go_yes": "yes !",
        "go_no": "no !",
        "go_copy": "do copy...",
        "go_exit": "do exit",
        "go_modify": "do modif",
        "go_save": "do save",
    }
    print(actions[response[0]])
    # dans un vra programme on fera plutôt:
    # action[response[0]](response[1:])
    for arg in response[1:]:
        print("parameters : ")
        print(actions[arg])


menu1 = [
    "\nMon menu\n",
    (0, "back", "go_back"),
    (1, "choix 1", "go_choice1"),
    "\n autre:\n",
    (2, "choix 2", "go_choice2"),
    (3, "choix 1 et 2", "go_choice1", "go_choice2")
]

menu2 = [
    (0, "retour", "go_back"),
    (1, "yes", "go_yes"),
    (2, "no", "go_no"),
    ("c", "copy", "go_copy"),
    ("x", "exit", "go_exit"),
    ("modif", "modify", "go_modify"),
]


form = Form(
    [
        ("name", "Name of the caracter"),
        ("age", "Age of the caracter"),
        ("size", "size of the caracter"),
    ]
)


if __name__ == "__main__":
    print("exemple d'utilisation de la classe Menu")
    handler(Menu(menu1).response)
    handler(Menu(menu2, box_size=20).response)
    res = form.ask()
    res2 = form.ask()
    print(f"Nom : {res.name}, taille : {res.size}, age: {res.age}")
    print(f"Nom : {res2.name}, taille : {res2.size}, age: {res2.age}")
