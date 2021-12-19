from django.http import HttpResponse
import unittest
from cine import Cine
import requests
from Module.data.config import cine_link


class TestCine(unittest.TestCase):
    def setUp(self) -> None:
        self.cine1 = Cine()
        url_origin = "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails" \
                     "=1&q=cinema+Louvain-la-Neuve&format=json"
        self.response = requests.get(url_origin).json()

    def test_url(self):
        self.assertEqual(Cine('Louvain-la-Neuve').url_origin,
                         "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails"
                         "=1&q=cinema+Louvain-la-Neuve&format=json")
        self.assertEqual(Cine('Namur').url_origin,
                         "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails"
                         "=1&q=cinema+Namur&format=json")

    def test_get_cine(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertRaises(ConnectionError, Cine, Cine.origin)


