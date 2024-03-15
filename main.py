import kivy
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.


kivy.require("1.10.1")

# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout
# Arg for gridlayout GridLayout
class Module_page(App):
    def build(self):
    # runs on initialization
    #def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout (understanding_super.py)
       # super().__init__(**kwargs)

        #self.cols = 2  # used for our grid
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10, padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout = BoxLayout(orientation="vertical",spacing=2, padding=0)
        # widgets added in order, so mind the order.
        layout.add_widget(Label(text='Module:', size_hint_y=None,size_hint_x=None))  # widget #1, top left
        Module_Name = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40, width=300)  # defining self.ip...
        layout.add_widget(Module_Name) # widget #2, top right
        submit_btn = Button(text='submit', on_press=self.on_submit,  height=30, width=60, size_hint_y=None, size_hint_x=None)
        layout.add_widget(submit_btn)    
        general_layout.add_widget(layout)
        return general_layout
    
    def on_submit(self, instance):
        Module_name = self.Module_Name.text
        print("Module Name: {Module_name}")
    

# class Setap2DApp(App):
#     def build(self):
#         return ConnectPage()


if __name__ == "__main__":
    Module_page().run()