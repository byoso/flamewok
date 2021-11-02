#! /usr/bin/env python3
# coding: utf-8


# exemple d'utilisation :
# un handler renvoie vers la fonction apropriée


from archi import Menu, Form


def handler(response):
    """renvoie vers diverses fonctions suivant la reponse"""
    print(f"<< {response} >>")

    actions = {
        # dans un vrai programme, chaque clé renvoie un nom de
        # fonction exemple:
        # "go_fonction_truc" : fonction_truc,
        "go_retour": "retour",
        "go_choix1": "action1",
        "go_choix2": "action2",
        "go_yes": "yes !",
        "go_no": "no !",
        "copy": "do copy...",
        "exit": "do exit",
        "modif_foo": "do modif",
        "save": "do save"

    }
    print(actions[response[0]])
    # dans un vra programme on fera plutôt:
    # action[response[0]](response[1:])
    for arg in response[1:]:
        print("parametres : ")
        print(actions[arg])

print("exemple d'utilisation de la classe Menu")

menu1 = [
    "\nMon menu\n",
    (0, "retour", "go_retour"),
    (1, "choix 1", "go_choix1"),
    "\n autre:\n",
    (2, "choix 2", "go_choix2"),
    (3, "choix 1 et 2", "go_choix1", "go_choix2")
]

menu2 = [
    (0, "retour", "go_retour"),
    (1, "yes", "go_yes"),
    (2, "no", "go_no"),
    ("c", "copy", "copy"),
    ("x", "exit", "exit"),
    ("modif", "modifier", "modif_foo"),
]

# handler(Menu(menu1).response)
handler(Menu(menu2, box_size=20).response)

form = Form(
    [
        ("Nom", "name"),
        ("Age", "age"),
        ("taille", "size"),
    ]
).get()

print(f"age : {form.age}, taille : {form.size}, age: {form.age}")
