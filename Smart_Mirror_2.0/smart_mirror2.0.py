from tkinter import *
import time

class Clock(Frame):
    def __init__(self, root):
        clock = Label(root, font=('times', 20, 'bold'), bg='green')
        clock.pack(fill="both", expand=True)
        self.tick()

    def tick(self):
        time1 = ''
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
        self.clock.config(text=time2)
        clock.after(200, tick)

if __name__=='__main__':
    win = Tk()
    view = Clock(win)
    view.pack(side="top", fill="both", expand=True)
    win.mainloop()
