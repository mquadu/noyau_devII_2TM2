import os
import sys

import kivy

from src.models.mongo_connector import MongoConnector
from src.models.screens_manager import ScreensManager

from kivy.app import App
from kivy.lang import Builder
from Module.data.config import VIEWS_DIR

kivy.require('2.0.0')
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

if sys.platform == "win32":
    Builder.load_file("{0}\\common.kv".format(VIEWS_DIR))
if sys.platform == "linux":
    Builder.load_file("{0}/common.kv".format(VIEWS_DIR))


class ChatBot(App):
    title = 'Chabot'

    def build(self):
        from src.views.landing import LandingScreen

        sm = ScreensManager()
        landing_screen = LandingScreen()
        sm.add_widget(landing_screen)
        sm.current = "landing"
        landing_screen.set_teams_list()
        return sm


if __name__ == "__main__":
    ChatBot().run()

# add the following 2 lines to solve OpenGL 2.0 bug
# from kivy import Config
# Config.set('graphics', 'multisamples', '0')

#
# class ChatBot(App):
#     def __init__(self):
#         super().__init__()
#         self.input_space = TextInput(size_hint=(0.6, 0.1), pos=(0.2, 0), halign="auto")
#         self.output_space = Label(text='', size_hint=(0.6, 0.9), pos=(0.2, 1))
#
#     def build(self):
#         self.icon = 'hello.png'
#         self.title = "Chatbot"
#         box_input = BoxLayout(orientation='horizontal')
#         input_text = Label(text="input", size_hint=(0.2, 0.1), pos=(0, 0))
#         send_button = Button(text='Enter', size_hint=(0.2, 0.1), pos=(0.8, 0))
#
#         with input_text.canvas:
#             Color(0, 1, 0, 0.25)
#             Rectangle(pos=input_text.pos, size_hint=(0.2, 0.3))
#
#         box_input.add_widget(input_text)
#         box_input.add_widget(self.input_space)
#         box_input.add_widget(send_button)
#
#         box_output = BoxLayout(orientation='horizontal')
#         box_output.add_widget(self.output_space)
#         # box_output.add_widget(Label)
#
#         box = BoxLayout(orientation='horizontal')
#         box.add_widget(box_input)
#         # box.add_widget(box_output)
#
#         send_button.bind(on_press=self.send_info)
#         return box
#
#     def send_info(self, source):
#         print(self.input_space.text)
#         return self.input_space.text

# def display_info(self):


# class ChatBot(App):
#
#     def build(self):
#         return TextBarre().build()
#
#     def text_user(self):
#         return TextBarre()._send_info()
#
#     Config.set('graphics', 'width', '350')
#     Config.set('graphics', 'height', '50')


# ChatBot().run()


# from request.request import Request
# from bot.bot import Bot
# # from app import ChatBot
#
#
# if __name__ == "__main__":
#     rep = input("Entrez une commmande \t")  # La classe request doit récupérer le request de l'utilisateur et son
#     # pseudo
#     # ChatBot.run()
#
#     # rep = ChatBot.send_info("")
#
#     # print(rep)
#     command_list = ["/help", "/weather", "/itinerary", "/resto", "/cine", "/news", "/opinion"]
#     message = Request(rep)
#     Bot(message, command_list)
#
