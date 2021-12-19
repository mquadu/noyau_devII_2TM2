from unittest import TestCase
from itinerary import Itinerary, ParameterException
from Module.data.itinerary_json import itinerary_lln_ottignies


class TestItinerary(TestCase):
    def setUp(self) -> None:
        # Definir une instance de la classe et la tester

        self.itinerary_lln_ottignies = Itinerary("ottignies")

        self.itinerary_wavre_ottignies = Itinerary("wavre", "ottignies")

    def test_init(self):
        self.assertRaises(ParameterException, Itinerary(""))

        self.assertEqual(self.itinerary_wavre_ottignies.url_address_origin,
                         'https://nominatim.openstreetmap.org/search/wavre?format=json')
        self.assertEqual(self.itinerary_wavre_ottignies.url_address_destination,
                         'https://nominatim.openstreetmap.org/search/ottignies?format=json')

    def test_get_itinerary(self):
        self.assertEqual(self.itinerary_lln_ottignies.get_itinerary(), itinerary_lln_ottignies)

        # self.assertEqual(self.itinerary_lln_ottignies.get_itinerary(),
        #                  "Mauvaise syntaxe veuillez entrez /help pour plus de précision!")
        #
        # self.assertIsNotNone(self.itinerary_wavre_ottignies.get_itinerary())

