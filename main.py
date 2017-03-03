from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class HomePage(Screen):
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

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("style.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
