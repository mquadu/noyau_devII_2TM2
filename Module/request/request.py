# Recupère les messages de discord
# -*- coding: utf-8 -*-
class Request:
    def __init__(self, message: str):
        self.__message = message

    @property
    def message(self):
        return self.__message
    
    def set_message(self, message: str):
        self.__message = message

    def get_message(self, command_list):
        message_words = self.message.split(" ")
        if message_words[0][0] == "/" and message_words[0] in command_list:
            return message_words

        elif message_words[0][0] == "/" and message_words[0] not in command_list:
            self.set_message("Commande introuvable! Entrez /help pour voir la liste des commandes")
            return self.message
        else:
            self.set_message("Commande introuvable! Entrez /help pour voir la liste des commandes")
            return self.message

        # elif rep_split[0] == "/weather":
        #
        #     if len(rep_split) == 2:
        #         commande = Commande(rep_split[1]).weather
        #         print(commande)
        #     else:
        #         commande = Commande().weather
        #         print(commande)
        # else:
        #     print("Erreur dans la weather!")
