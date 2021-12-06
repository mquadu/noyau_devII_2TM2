#Noé Libon
#https://www.w3schools.com/python/python_mongodb_getstarted.asp

import pymongo
from pymongo import MongoClient


class Opinion:
    def __init__(self, is_positif=5, message="super"):
        self.__opinion = is_positif
        self.__message = message
        self.send_db()

    def send_db(self):
        client = MongoClient("mongodb+srv://noeli:user123@pyp.ajkyd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client["Opinions"]
        collection = db.opinion
        votes = {
                "opinion" : self.__opinion,
                "message" : self.__message
                }
        collection.insert_one(votes)
        print(client.list_database_names())
        db_list = client.list_database_names()
        if "Opinions" in db_list:
            print("The database exists.")
        else:
            print("Doesn't exists ! ")



#test
test_default = Opinion()
test_modified = Opinion(is_positif=2, message="pas ouf")