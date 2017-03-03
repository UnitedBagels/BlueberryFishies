import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')
# werpt is a giraffwe lmao u foshfghvc

# A Float layout positions and sizes objects as a percentage
# of the window size
class HomePage(Screen):
    pass

class MedicationPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class FloatingApp(App):
    def build(self):
        return FloatLayout()

flApp = FloatingApp()

flApp.run()
