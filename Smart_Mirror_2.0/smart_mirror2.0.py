from tkinter import *
import time

xlarge_text_size = 12

class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        #time label
        self.time1 = ''
        self.timeLbl = Label(self, font=('Helvetica', xlarge_text_size), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):
        time2 = time.strftime('%H:%M:%S')
        if time2 != self.time1:
            time1 = time2
            self.timeLbl.config(text=time2)
            self.timeLbl.after(200, self.tick)

if __name__=='__main__':
    win = Tk()
    view = Clock(win)
    view.pack(side="top", fill="both", expand=True)
    win.mainloop()
