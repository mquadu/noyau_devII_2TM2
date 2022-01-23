import logging
from src.Bot.bot import Bot


if __name__ == "__main__":
    logging.basicConfig(filename='main.log',  filemode='a', format='%(asctime)s-%(levelname)s-%(message)s',  datefmt='%Y-%m-%d %H:%M:%s') #level=logging.DEBUG,

    logging.warning("ceci est un warning dans les logs")
    print("\t-----  BIENVENUE SUR LE CHATBOT EXTERNE -----\n")
    print("--Entrez /help pour voir la liste des commandes disponibles et leurs utilitées --\n\n ")
    while True:
        rep = input("Entrez une commmande ou exit pour quitter:\t")
        if rep == "exit":
            print("\t-- Merci --\n")
            break

        print(Bot(rep), "\n")

