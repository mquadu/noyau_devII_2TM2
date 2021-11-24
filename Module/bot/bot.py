import os
import sys
from ..weather.weather import Weather

class Bot:
    def __init__(self, help_file=sys.path[0]):
        self.__help = help_file

    @property
    def help(self):
        return self.__help

    def get_help(self):
        """
        Renvoie toutes les commandes possible et leur description
        PRE : Prend un fichier contenant les commandes et leur description
        """
        try:
            with open(os.path.join(self.help, "data/help.txt")) as help:
                print(help.read())
        except FileNotFoundError:
            print("Fichier Introuvable")