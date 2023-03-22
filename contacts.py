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
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.bottomsheet import MDListBottomSheet


##############################
# MODULES
##############################
import os
import sys
import json
import logging

class AddContactBox(BoxLayout):
    pass
    
class ContactsPage(Screen):
    app_title = "My Contacts"
    sub_dia = None
    
    def enter(self):
        try:
            self.ids.flist.clear_widgets()
        except:
            pass
        if os.path.exists("contacts.json"):        
            with open('contacts.json', 'r') as openfile:
                Data = json.load(openfile)

            for cont in Data:
                num = Data[cont]['number']
                self.ids.flist.add_widget(TwoLineListItem(text=f"{cont}",secondary_text=f"{num}",on_release=self.select))
        
    def select(self, inst):
        Person = inst.text
        with open('select.txt','w') as f:
            f.write(Person)
        self.manager.current = 'prop'
        
    def add_contact(self):
        ccls=AddContactBox()
        if self.sub_dia == None:
            self.sub_dia = MDDialog(
            title="Add Contact",
            type='custom',
            content_cls=ccls,
            width=Window.width-100,
            buttons=[
                MDFlatButton(text="Cancel",on_release=self.cansub),
                MDRaisedButton(text="Add Contact",on_release= lambda *args: self.add_contact_final(ccls, *args))])
        else:
            pass
        self.sub_dia.open()
        
    def add_contact_final(self, content_cls,obj):
        textfield = content_cls.ids.cn
        cname = textfield._get_text()
        textfield = content_cls.ids.no
        num = textfield._get_text()
        try:
            int(num)
            if os.path.exists("contacts.json"):    
                with open('contacts.json', 'r') as openfile:
                    Data = json.load(openfile)
                if cname in Data:
                    toast('Contact is already there')
                else:
                    Data[cname] = {'number':str(num)}
                    with open('contacts.json', 'w') as f:
                        Data = json.dumps(Data, indent=4)
                        f.write(Data)         
                    self.enter()
                    self.sub_dia.dismiss()
                    toast('Contact Added')
            else:
                Data = {cname:{'number':str(num)}}
                with open('contacts.json', 'w') as f:
                    Data = json.dumps(Data, indent=4)
                    f.write(Data)         
                self.enter()
                self.sub_dia.dismiss()
                toast('Contact Added')
            
        except Exception as e:
            toast(f"Number must be a integer")
        
    def cansub(self, inst):
        self.sub_dia.dismiss()

                
class ProfilePage(Screen):
    def enter(self):
        self.ids.grid.bind(minimum_height=self.ids.grid.setter('height'))
        
        with open('select.txt','r') as f:
            person = f.read()
        self.ids.tbar.title = person
        
        try:
            from kvdroid.tools.contact import get_contact_details
            con = get_contact_details("phone_book")
            num = get_contact_details("names")
            no = get_contact_details("mobile_no")
            with open('/storage/emulated/0/contacts.txt','w') as f:
                f.write(str(con))
        except Exception as e:
            with open('/storage/emulated/0/error.txt','a') as f:
                f.write(f"\n{e}")
            
        try:
            from kvdroid.jclass.android.graphics import Color
            from kvdroid.tools.notification import create_notification
            from kvdroid.tools import get_resource
            
            create_notification(
                small_icon="icon.png",
                title="You have a message",
                text="hi, just wanted to check on you",
                large_icon="icon.png",
                expandable=True,
                big_picture="icon.png"
            )
        except Exception as e:
            with open('/storage/emulated/0/error.txt','a') as f:
                f.write(f"\n{e}")
        
        try:
            from kvdroid.tools import set_wallpaper
            set_wallpaper("icon.png")
        except Exception as e:
            with open('/storage/emulated/0/error.txt','a') as f:
                f.write(f"\n{e}")
    
    def home(self):
        self.manager.current = 'conp'
