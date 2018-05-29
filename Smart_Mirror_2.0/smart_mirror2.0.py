from tkinter import *
import time

xlarge_text_size = 12

class Clock(Frame):
    def __init__(self, root):
        #clock = Label(root, font=('times', 20, 'bold'), bg='green')
        clock= Label(self, font=('Helvetica', xlarge_text_size), fg="white", bg="black")
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
