from tkinter import *
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

class ExampleView(Frame):
    def __init__(self, root):
        red = LED(20)
        green = LED(16)
        blue = LED(21)
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

        Frame.__init__(self, root)
        redButton = Button(win, text="Turn LED On", command= redToggle)
        redButton.pack()
        blueButton = Button(win, text="Turn LED On", command= blueToggle)
        blueButton.pack()
        greenButton = Button(win, text="Turn LED On", command= greenToggle)
        greenButton.pack()
        
if __name__=='__main__':
    win = Tk()
    view = ExampleView(win)
    view.pack(side="top", fill="both", expand=True)
    win.mainloop()
