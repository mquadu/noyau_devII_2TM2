from src.data.config import COMMAND_LIST
from src.request.request import Request
from src.bot.bot import Bot

if __name__ == "__main__":
    print("\t-----  BIENVENUE SUR LE CHATBOT EXTERNE -----\n")
    print("--Entrez /help pour voir la liste des commandes disponibles et leurs utilitées --\n\n ")
    while True:
        rep = input("Entrez une commmande ou exit pour quitter:\t")
        if rep == "exit":
            break
        message = Request(rep)

        print(Bot(message, COMMAND_LIST), "\n")

