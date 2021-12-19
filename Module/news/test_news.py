import unittest
from Module.news.news import *


class TestNews(unittest.TestCase):
    def setUp(self) -> None:
        self.news1 = News('fr')
        self.news2 = News('tennis')
        self.news3 = News('qshgnhyrqETVUHQSUUQETUNDol')
        self.news4 = News('af')
        self.news5 = News('fr')
        self.news5.api_link = "plusLeBonLien"
        self.date = str(datetime.date.today())

    def test__init__(self):
        self.assertEqual(self.news1.argument, 'fr')
        self.assertEqual(self.news2.argument, 'tennis')

        self.assertEqual(self.news1.date, "&date=" + self.date)
        self.assertEqual(self.news2.date, "&date=" + self.date)

    def test_get_news(self):
        self.assertEqual(len(self.news1.get_news().split("\n")), 10)
        self.assertEqual(len(self.news2.get_news().split("\n")), 10)
        self.assertEqual(self.news3.get_news(),
                         "Désolé nous n'avons pas trouvé d'article en français pour le pays ou le sujet sélectionné")
        self.assertEqual(self.news4.get_news(),
                         "Désolé nous n'avons pas trouvé d'article en français pour le pays ou le sujet sélectionné")
        self.assertEqual(self.news5.get_news(), "Erreur dans le get")


if __name__ == '__main__':
    unittest.main()
