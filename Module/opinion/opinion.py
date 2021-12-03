#Noé Libon
#https://www.w3schools.com/python/python_mongodb_getstarted.asp

import requests

class Opinion:
    def __init__(self, is_positif, message=""):
        self.__opinion = is_positif
        self.__message = message

    def send_DB(self):
        pass