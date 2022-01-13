from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.uix.textfield import *
import pyautogui
from kivy.uix.image import Image 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.toast import toast
import os
from KivyOnTop import register_topmost, unregister_topmost
from kivy.animation import Animation
from kivy.properties import NumericProperty
path=os.path.dirname(os.path.abspath(__file__))

TITLE = 'Virtual Typer'

class Clock(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.color=(0,0.4,1,1)
        self.bold=True
        self.size_hint_y=0.2
        self.font_size='40sp'
    
    a=NumericProperty()
    
    def start(self,a,MAIN,BUTTON,s,f):
        self.a=a
        Animation.cancel_all(self)  
        self.anim = Animation(a=0, duration = self.a)
 
        
        def finish_callback(animation, clock):
            MAIN.remove_widget(self)
            MAIN.add_widget(BUTTON)
            pyautogui.write(s, interval = f)
            toast('Done')
 
        self.anim.bind(on_complete = finish_callback)
        self.anim.start(self)
 
    
    def on_a(self, instance, value):
        self.text = str(round(value, 1))

class Test(MDApp):
    

    def on_start(self, *args):
        Window.set_title(TITLE)
        register_topmost(Window, TITLE)
        self.bind(on_stop=lambda *args, w=Window, t=TITLE: unregister_topmost(w, t))
    def change(self,instance):
        clock=Clock()
        self.B.remove_widget(self.Ty)
        self.B.add_widget(clock)
        clock.start(int(self.Delay.text),self.B,self.Ty,self.T.text,int(self.Interval.text)//10)
        
    def add_delay(self,instance):
        self.Delay.text=str(int(self.Delay.text)+1)

    def sub_delay(self,instance):
        if int(self.Delay.text) != 0:
            self.Delay.text=str(int(self.Delay.text)-1)
    
    def add_interval(self,instance):
        self.Interval.text=str(int(self.Interval.text)+1)

    def sub_interval(self,instance):
        if int(self.Interval.text) != 0:
            self.Interval.text=str(int(self.Interval.text)-1)

    def build(self):

        self.B=BoxLayout(orientation='vertical')

        self.H=BoxLayout(size_hint=(1,0.4))
        self.H.add_widget(Image(source=f'{path}/h.png',allow_stretch = True,keep_ratio = True,size_hint=(0.5,0.5),pos_hint={'center_y':0.5,'center_x':0}))
        self.H.add_widget(Label(text="Virtual Typer",bold=True,font_size='50sp',color=(0.2,0.8,0.8,1),pos_hint={'x':0}))
        self.D=BoxLayout(orientation='vertical',size_hint=(0.5,1))
        self.D.add_widget(Label(text='Developed By :\nSatyam Lohiya',color=(0.2,0.2,0.2,0.5),pos_hint={'top':0}))
        self.D.add_widget(Label())
        self.H.add_widget(self.D)
        self.B.add_widget(self.H)

        self.I=BoxLayout(size_hint=(1,0.1))
        self.I.add_widget(Label(text='Delay',color=(0,0,0,0.7),size_hint=(0.5,1)))
        self.Delay=TextInput(text='5',multiline=False,input_filter= "int")
        self.I.add_widget(self.Delay)
        self.I.add_widget(MDIconButton(icon='plus',theme_text_color= "Custom",text_color=(0,0,1,1),on_press=self.add_delay))
        self.I.add_widget(MDIconButton(icon='minus',theme_text_color= "Custom",text_color=(1,0,0,1),on_press=self.sub_delay))
        
        self.I.add_widget(Label(text='Interval',color=(0,0,0,0.7),size_hint=(0.5,1)))
        self.Interval=TextInput(text='0',multiline=False)
        self.I.add_widget(self.Interval)
        self.I.add_widget(MDIconButton(icon='plus',theme_text_color= "Custom",text_color=(0,0,1,1),on_press=self.add_interval))
        self.I.add_widget(MDIconButton(icon='minus',theme_text_color= "Custom",text_color=(1,0,0,1),on_press=self.sub_interval))
        self.B.add_widget(self.I)

        self.B.add_widget(Label(size_hint=(1,0.1)))

        self.T=TextInput(hint_text='Input Text')
        self.B.add_widget(self.T)
        self.Ty=Button(text='Type',size_hint=(1,0.2),background_color=(0.2,0.8,1,1),on_release=self.change)
        self.B.add_widget(self.Ty)
        return self.B

Test().run()