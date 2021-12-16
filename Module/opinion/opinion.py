#Noé Libon
#connexion: mongosh "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom-2TM2?authSource=%24external&authMechanism=MONGODB-X509" --tls --tlsCertificateKeyFile C:\Users\noeli\Desktop\TI\Bloc2\Q1\Dev2\Projets\PythonChatBot\noyau_devII_2TM2\Module\data\X509-cert-5486301905818120966.pem

from pymongo import MongoClient
from Module.data.config import *

class MongoConnector:
    
    def __init__(self):
        certificat_path = CERTIFICATE_FILE
        uri = "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom-2TM2?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
        client = MongoClient(uri,
                             tls=True,
                             tlsCertificateKeyFile=certificat_path)
        self.db = client["ephecom-2TM2"]
    
    def __enter__(self):
        return self
    
    def __exit__(self):
        self.db.close()


class Opinion:
    def __init__(self, is_positif=5, message="super"):
        try:
            with MongoConnector() as connector:
                collection = connector.db["users"]
                res = collection.find_one()
                print(res)
        except Exception as e:
            print(e)
        
    """    
        self.__opinion = is_positif
        self.__message = message
        self.send_db()


    def send_db(self):
        client = MongoClient("mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom-2TM2?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
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
    """

o = Opinion()