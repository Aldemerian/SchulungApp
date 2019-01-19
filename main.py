# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import time
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
import random
from kivy.animation import Animation
from kivy.clock import Clock
import datetime
from kivy.uix.textinput import TextInput

import sqlite3
#conn = sqlite3.connect('example.db')


class MainScreen(Screen):

    def on_touch_down(self, touch):
        self.initial_x = touch.x
        print(self.initial_x)
        self.initial_y = touch.y
        print(self.initial_y)

    def on_touch_up(self, touch):
        touch_diff_x = touch.x-self.initial_x
        touch_diff_y = touch.y-self.initial_y
        if abs(touch_diff_x) > abs(touch_diff_y):
            if touch_diff_x < 0:
                print("left")
                self.manager.current = 'left'
            else:
                print("right")
                self.manager.current = 'right'
        elif abs(touch_diff_x) < abs(touch_diff_y):
            if touch_diff_y < 0:
                print("down")
                self.manager.current = 'down'
            else:
                print("up")
                self.manager.current = 'up'
        else:
            pass


class LeftScreen(Screen):
    ##change the way the countdown and countup works
    # change label
    hour_db = (("Anfang", 5), ("Mitte", 3), ("Ende", 10))
    duration = hour_db[0][1] * 60
    time_now = datetime.datetime.now()
    name_hour = StringProperty
    name_hour = hour_db[0][0]
    dur_hour = hour_db[0][1] *60
    run_thru = 1
    counter_whole = 0
    counter_part = 0

    def on_enter(self):
        self.clocking()

    def clocking(self):
        Clock.schedule_interval(self.color_change, 1)

    def close_event(self):
        Clock.unschedule(self.color_change)

    def counter(self):
        self.counter_whole = self.counter_whole + 1
        if self.counter_whole == self.dur_hour:
            pass
        else:
            pass

    def color_change(self, *args):
        with self.canvas.before:
            time_now = datetime.datetime.now()
            percent_color = (self.duration/self.dur_hour)
            print(percent_color)
            new_color = percent_color * 0.7
            newer_color = tuple(Color(new_color, 1, 1, mode='hsv').rgba)
            print(newer_color)
            new_color = str(new_color) + " color"
            print(new_color)
            self.color = newer_color
            self.duration = self.duration -1

    def new_unit(self):
        self.name_hour = self.hour_db[self.run_thru][0]
        print(self.name_hour)
        self.dur_hour = self.hour_db[self.run_thru][1] * 60
        print(self.dur_hour)
        self.duration = self.hour_db[self.run_thru][1] * 60
        print(self.duration)
        self.close_event()
        self.run_thru = self.run_thru + 1
        self.clocking()

    def old_unit(self):
        self.name_hour = self.hour_db[self.run_thru][0] * 60
        self.dur_hour = self.hour_db[self.run_thru][1]  * 60
        self.close_event()
        self.run_thru = self.run_thru -2
        self.clocking()


    def on_touch_down(self, touch):
        self.initial_x = touch.x
        print(self.initial_x)

    def on_touch_up(self, touch):
        touch_diff_x = touch.x-self.initial_x
        if touch_diff_x < 0:
            print("new")
            self.new_unit()
        elif touch_diff_x > 0:
            print("old")
            self.old_unit()
        else:
            pass


class UpScreen(Screen):

    def on_enter(self):
        print("change lessons&create them")


class DownScreen(Screen):
    pass


class RightScreen(Screen):
    def build(self):
        self.txt = TextInput()

    def buttonClicked(self):
        print("hey")
        inputtext = self.drei.text
        print(inputtext)



class ScreenManagement(ScreenManager):
    mainscreen = ObjectProperty(None)
    upscreen = ObjectProperty(None)
    downscreen = ObjectProperty(None)
    rightscreen = ObjectProperty(None)
    leftscreen = ObjectProperty(None)


presentation = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    MainApp().run()