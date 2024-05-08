from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
#from algo import ModifyDataFiles


class Module_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(400, 400), spacing=10,
        #                            padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # layout = BoxLayout(orientation="vertical", spacing=2, padding=0)

        # # Back button above the module text
        # back_btn = Button(text='Back', on_press=self.go_back, height=30, width=60, size_hint_y=None, size_hint_x=None)
        # layout.add_widget(back_btn)

        # layout.add_widget(Label(text='Module:', size_hint_y=None, size_hint_x=None))
        # self.module_name_input = TextInput(multiline=False, size_hint_y=None, size_hint_x=None, height=40, width=300)
        # layout.add_widget(self.module_name_input)
        # submit_btn = Button(text='Submit', on_press=self.on_submit, height=30, width=60, size_hint_y=None,
        #                     size_hint_x=None)
        # layout.add_widget(submit_btn)

        # general_layout.add_widget(layout)
        # self.add_widget(general_layout)
       
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(500, 500), spacing=10,
                                   padding=10, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Top header with back button
        header_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
        back_button = Button(text="Back", size_hint=(None, None), width=80, height=40)
        back_button.bind(on_press=self.go_back)
        header_layout.add_widget(back_button)
        header_layout.add_widget(Label(text="Module Page", size_hint=(1, None), height=40))
        general_layout.add_widget(header_layout)

        # Main content
        layout = BoxLayout(orientation="vertical", spacing=2, padding=0)
        layout.add_widget(Label(text='module Name:'))  # Label
        self.module_Name = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.module_Name)
        layout.add_widget(Label(text='Module enrolled'))  # Label
        self.module_enrolled = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.module_enrolled)
        layout.add_widget(Label(text='module lecturers'))  # Label
        self.module_lecturers = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.module_lecturers)
        
        layout.add_widget(Label(text='module practicals'))  # Label
        self.module_practicals = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.module_practicals)
        
        layout.add_widget(Label(text='module tutorials'))  # Label
        self.module_tutorials = TextInput(multiline=False, height=40, width=300)  # TextInput
        layout.add_widget(self.module_tutorials)

        submit_btn = Button(text='Submit', on_press=self.on_submit, height=30, width=60)
        submit_btn.bind(on_press=self.on_submit)
        layout.add_widget(submit_btn)

        general_layout.add_widget(layout)
        self.add_widget(general_layout) 

    def on_submit(self, instance):
        # module_name = self.module_name_input.text
        # enter_module = ModifyDataFiles()
        print("I can hear you")

    def go_back(self, instance):
        self.manager.current = 'entry_section' # Stops the current application instance, effectively going back



