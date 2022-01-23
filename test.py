#Utilisation du package Bot-Externe
# Executer les commandes suivantes dans un terminal

#Windows

#python3 -m venv env
#.\env\Scritps\Activate.ps1
#pip install Bot-Externe

#Linux

#python3 -m venv env
#source env/bin/activate
#pip install Bot-Externe

#PUIS TESTER LE MODULE DE CETTE FACON : 
from Bot.bot import Bot

if __name__ == "__main__":
    
    print(Bot("/cine"))

