from ..data.config import resto_link
import requests


class Resto:

    def __init__(self, origin='Louvain-la-Neuve'):
        self.__origin = origin
        self.__url_origin = resto_link(self.__origin)

    def get_resto(self):
        response = requests.get(self.__url_origin).json()

        print(response)

        for i in response:
            return f"{i['display_name']}\n"
