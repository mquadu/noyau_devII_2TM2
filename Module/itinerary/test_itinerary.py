from unittest import TestCase
from itinerary import Itinerary, ParameterException
from Module.data.itinerary_json import itinerary_lln_ottignies


class TestItinerary(TestCase):
    def setUp(self) -> None:
        self.itinerary_lln_ottignies = Itinerary(destination_address="ottignies")

        self.itinerary_bruxelle_namur = Itinerary("bruxelle", "namur")

    def test_init(self):
        self.assertRaises(ParameterException, Itinerary, "", "")
        self.assertEqual(self.itinerary_lln_ottignies.origin_address, "louvain-la-neuve")
        self.assertEqual(self.itinerary_bruxelle_namur.destination_address, "namur")

    def test_url_address_origin(self):
        self.assertEqual(self.itinerary_lln_ottignies.url_address_origin,
                         'https://nominatim.openstreetmap.org/search/louvain-la-neuve?format=json', "Mauvais lien")
        self.assertEqual(self.itinerary_bruxelle_namur.url_address_origin,
                         'https://nominatim.openstreetmap.org/search/bruxelle?format=json', "Mauvais Lien")

    def test_url_address_destination(self):

        self.assertEqual(self.itinerary_lln_ottignies.url_address_destination,
                         'https://nominatim.openstreetmap.org/search/ottignies?format=json', "Mauvais lien")
        self.assertEqual(self.itinerary_bruxelle_namur.url_address_destination,
                         'https://nominatim.openstreetmap.org/search/namur?format=json', "Mauvais Lien")

    def test_process_request(self):
        request = self.itinerary_lln_ottignies.process_request()
        self.assertEqual(self.itinerary_lln_ottignies.process_request(), )

    def test_get_itinerary(self):

        self.assertEqual(self.itinerary_lln_ottignies.get_itinerary(), itinerary_lln_ottignies)



