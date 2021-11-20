import os
import sys

import requests

from mvp.data.codesTemps import codesTemps


class Commande:
    def __init__(self, weather_parameter="Louvain-la-Neuve"):
        self.weather_parameter = weather_parameter
        self.__api_link = f"http://api.weatherstack.com/current?access_key=4c53b8fcf4818536539b668a0247408c&query=" \
                          f"{self.weather_parameter} "

    @property
    def api_link(self):
        return self.__api_link

    @api_link.setter
    def api_link(self, api_link):
        self.__api_link = api_link

    def help(self):
        """
        Renvoie toutes les commandes possible et leur description
        PRE : Prend un fichier contenant les commandes et leur description
        """
        try:
            with open(os.path.join(sys.path[0], "data/help.txt")) as help:
                print(help.read())
        except FileNotFoundError:
            print("Fichier Introuvable")

    @property
    def weather(self):
        """Renvoie la température de la ville

        PRE : Utilise le parametre weather qui est la ville possible que l'utilisateur doit entrer
        POST : Renvoie une chaine contenant la température qu'il fait dans la ville
        """
        response = requests.get(self.api_link)
        current = response.json()
        return f"La température de {self.weather_parameter} est de {current['current']['temperature']}°C et " \
               f"il fait {codesTemps[current['current']['weather_code']]}"
