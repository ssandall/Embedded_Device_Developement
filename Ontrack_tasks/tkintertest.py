from tkinter import *
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

class RGBLed(Frame):
    def __init__(self, root):
        red = LED(20)
        green = LED(16)
        blue = LED(21)
        def redToggle():
            if red.is_lit:
                red.off()
                redButton["text"] = "Turn RED on"
            else:
                red.on()
                redButton["text"] = "Turn RED off"
        def greenToggle():
            if green.is_lit:
                green.off()
                greenButton["text"] = "Turn GREEN on"
            else:
                green.on()
                greenButton["text"] = "Turn GREEN off"
        def blueToggle():
            if blue.is_lit:
                blue.off()
                blueButton["text"] = "Turn BLUE on"
            else:
                blue.on()
                blueButton["text"] = "Turn BLUE off"

        Frame.__init__(self, root)
        redButton = Button(win, text="Turn RED On", command= redToggle)
        redButton.pack()
        blueButton = Button(win, text="Turn BLUE On", command= blueToggle)
        blueButton.pack()
        greenButton = Button(win, text="Turn GREEN On", command= greenToggle)
        greenButton.pack()

if __name__=='__main__':
    win = Tk()
    view = RGBLed(win)
    view.pack(side="top", fill="both", expand=True)
    win.mainloop()
