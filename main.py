from src.Bot.bot import Bot


if __name__ == "__main__":
    print("\t-----  BIENVENUE SUR LE CHATBOT EXTERNE -----\n")
    print("--Entrez /help pour voir la liste des commandes disponibles et leurs utilitées --\n\n ")
    while True:
        rep = input("Entrez une commmande ou exit pour quitter:\t")
        if rep == "exit":
            print("\t-- Merci --\n")
            break

        print(Bot(rep), "\n")

