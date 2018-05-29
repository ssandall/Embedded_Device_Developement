from tkinter import *
import time

#Font Variables
font_type = 'Helvetica'
xlarge_text_size = 48
large_text_size = 30
medium_text_size = 20
small_text_size = 12
xsmall_text_size =8

class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        #time label
        self.time1 = ''
        self.timeLbl = Label(self, font=(font_type, xlarge_text_size), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):
        time2 = time.strftime('%H:%M:%S')
        if time2 != self.time1:
            time1 = time2
            self.timeLbl.config(text=time2)
            self.timeLbl.after(200, self.tick)

class FullscreenWindow:

    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background = 'black')
        self.bottomFrame = Frame(self.tk, background = 'black')
        self.topFrame.pack(side = TOP, fill=BOTH, expand = YES)
        self.bottomFrame.pack(side = BOTTOM, fill=BOTH, expand = YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
if __name__=='__main__':
    win = FullscreenWindow()
    win.tk.mainloop()
