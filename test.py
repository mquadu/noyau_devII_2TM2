from src.libs.Module import Request
from src.Module.bot import Bot

if __name__ == "__main__":
    rep = input("Entrez une commmande \t")  # La classe request doit récupérer le request de l'utilisateur et son

    command_list = ["/help", "/weather", "/itinerary", "/resto", "/cine", "/news", "/opinion"]

    message = Request(rep)
    print(message.get_message(command_list))
    print(Bot(message, command_list))
