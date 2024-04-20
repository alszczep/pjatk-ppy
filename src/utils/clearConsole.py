from os import system, name


def clearConsole():
    if name == "nt":
        system("cls")
    else:
        system("clear")
