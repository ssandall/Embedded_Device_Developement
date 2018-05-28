from tkinter import *
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

class ExampleView(Frame):
    red = LED(20)
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        '''
        l = tk.Label(self, text="your widgets go here...", anchor="c")
        l.pack(side="top", fill="both", expand=True)
        '''
        redButton = Button(master, text="Turn LED On", command=redToggle)
        redButton.pack()

    def redToggle():
        if red.is_lit:
            red.off()
            redButton["text"] = "Turn LED on"
        else:
            red.on()
            redButton["text"] = "Turn LED off"

if __name__=='__main__':
    root = Tk()
    view = ExampleView(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
