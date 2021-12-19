from unittest import TestCase
import resto
import requests
from ..data.config import cine_link


class TestResto(TestCase):
    def setUp(self) -> None:
        url_origin = "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails" \
                     "=1&q=cinema+Louvain-la-Neuve&format=json"
        self.response = requests.get(url_origin).json()

    def test_url(self):
        self.assertEqual(resto.Resto('Louvain-la-Neuve'),
                         "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails"
                         "=1&q=cinema+louvain-la-neuve&format=json")
        self.assertEqual(resto.Resto('Namur'),
                         "https://nominatim.openstreetmap.org/search?osmtype=N&addressdetails"
                         "=1&q=cinema+Namur&format=json")

    def test_get_cine(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertRaises(ConnectionError, resto.Resto, resto.Resto.origin)

    if __name__ == '__main__':
        unittest.main()
