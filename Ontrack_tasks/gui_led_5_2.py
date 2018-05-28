from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE ###

red = LED(20)
green = LED(16)
blue = LED(21)

### GUI DEFINITIONS ##

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### EVENT FUNCTIONS ###

def redToggle():
    if red.is_lit:
        red.off()
        redButton["text"] = "Turn LED on"
    else:
        red.on()
        redButton["text"] = "Turn LED off"

def blueToggle():
    if green.is_lit:
        green.off()
        greenButton["text"] = "Turn LED on"
    else:
        green.on()
        greenButton["text"] = "Turn LED off"

def greenToggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "Turn LED on"
    else:
        blue.on()
        blueButton["text"] = "Turn LED off"

### WIDGETS ###
redButton = Button(win, text = "Turn LED on", font = myFont, command = redToggle, bg = 'red', height = 1, width = 24)
redButton.grid(row=0, column = 1)

greenButton = Button(win, text = "Turn LED on", font = myFont, command = greenToggle, bg = 'red', height = 1, width = 24)
redButton.grid(row=0, column = 2)

blueButton = Button(win, text = "Turn LED on", font = myFont, command = blueToggle, bg = 'red', height = 1, width = 24)
redButton.grid(row=0, column = 3)

win.mainloop
