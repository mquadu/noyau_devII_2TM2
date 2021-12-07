import os
import kivy

kivy.require('2.0.0')

# from kivy.app import App
# from kivy.config import Config
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.label import Label
# from kivy.graphics import Color, Rectangle
# from kivy.uix.widget import Widget


# Module for kivymd

from kivymd.app import MDApp
from kivy.lang import Builder

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class ChatBot(MDApp):
    def build(self):
        return Builder.load_file("view/interface.kv")


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
