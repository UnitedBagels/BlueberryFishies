from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.config import Config
from kivy.core.window import Window
import webbrowser
"""Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')"""
Window.size = (480, 800)
#dan@finisventures.com

class CheckBox(ToggleButton):
    pass

class HomePage(Screen):
    Window.clearcolor = (1, 1, 1, 1)
    pass

class DietPage(Screen):
    def SodiumDietBrowser(self):
        webbrowser.open_new("http://allrecipes.com/recipes/1788/healthy-recipes/low-sodium/")

    def FatDietBrowser(self):
        webbrowser.open_new("http://allrecipes.com/recipes/1231/healthy-recipes/low-fat/")

    def DiabeticBrowser(self):
        webbrowser.open_new("http://allrecipes.com/recipes/739/healthy-recipes/diabetic/")

class ExercisePage(Screen):
    pass

class MedicationPage(Screen):
    def MedicineGuide(self):
        webbrowser.open_new("https://www.fda.gov/Drugs/DrugSafety/ucm085729.htm")

class GoalsPage(Screen):
    pass

class LifePage(Screen):
    pass

class SettingsPage(Screen):

    yPos = 0.74

    def addMedication(self):
        self.add_widget(TextInput(
            background_color = (1, 1, 1, 1), # These two properties already exist in
            font_name = 'images/cambriab',   # CustTextInput, not sure how to get them back
            hint_text = "Enter Description",
            pos_hint = {"center_x": .385, "center_y": self.yPos},
            font_size = 25,
            size_hint = (.6, .055),
            multiline = False))
        self.add_widget(Spinner(
            pos_hint = {"center_x": .785, "center_y": self.yPos},
            size_hint = (.15, .05),
            text = "Time",
            background_color = (.502, .651, .671, 1),
            values = ('1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00'),
            font_name = 'images/cambriab'))
        print("helloi")

class PhysicalActivities(Screen):
    def PhysicalActivity(self):
        webbrowser.open_new("https://www.niddk.nih.gov/health-information/health-topics/weight-control/young-heart-tips-Older-adults/Pages/young-heart-tips-older-adults.aspx#physical_activity")

class ScreenManager():

    def notify(self):
        pass

    #def addMedication(self):
        #self.yPos -= 0.1
        #self.instances += 1
        #print(self.addButton.ids.add_button.state)
        #addButton.pos_hint = {"center_x": .1, "center_y": self.yPos}
        #print(addButton.pos_hint)"""

presentation = Builder.load_file("style.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()