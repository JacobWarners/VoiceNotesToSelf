
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
#from writeTospreadsheet import putDataToSpreadsheet
from voicething import recordAudioToFile, translateAudioFile

recordButton=False

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text='Record', on_press=self.on_press_button))
        layout.add_widget(Button(text='Check Spreadsheet',on_press=self.on_press_button2))
        return layout

    def on_press_button(self, instance):
        recordAudioToFile()
    def on_press_button2(self, instance):
        print("other Button")

if __name__ == '__main__':
    app = MainApp()
    app.run()
