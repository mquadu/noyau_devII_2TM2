from Module.data.config import COMMAND_LIST
from Module.request.request import Request
from Module.bot.bot import Bot

if __name__ == "__main__":
    while True:
        rep = input("Entrez une commmande ou exit pour quitter\t")
        if rep == "exit":
            break
        message = Request(rep)
        print(message.get_message(COMMAND_LIST))
        print(Bot(message, COMMAND_LIST))

