import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Bot.bot import Bot
from src.Bot.config import COMMAND_LIST,HELP_FILE
from src.Bot.request import Request
from src.Bot.cine import Cine
from src.Bot.cine import RequestError
from src.Bot.itinerary import Itinerary, ParameterException
from src.Bot.news import News
from src.Bot.opinion import Opinion, MongoConnector
from src.Bot.resto import Resto, RequestError
from src.Bot.weather import Weather