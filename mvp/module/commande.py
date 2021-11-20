from module.codesTemps import codesTemps
import requests
import sys
import os

class Commande:
    def __init__(self, parametreWeather="Louvain-la-Neuve"):
        self.parametreWeather = parametreWeather

    def help(self):
        try:
            with open(os.path.join(sys.path[0] , "data\help.txt")) as help:
                print(help.read())
                print(sys.path[0])
        except FileNotFoundError:
            print("Fichier Introuvable")

    @property
    def weather(self):
        # print(self.parametreWeather)
        reponse = requests.get(
            f"http://api.weatherstack.com/current?access_key=4c53b8fcf4818536539b668a0247408c&query={self.parametreWeather}")  # se connecte à l'API de weatherStack
        current = reponse.json()
       # print(current)
        print(
            f"La température de {self.parametreWeather} est de {current['current']['temperature']}°C et il fait {codesTemps[current['current']['weather_code']]}")

        # print(reponse.json()["current"]["weather_code"])
