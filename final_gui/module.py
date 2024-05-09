from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import SpinnerOption, Spinner
from algo import ModifyDataFiles


class Module_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        general_layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(600, 600), spacing=10,
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
        self.module_enrolled = TextInput(multiline=False, height=40, width=300, padding_y=(0, 20))  # TextInput
        layout.add_widget(self.module_enrolled)
        spinner = MultiSelectSpinner(text="Select Lecturers")
        getLecturers = ModifyDataFiles()
        
        options = getLecturers.selectLecturer()
        for option in options:
             key, value = option 
             spinner.add_option(f"{key}-{value}")
        layout.add_widget(spinner)
        
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
       pass
    def go_back(self, instance):
        self.manager.current = 'entry_section' # Stops the current application instance, effectively going back


class MultiSelectSpinner(Spinner):
    def __init__(self, **kwargs):
        super(MultiSelectSpinner, self).__init__(**kwargs)
        self.dropdown = DropDown()

    def add_option(self, option):
        if option not in self.dropdown.children:
            btn = SpinnerOption(text=option)
            btn.bind(on_release=self.on_option_select)
            self.dropdown.add_widget(btn)

    def on_option_select(self, instance):
        if instance.text not in self.values:
            self.values.append(instance.text)
        else:
            self.values.remove(instance.text)
            if(len (self.values) == 0):
                self.values.append("Select Lecturer")
                

    def on_values(self, instance, values):
        self.text = ', '.join(values)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dropdown.open(self)
        return super(MultiSelectSpinner, self).on_touch_down(touch)
