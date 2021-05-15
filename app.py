from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivymd.uix.dialog import MDDialog
from kivy_garden.zbarcam import ZBarCam
from kivymd.uix.tab import MDTabsBase
from kivymd.toast import toast
from kivymd.theming import ThemeManager
from kivy.core.window import Window
from helper import screen_helper
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import cv2
from cv2 import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from datetime import datetime
from datetime import time
import time
import mysql.connector
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import VariableListProperty
from kivy.config import Config
from kivy.core.window import Window  


class LoginScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class ScanScreen(Screen):
    pass


class AttendanceScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()

sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(ScanScreen(name='scan'))
sm.add_widget(AttendanceScreen(name='attendance'))
sm.add_widget(AboutScreen(name='about'))
sm.add_widget(ProfileScreen(name='profile'))


class DemoApp(MDApp):

    def build(self):
        
        Window.size = (400, 700)
        Window.minimum_width, Window.minimum_height = Window.size
        self.screen = Builder.load_string(screen_helper)
        theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        self.title = 'LogX'
        return self.screen

    def validation(self):
        global ls,ms,ss,atts, ok_button, ty_button, ps, abts
        ls = self.screen.get_screen('login')
        ms = self.screen.get_screen('main')
        ss = self.screen.get_screen('scan')
        atts = self.screen.get_screen('attendance')
        ps = self.screen.get_screen('about')
        abts = self.screen.get_screen('profile')
        global usr, pwd
        usr = ls.username.text
        pwd = ls.password.text
        from sql import validateLogin
        val = validateLogin(usr, pwd)
        ok_button = MDFlatButton(text='Okay', on_release=self.close_dialog)
        ty_button = MDFlatButton(text='Thank You', on_release=self.close_dialog)
        if val == 0:
            print("Login Unsuccessful")
            self.dialog = MDDialog(title="Login Failed", text="Username Or Password Incorrect", size_hint=(
                0.7, 1), buttons=[ok_button])
            self.dialog.open()
        else:
            print("Login Successful")
            from sql import name
            namee = name(usr)
            welcome = "Welcome " + namee
            
            self.dialog = MDDialog(
                title="Login Successful",
                text=welcome,
                size_hint=(0.7, 1),
                buttons=[ty_button])

            self.dialog.open()
            self.screen.switch_to(ms, direction='left', duration=1)

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def calc(self, obj):
        qrvalue = ss.qrlabel.text
        final = qrvalue.strip("b''")
        latest = datetime.now()
        date_time = latest.strftime("%m-%d-%Y-%H-%M")
        if final == date_time:
            print("Present")
            from sql import markattendance
            markattendance(usr)
            #ls = self.screen.get_screen('main')
            self.dialog = MDDialog(
                title="Attendance",
                text="Attendance Marked!",
                size_hint=(0.7, 1),
                buttons=[ok_button])
            self.dialog.open()
            self.screen.switch_to(ms, direction='right', duration=1)

        else:
            print("Absent")

    data = {
        'alien': 'About',
        'account': 'Profile',
        }

    def back(self):
        self.screen.switch_to(ms, direction='right')
    
    def bback(self,obj):
        self.screen.switch_to(ms, direction='right')
    
    def scanner(self):
        self.screen.switch_to(ss, direction='left')
        
    def callback(self, instance):
        if instance.icon == 'alien':
            self.screen.switch_to(ps)

        elif instance.icon == 'account':
            self.screen.switch_to(abts)
        
        
    def table(self):
        self.screen.switch_to(atts, direction='left', duration=1)
        box = BoxLayout(padding = [10, 10, 10, 10])
        from sql import attendance_fetch
        data = attendance_fetch(usr)
        self.data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=True,

            # name column, width column, sorting function column(optional)
            column_data=[
                ("Employee ID", dp(20)),
                ("Timestamp", dp(50)),
                ("Date", dp(50)),
            ],
            row_data=data
        )
        self.backButton = MDIconButton(icon= "keyboard-backspace",
        pos_hint= {"center_x": .15, "center_y": .95},
        on_release= self.bback
        )
        box.add_widget(self.data_tables)
        box.add_widget(self.backButton)
        atts.add_widget(box)


DemoApp().run()