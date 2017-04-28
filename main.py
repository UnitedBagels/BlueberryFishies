from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
import webbrowser, pickle, plyer
from plyer import notification as n
from kivy.clock import Clock
import datetime
"""Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')"""
Window.size = (480, 800)
#dan@finisventures.com

#print(datetime.datetime.now())

n.notify(title="test", message = 'm', ticker = 'r')
medData = {}
lazy = 1

class CCheckBox(CheckBox):
    def __init__(self, **kwargs):
        super(CCheckBox, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()

    def update_canvas(self, *args):
        with self.canvas.before:
            Color(rgba = (.2, .2, .2, 1))
            Rectangle(pos=self.pos, size=self.size)

class HomePage(Screen):
    Window.clearcolor = (0.7647, 0.8353, 8588, 1)
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

    def grabTime(self):
        file_Name = "testfile.dat"
        fileObject = open(file_Name,'r')
        c = pickle.load(fileObject)
        fileObject.close()
        return c

    def writeTime(self, b):
        if b != "":
            file_Name = "testfile.dat"
            fileObject = open(file_Name,'wb')
            c = pickle.dump(b, fileObject)
            fileObject.close()

    def dailyWalkTime(self, b):
        if b != "":
            file_Name = "testfile.dat"
            currentTime = self.grabTime()
            print currentTime
            try:
                currentTime = int(currentTime) + int(b)
            except ValueError:
                print "why tho"

            print currentTime
            self.writeTime(currentTime)

    def undoTime(self, b):
            file_Name = "testfile.dat"
            c = self.grabTime()
            print "c=" + str(c)
            newT = 0
            try:
                newT = int(c) - int(b)
            except ValueError:
                print "hhhh"

            if newT != 0:
                self.writeTime(newT)
#$$

    def resetTime(self):
        self.writeTime(0)

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

    yPos = 0.98
    instances = 0
    done_loading = False

    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)
        Clock.schedule_interval(self.loadData, 0.01)


    def addMedications(self): # This children thing looks ridiculous but thats how I figured it out
        self.instances += 1
        self.children[2].children[0].add_widget(TextInput(
            id = "t" + str(self.instances),
            background_color = (1, 1, 1, 1), # These two properties already exist in
            font_name = 'images/cambriab',   # CustTextInput, not sure how to get them back
            hint_text = "Enter Description",
            pos_hint = {"center_x": .3, "center_y": self.yPos},
            font_size = 25,
            size_hint = (.6, .025),
            multiline = False))
        self.children[2].children[0].add_widget(Spinner(
            id = "s" + str(self.instances),
            pos_hint = {"center_x": .7, "center_y": self.yPos},
            size_hint = (.15,.025),
            text = "Time",
            background_color = (.502, .651, .671, 1),
            values = ('1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00'),
            font_name = 'cambriab.ttf'))
        self.children[2].children[0].add_widget(CCheckBox(
            id = "a" + str(self.instances),
            group = 'ampm' + str(self.instances),
            pos_hint={"center_x": .815, "center_y": self.yPos},
            size_hint = (0.05, 0.015)
        ))
        self.children[2].children[0].add_widget(CCheckBox(
            id = "p" + str(self.instances),
            group = 'ampm' + str(self.instances),
            pos_hint = {"center_x": .87, "center_y": self.yPos},
            size_hint = (0.05, 0.015)))
        self.yPos -= 0.05

    def saveMedications(self):
        global medData
        for i in range(len(self.children[2].children[0].children)):
            try:
                medData[str(self.children[2].children[0].children[i].id)] = str(self.children[2].children[0].children[i].text)
            except AttributeError:
                medData[str(self.children[2].children[0].children[i].id)] = str(self.children[2].children[0].children[i].active)
        try:
            with open('save.dat','wb') as f:
                f.seek(0)
                f.truncate()
                pickle.dump(medData, f)
                f.close()
        except EOFError:
            pass
        print(medData)

    def loadData(self, dt):
        global medData
        if self.manager.current == "reminders" and not self.done_loading:
            try:
                with open('save.dat','rb') as fp:
                    medData = pickle.load(fp)
                    fp.close()
            except EOFError:
                pass
            for q in range(len(medData) / 4):
                self.addMedications()
            for ide, valuee in medData.iteritems():
                #print(ide, valuee)
                for widget in self.walk():
                    if widget.id == ide:
                        widget.text = valuee
                        print(widget.id, valuee)
                        widget.active = self.str_to_bool(valuee)
                        #if ide[0] == "a" or "p":
                        #    widget.active == valuee
                        #self.children[2].children[0].children[k].text = valuee
                        #print(valuee)
                        #print(self.children[2].children[0].children[k].text)
            self.done_loading = True
            # ---------- I left off here ----------

    def str_to_bool(self, s):
        if s == 'True':
            return True
        elif s == 'False':
            return False
        #elif s == None:
        #    pass

    #def my_callback(self,dt):


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