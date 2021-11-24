import os
import sys

import requests

from Module.data.codesTemps import codesTemps


class Weather:
    def __init__(self, city: str = "Louvain-la-Neuve", day: int = 1):
        self.__city = city
        self.__api_link = f"http://api.weatherstack.com/current?access_key=4c53b8fcf4818536539b668a0247408c&query=" \
                          f"{self.weather_parameter} "

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def api_link(self):
        return self.__api_link

    @api_link.setter
    def api_link(self, api_link):
        self.__api_link = api_link

    def get_weather(self):
        """Renvoie la température de la ville

        PRE : Utilise le parametre weather qui est la ville possible que l'utilisateur doit entrer
        POST : Renvoie une chaine contenant la température qu'il fait dans la ville
        """
        response = requests.get(self.api_link)
        current = response.json()
        return f"La température de {self.city} est de {current['current']['temperature']}°C et " \
               f"il fait {codesTemps[current['current']['weather_code']]}"
