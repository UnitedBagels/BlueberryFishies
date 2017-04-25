from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
import webbrowser
"""Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')"""
Window.size = (480, 800)
#dan@finisventures.com


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

class StepTrack(Screen):
    pass

class LifePage(Screen):
    pass

class ExerciseClasses(Screen):
    def tennisClass(self):
        webbrowser.open_new("https://www.google.com/search?q=tennis+classes+for+seniors+near+me&rlz=1C1CHBF_enUS697US697&oq=tennis+classes+for+seniors+near+me&aqs=chrome..69i57.4491j0j9&sourceid=chrome&ie=UTF-8")
    def waterAerobics(self):
        webbrowser.open_new("https://www.google.com/search?q=water+aerobics+for+seniors+near+me&rlz=1C1CHBF_enUS697US697&oq=water+aer&aqs=chrome.0.69i59j0j69i57j0l3.2565j0j9&sourceid=chrome&ie=UTF-8")
    def swimmingPools(self):
        webbrowser.open_new("https://www.google.com/search?q=swimming+pools+near+me+seniors&rlz=1C1CHBF_enUS697US697&oq=swimming+pools+near+me+seniors&aqs=chrome..69i57.5952j0j9&sourceid=chrome&ie=UTF-8#safe=strict&q=swimming+pools+near+me+")
class SettingsPage(Screen):

    yPos = 0.93
    instances = 1

    def addMedication(self): # This children thing looks ridiculous but thats how I figured it out
        self.children[2].children[0].add_widget(TextInput(
            background_color = (1, 1, 1, 1), # These two properties already exist in
            font_name = 'images/cambriab',   # CustTextInput, not sure how to get them back
            hint_text = "Enter Description",
            pos_hint = {"center_x": .3, "center_y": self.yPos},
            font_size = 25,
            size_hint = (.6, .025),
            multiline = False))
        self.children[2].children[0].add_widget(Spinner(
            pos_hint = {"center_x": .7, "center_y": self.yPos},
            size_hint = (.15,.025),
            text = "Time",
            background_color = (.502, .651, .671, 1),
            values = ('1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00'),
            font_name = 'images/cambriab'))
        self.children[2].children[0].add_widget(CheckBox(
            group = 'ampm' + str(self.instances),
            pos_hint={"center_x": .815, "center_y": self.yPos},
            size_hint = (0.05, 0.015)))
        self.children[2].children[0].add_widget(CheckBox(
            group = 'ampm' + str(self.instances),
            pos_hint = {"center_x": .815, "center_y": self.yPos},
            size_hint = (0.05, 0.015)))
        self.instances += 1
        self.yPos -= 0.05
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