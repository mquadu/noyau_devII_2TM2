#Nathan Sancke
import os
import sys
import requests


class News:
    def __init__(self, country: str = "be", languages: str = "fr"):
        self.__country = "&country="+country
        self.__languages = "&languages="+languages
        self.__api_link = f"http://api.mediastack.com/v1/news?access_key=4a9e07d9cfd75c8d73c70f90ed4846f5"

    @property
    def country(self):
        return self.__country

    @property
    def api_link(self):
        return self.__api_link

    @property
    def languages(self):
        return self.__languages

    def get_news(self):
        """
        Renvoie les news

        PRE : Utilise le parametre weather qui est la ville possible que l'utilisateur doit entrer
        POST : Renvoie une chaine contenant la température qu'il fait dans la ville
        """
        response = requests.get(self.api_link+self.country+self.languages)
        current = response.json()
        return current

