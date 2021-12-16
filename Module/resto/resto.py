# Marina
from ..data.config import resto_link
import requests


class Resto:

    def __init__(self, origin='Louvain-la-Neuve'):
        self.__origin = origin
        self.__url_origin = resto_link(self.__origin)

    @property
    def url_origin(self):
        return self.__url_origin

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin):
        self.__origin = origin

    def get_resto(self):
        """
        PRE : "/resto"
        POST : liste des restos du lieu passé en paramètre (par défaut LLN)
        """
        try:
            response = requests.get(self.url_origin).json()
        except ValueError:
            return "Can't fetch Restaurant"
        restaurant = ""
        for i in response:
            restaurant += f"{i['display_name']}\n"
        return restaurant
