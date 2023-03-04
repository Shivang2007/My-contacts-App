##############################
# KIVY MAIN APP CLASSES
##############################
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivymd.utils.set_bars_colors import set_bars_colors
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

##############################
# KIVYMD WIDGETS 
##############################
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton,MDFlatButton,MDRaisedButton,MDRectangleFlatIconButton
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import DictProperty
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.clock import Clock

##############################
# MODULES
##############################
import os
import sys
import requests


if os.path.exists('Profile_Images'):
    pass
else:
    os.mkdir('Profile_Images')
    
try:
    from android.permissions import request_permissions, Permission
except:
    toast('Error 101')
    
from history import HistoryPage
from contacts import ContactsPage, ProfilePage

try:
    request_permissions([Permission.INTERNET,Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.SEND_SMS,Permission.CALL_PHONE,Permission.READ_CONTACTS,Permission.SET_WALLPAPER])
except:
    toast('Error 102')

ContactsPage()
HistoryPage()
ProfilePage()
    
class MainApp(MDApp):
    def build(self):
        try:
            url = "https://getpantry.cloud/apiv1/pantry/cebe6650-5045-4ea3-b6f0-d171a877b307/basket/apps_data"
            app_data = requests.get(url).json()
            if "My Contacts" in app_data:
                app_data = app_data["My Contacts"]
            else:
                app_data = {}
        except:
            app_data = {}

        self.theme_cls.theme_style_switch_animation = True
        try:
            self.theme_cls.primary_palette = str(app_data['theme'])
        except:
            self.theme_cls.primary_palette = "Blue"
        
        try:
            self.theme_cls.theme_style = str(app_data['mode'])
        except:
            self.theme_cls.theme_style = "Light"  
             
        self.set_bars_colors()        
        sm=ScreenManager()        
        sc_lst = [
        ContactsPage(name='conp'),
        HistoryPage(name='histp'),
        ProfilePage(name='prop')
        ]
        for sc in sc_lst:
            sm.add_widget(sc)
            
        return sm

    def set_bars_colors(self):
        set_bars_colors(
            self.theme_cls.primary_color, 
            self.theme_cls.primary_color,
            "Light",
        )

MainApp().run()