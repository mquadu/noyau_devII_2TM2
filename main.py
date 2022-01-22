import os
import sys

import kivy

from src.models.screens_manager import ScreensManager

from kivy.app import App
from kivy.lang import Builder
from src.libs.Module.data.config import VIEWS_DIR

if sys.platform == "win32":
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
