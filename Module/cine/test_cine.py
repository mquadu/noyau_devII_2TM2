from unittest import TestCase
from cine import Cine
import requests

class TestCine(TestCase):
    def setUp(self):
        url_origin = "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails=1&q=cinema+Louvain-la-Neuve&format=json"
        self.response = requests.get(url_origin).json()

    def test_url(self):
        self.assertEqual(Cine('Louvain-la-Neuve'), "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails=1&q=cinema+louvain-la-neuve&format=json")
        self.assertEqual(Cine('Namur'), "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails=1&q=cinema+Namur&format=json")

    def test_get_cine(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertRaises(()


    pass
