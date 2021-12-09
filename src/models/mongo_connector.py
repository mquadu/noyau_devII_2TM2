from pymongo import MongoClient

from Module.data.config import CERTIFICATE_FILE
from Module.data.config import ROOT_DIR


class MongoConnector:
    """
        Cette classe permet de créer une connexion vers la base de données.

        Veuillez modifier la variable 'certificat_path' avec le chemin vers l'endroit ou se trouve votre certificat.

        Exemple d'utilisation dans votre code :

        try:
            with MongoConnector() as connector:
                collection = connector.db["users"]
                res = collection.find_one()
                print(res)
        except Exception as e:
            print(e)
    """

    def __init__(self):
        # certificat_path = ROOT_DIR + "/certif_mongo.pem"
        uri = "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom-2TM2?authSource=%24external&authMechanism=MONGODB-X509" \
              "&retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
        client = MongoClient(uri,
                             tls=True,
                             tlsCertificateKeyFile=CERTIFICATE_FILE)
        self.db = client['ephecom-2TM2']

    def __enter__(self):
        return self

    def __exit__(self):
        self.db.close()
