import os
import kivy

kivy.require('2.0.0')
from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


# add the following 2 lines to solve OpenGL 2.0 bug
# from kivy import Config
# Config.set('graphics', 'multisamples', '0')

class TextBarre(App):
    def build(self):
        self.icon = 'hello.png'
        self.title = "Chatbot"
        box = BoxLayout(orientation='horizontal')
        box.add_widget(Label(text="input"))
        box.add_widget(TextInput())
        box.add_widget(Button(text='Enter'))

        Config.set('graphics', 'width', '350')
        Config.set('graphics', 'height', '50')
        return box


    # return Label(text='Hello World!', font_size='100sp')


class ChatBot(App):

    def build(self):
        text_barre = TextBarre()

        return text_barre.build()

    Config.set('graphics', 'width', '350')
    Config.set('graphics', 'height', '300')


ChatBot().run()
