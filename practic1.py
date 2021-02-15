from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):

        s=Scatter()
        fl=FloatLayout(size=(300, 300))
        s.add_widget(fl)
        fl.add_widget(Button(
            text="Это кнопка №1",
            font_size=18,
            on_press=self.btn_press,
            background_color='#310062',
            background_normal='',
            size_hint=(.5, .25),
            pos=(220, 100)));
  
        fl.add_widget(Button(
            text="Это кнопка №2",
            font_size=18,
            on_press=self.btn_press2,
            background_color='#FFEFD5',
            background_normal='',
            size_hint=(.5, .25),
            pos=(50, 100)));
        return s
    
    def btn_press(self, instance):
        instance.text='Я нажата'
    def btn_press2(self, instance):
        instance.text='Я нажата'

if __name__=="__main__":
    myApp().run()
    
         
        
            
                       
