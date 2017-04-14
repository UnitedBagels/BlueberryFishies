from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.config import Config
from kivy.core.window import Window
import webbrowser
"""Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')"""
Window.size = (480, 800)
#dan@finisventures.com

class HomePage(Screen):
    Window.clearcolor = (1, 1, 1, 1)
    pass

class DietPage(Screen):
    pass

class ExercisePage(Screen):
    pass

class MedicationPage(Screen):
    pass

class GoalsPage(Screen):
    pass

class LifePage(Screen):
    pass

class SettingsPage(Screen):
    pass

class ScreenManagement(ScreenManager):

    # addMedication
    instances = 0
    yPos = 0.825

    def SodiumDietBrowser(self):
        webbrowser.open_new("http://allrecipes.com/recipes/1788/healthy-recipes/low-sodium/")
    def FatDietBrowser(self):
        webbrowser.open_new("http://allrecipes.com/recipes/1231/healthy-recipes/low-fat/")
    def DiabeticBrowser(self):
        webbrowser.open_new("http://allrecipes.com/recipes/739/healthy-recipes/diabetic/")
    def addMedication(self):
        pass
        """self.instances += 1
        self.addYPos += .5
        button = self.ids['add_button']
        button.pos_hint = {"center_x": .1, "center_y": self.addYPos}"""

presentation = Builder.load_file("style.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
