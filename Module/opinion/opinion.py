#Noé Libon
#https://www.w3schools.com/python/python_mongodb_getstarted.asp


from pymongo import MongoClient


class Opinion:
    def __init__(self, is_positif=5, message="super"):
        self.__opinion = is_positif
        self.__message = message
        self.send_db()

    def send_db(self):
        #client = MongoClient("mongodb+srv://noeli:user123@pyp.ajkyd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        client = MongoClient("mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
        db = client["ephecom-2TM2"]
        collection_opinions = db.opinions
        personal_opinion = {
                "opinion" : self.__opinion,
                "message" : self.__message
                }
        collection_opinions.insert_one(personal_opinion)
        print(client.list_database_names())
        db_list = client.list_database_names()
        if "ephecom-2TM2" in db_list:
            print("The database exists.")
        else:
            print("Doesn't exists ! ")



#test
test_default = Opinion()
test_modified = Opinion(is_positif=2, message="pas ouf")