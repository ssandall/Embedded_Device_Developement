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

def ledToggle():
    if red.is.lit:
        red.off()
        redButton["text"] = "Turn LED on"
    else
        red.on()
        redButton["text"] = "Turn LED off"

### WIDGETS ###
redButton = Button(win, text = "Turn LED on", font = myFont, command = ledToggle, bg = 'red', height = 1, width = 24)
redButton.grid(row=0, column = 1)
