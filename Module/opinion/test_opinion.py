import unittest
from Module.opinion.opinion import *
from pymongo import MongoClient
from Module.data.config import CERTIFICATE_FILE


class TestOpinion(unittest.TestCase, MongoConnector):
    def setUp(self):
        try:
            with MongoConnector() as connector:
                self.collection = connector.db["users"]
                res = self.collection.findOne()
                print(res)
        except Exception as e:
            print(e)

        for elem in self.collection.find():
            self.id = elem["_id"]
            print(self.id)

        self.rep1 = {'_id': 0, 'opinion': '4', 'message': "c'est trop bien"}
        self.rep2 = {'_id': 1, 'opinion': '5', 'message': ""}
        self.rep3 = {'_id': 2, 'opinion': '1', 'message': "nul"}

    def test_set_opinion(self):
        self.assertEqual(Opinion(is_positif=12).set_opinion(), "Choisissez plutôt un nombre entre 0 et 5 svp.")
        self.assertEqual(Opinion(is_positif=4, message="c'est trop bien").set_opinion(),
                         "Votre avis a bien été envoyé. Nous en tiendrons compte !")
        self.assertEqual(Opinion(is_positif=5).set_opinion(),
                         "Votre avis a bien été envoyé. Nous en tiendrons compte !")
        self.assertEqual(Opinion(is_positif=1, message="nul").set_opinion(),
                         "Votre avis a bien été envoyé. Nous en tiendrons compte !")
        for elem in self.collection.find():
            print(elem)

        self.assertEqual(self.collection.findOne({"_id": self.id + 1}), self.rep1)
        self.assertEqual(self.collection.findOne({"_id": self.id + 1}), self.rep2)
        self.assertEqual(self.collection.findOne({"_id": self.id + 1}), self.rep3)

        self.collection.delete_one(self.rep1['_id'])
        self.collection.delete_one(self.rep2['_id'])
        self.collection.delete_one(self.rep3['_id'])


if __name__ == '__main__':
    unittest.main()
