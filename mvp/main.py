"""
L’utilisateur aura une interface en ligne de commande dans laquelle il pourra rentrer la commande qui sera ensuite exécutée. 
Les commandes qui peuvent être exécutées seront help et weather auxquelles l’ordinateur renverra une réponse adéquate décrivant respectivement 
a liste des commandes disponibles et la météo.
"""


import sys
# from Projet.mvp.commande import Commande

import requests
from module.commande import Commande

# Commande pour le mvp : help et weather
# Une classe commande qui contient les fonctions

if __name__ == "__main__":
    rep = input("Entrez une commmande \t")
    repSplit = rep.split(" ")  # Cas ou il entre le weather avec paramètre

    if(repSplit[0] == "/help"):

        help = Commande().help()

    elif(repSplit[0] == "/weather"):

        if len(repSplit) == 2:
            commande = Commande(repSplit[1]).weather
        else:
            commande = Commande().weather

    else:
        print("Erreur dans la commande!")


"""
Exemple de retour json
{'request': {'type': 'City', 'query': 'Louvain-La-Neuve, Belgium', 'language': 'en', 'unit': 'm'}, 
'location': {'name': 'Louvain-La-Neuve', 'country': 'Belgium', 'region': '', 'lat': '50.683', 'lon': '4.617', 'timezone_id': 'Europe/Brussels', 'localtime': '2021-11-10 20:36', 'localtime_epoch': 1636576560, 'utc_offset': '1.0'}, 'current': {'observation_time': '07:36 PM', 'temperature': 7, 'weather_code': 113, 'weather_icons': ['https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear'], 'wind_speed': 0, 'wind_degree': 209, 'wind_dir': 'SSW', 'pressure': 1024, 'precip': 0, 'humidity': 81, 'cloudcover': 0, 'feelslike': 6, 'uv_index': 1, 'visibility': 9, 'is_day': 'no'}}
"""
