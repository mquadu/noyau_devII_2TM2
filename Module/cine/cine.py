# Marina
from ..data.config import cine_link
import requests


class Cine:
    def __init__(self, origin='Louvain-la-Neuve'):
        self.__origin = origin
        self.__url_origin = cine_link(self.origin)

    @property
    def url_origin(self):
        return self.__url_origin

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin):
        self.__origin = origin

    def get_cine(self):
        """
        PRE : "/cine"
        POST : liste des cinemas du lieu passé en paramètre (par défaut LLN)
        RAISES : exception : si pas de réponse à la requete
        """
        try:
            response = requests.get(self.url_origin).json()
        except ValueError:
            return "Can't fetch Cinema"

        cine = ""
        for i in response:
            cine += "\n"
            for address in i["address"]:
                if address not in ["country", "country_code", "region", "postcode", "county"]:
                    cine += f"{i['address'][address]} "
            cine += "\n"
        return cine

