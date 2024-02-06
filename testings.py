from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="RedsTooN: "))
        self.Reds = TextInput(multiline=False)
        self.add_widget(self.Reds)
        self.add_widget(Label(text="New Xiro: "))
        self.Xiro = TextInput(multiline=False)
        self.add_widget(self.Xiro)
        self.add_widget(Label(text="Verdox: "))
        self.VER = TextInput(multiline=False)
        self.add_widget(self.VER)
        self.submit = Button(text="submit", font_size=32)
        self.add_widget(self.submit)

        
class HelloKivyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    HelloKivyApp().run()