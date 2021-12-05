#Noé Libon
#https://www.w3schools.com/python/python_mongodb_getstarted.asp

import pymongo


class Opinion:
    def __init__(self, is_positif, message=""):
        self.__opinion = is_positif
        self.__message = message
        self.send_db()

    def send_db(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["Opinions"]
        print(client.list_database_names())
        db_list = client.list_database_names()
        if "mydatabase" in db_list:
            print("The database exists.")
        else:
            print("Doesn't exists ! ")
