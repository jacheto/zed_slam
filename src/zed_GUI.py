#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import rospy

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        grid = Gtk.Grid()
        self.add(grid)
        
        self.buttonUp = Gtk.Button(label="UP")
        self.buttonDown = Gtk.Button(label="DOWN")
        self.buttonRight = Gtk.Button(label="RIGHT")
        self.buttonLeft = Gtk.Button(label="LEFT")
        self.buttonTurnR = Gtk.Button(label="TURN R")
        self.buttonTurnL = Gtk.Button(label="TURN L")
        
        grid.attach(self.buttonUp,    1, 0, 1, 1)
        grid.attach(self.buttonDown,  1, 2, 1, 1)
        grid.attach(self.buttonRight, 2, 1, 1, 1)
        grid.attach(self.buttonLeft,  0, 1, 1, 1)
        grid.attach(self.buttonTurnR, 2, 0, 1, 1)
        grid.attach(self.buttonTurnL, 0, 0, 1, 1)
        
        #self.button1 = Gtk.Button(label="Hello")
        #self.button1.connect("clicked", self.on_button1_clicked)
        #self.box.pack_start(self.button1, True, True, 0)
#
        #self.button2 = Gtk.Button(label="Goodbye")
        #self.button2.connect("clicked", self.on_button2_clicked)
        #self.box.pack_start(self.button2, True, True, 0)
#
        #self.button3 = Gtk.Button(label="paunocu")
        #self.button3.connect("clicked", self.on_button3_clicked)
        #self.box.pack_start(self.button3, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")

    def on_button3_clicked(self, widget):
        print("paunocu")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()