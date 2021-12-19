import os
import unittest
from Module.data.config import *
from Module.request.request import Request
from Module.itinerary.test_itinerary import TestItinerary
from Module.bot.bot import Bot

if __name__ == "__main__":
    TestItinerary()
    rep = input("Entrez une commmande \t")  # La classe request doit récupérer le request de l'utilisateur et son

    command_list = ["/help", "/weather", "/itinerary", "/resto", "/cine", "/news", "/opinion"]

    message = Request(rep)
    print(message.get_message(command_list))
    print(Bot(message, command_list))
