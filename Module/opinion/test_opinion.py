from unittest import TestCase
from opinion import *

class TestOpinion(TestCase):
    def setUp(self):
        self.first_op = Opinion(is_positif=12)
        self.second_op = Opinion(is_positif=2, message="pas ouf")
        self.third_op = Opinion(is_positif=5, username="jojo")
        self.fourth_op = Opinion(is_positif=1, message="nul", username="toto")

    def test_init(self):
        self.assertEqual(self.first_op, "Choisissez plutôt un nombre entre 0 et 5 svp.")
        