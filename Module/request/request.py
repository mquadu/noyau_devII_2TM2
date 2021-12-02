# Recupère les messages de discord

class Request:
    def __init__(self, message: str):
        self.__message = message

    @property
    def message(self):
        return self.__message
    
    def set_message(self, message: str):
        self.__message = message

    def get_message(self, command_list):
        # if self.request[0][0] == "/":
        # request = self.request.split(" ")  # Cas ou il entre le weather avec paramètre
        message_words = self.message.split(" ")
        if message_words[0][0] == "/" and message_words[0] in command_list:
            return message_words

        elif message_words[0][0] == "/" and message_words[0] not in command_list:
            print(message_words[0])
            self.set_message("Commande introuvable!")
            return self.message
        else:
            return

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
