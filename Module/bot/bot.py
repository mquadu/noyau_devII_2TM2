import os
import sys

from Module.request.request import Request
from Module.weather.weather import Weather
from Module.itinerary.itinerary import Itinerary


class Bot:
    # Mettre le chemin du fichier dans un fichier de configuration
    def __init__(self, message, command_list: list, opinion: str = "", help_file=sys.path[0]):
        self.__help = help_file
        self.__message = message.get_message(command_list)
        self.error = "Mauvaise syntaxe veuillez entrez /help pour plus de précision!"
        if self.__message:
            print(self.process_request(self.__message))

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

    def process_request(self, message):
        """
        Evalue la requête de l'utilisateur et appelle la classe correspondante
        """

        # message est une liste contenant la commande et les paramètres que l'utilisateur à entrer

        if isinstance(message, list):
            if message[0] == "/help":
                return self.get_help()

            elif message[0] == "/weather":
                return Weather().get_weather()

            elif message[0] == "/itinerary":
                # si on a plus que 2 paramètres , erreur
                if len(message) > 3 or len(message) <= 1:
                    return self.error
                if len(message) == 2:
                    return Itinerary(destination_address=message[1])
                if len(message) == 3:
                    return Itinerary(message[1], message[2])

            elif message[0] == "/news":
                pass

            elif message[0] == "/cine":
                pass

            elif message[0] == "/resto":
                pass

            elif message[0] == "/opinion":
                pass
        elif isinstance(message, str):
            return message
