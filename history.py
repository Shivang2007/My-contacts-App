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
from os import path
import random
import sys
import json
import time
import logging


class HistoryPage(Screen):
    app_title = "My Contacts"
    def enter(self):
        pass
        
    def contact(self):
        self.manager.current = 'conp'