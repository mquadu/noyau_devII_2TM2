from OSMPythonTools.api import Api
import requests
import urllib.parse


class Itinerary:
    def __init__(self, origin_address="", destination_address=""):
        self.__origin_address = origin_address
        self.__destination_address = destination_address
        self.__url_address = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(
            destination_address) + '?format=json'
        self.print_latlon()

    @property
    def url_address(self):
        return self.__url_address

    def print_latlon(self):
        response = requests.get(self.url_address).json()
        print(response[0]["lat"])
        print(response[0]["lon"])
