import os
import sys

from Module.message.message import Message
from Module.weather.weather import Weather


class Bot:
    # Mettre le chemin du fichier dans un fichier de configuration
    def __init__(self, message, command_list: list, opinion: str = "", help_file=sys.path[0]):
        self.__help = help_file
        self.__message = message.get_message(command_list)
        if self.__message:
            print(self.get_request(self.__message))

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

    def get_request(self, message):
        """
        Sonde selon la requete et
        """
        if isinstance(message, list):
            if message[0] == "/weather":
                return Weather().get_weather()
            elif message[0] == "/help":
                return self.get_help()
        elif isinstance(message, str):
            return message
