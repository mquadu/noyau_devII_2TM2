from unittest import TestCase
from Module.bot.bot import Bot
from Module.data.config import COMMAND_LIST, HELP_FILE
from Module.request.request import Request


class TestBot(TestCase):

    def setUp(self) -> None:
        self.true_command_list = COMMAND_LIST
        self.false_command_list_1 = ["/", "/help", "inutile", "/zarbi"]
        self.message_1 = Request("/help")
        self.message_2 = ["/cine", "namur"]
        self.message_3 = ["/resto"]  # Dans le cas ou on ne precise pas doit renvoyer celle de louvain-la-neuve
        self.message_4 = ["/zerjizoiejr", "je ne suis pas une commande"]

    def test_init(self):
        pass

    def test_get_help(self):
        # self.assertRaises(FileNotFoundError, Bot(Request("/help"), self.true_command_list).get_help, "")
        self.assertEqual(Bot(Request("/help"), self.true_command_list).get_help(HELP_FILE), "")

    def test_process_request(self):
        # self.assertEqual(Bot(self.message_1, self.true_command_list).get_help(HELP_FILE), "")

        self.assertEqual(len(Bot(Request("/itinerary louvain-la-neuve ottignies"), self.true_command_list).process_request(Request("/itinerary louvain-la-neuve ottignies").get_message(self.true_command_list))), 1201)
        self.assertEqual(len(Bot(Request("/cine namur"), self.true_command_list).process_request(Request("/cine namur").get_message(self.true_command_list))), 169)
        self.assertEqual(len(Bot(Request("/news basket"), self.true_command_list).process_request(Request("/news basket").get_message(self.true_command_list))), 89)
        self.assertEqual(len(Bot(Request("/cine"), self.true_command_list).process_request(Request("/cine").get_message(self.true_command_list))), 95)
