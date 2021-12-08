from Module.weather.weather import Weather
from Module.itinerary.itinerary import Itinerary
from Module.news.news import News
from Module.cine.cine import Cine
from Module.resto.resto import Resto
from Module.data.config import HELP_FILE


class Bot:
    # Mettre le chemin du fichier dans un fichier de configuration
    def __init__(self, message, command_list: list, opinion: str = "", help_file=HELP_FILE):
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
            with open(self.help) as help:
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
                print(News().get_news())

            elif message[0] == "/cine":
                if len(message) > 2:
                    return self.error
                if len(message) == 2:
                    return Cine(message[1]).get_cine()
                if len(message) == 1:
                    return Cine().get_cine()

            elif message[0] == "/resto":
                if len(message) > 2:
                    return self.error
                if len(message) == 2:
                    return Resto(message[1]).get_resto()
                if len(message) == 1:
                    return Resto().get_resto()

            elif message[0] == "/opinion":
                pass
        elif isinstance(message, str):
            return message
