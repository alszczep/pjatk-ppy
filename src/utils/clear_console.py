from os import system, name


def clear_console():
    if name == "nt":
        system("cls")
    else:
        system("clear")
