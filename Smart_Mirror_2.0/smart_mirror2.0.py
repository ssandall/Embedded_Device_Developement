from tkinter import *
import time
import json
import requests
from urllib.request import urlopen

#Font Variables
font_type = 'Helvetica'
font_colour = "White"
xlarge_text_size = 48
large_text_size = 30
medium_text_size = 20
small_text_size = 12
xsmall_text_size =8
#Local Weather Variables
READ_API_KEY = 'D71A7607GOWJSZ6D'
CHANNEL_ID = 502804


class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        #Time Label
        self.time1 = ''
        self.timeLbl = Label(self, font=(font_type, xlarge_text_size), fg=font_colour, bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        #Day Of the Week label
        self.weekday1 = ''
        self.weekdayLbl = Label(self, font=(font_type,medium_text_size), fg=font_colour, bg="black")
        self.weekdayLbl.pack(side=TOP,anchor=E)
        #Date Label
        self.date1 = ''
        self.dateLbl = Label(self,font=(font_type,medium_text_size), fg=font_colour, bg="black")
        self.dateLbl.pack(side=TOP,anchor=E)
        self.tick()

    def tick(self):
        #Set Clock
        time2 = time.strftime('%H:%M:%S')
        if time2 != self.time1:
            time1 = time2
            self.timeLbl.config(text=time2)
            self.timeLbl.after(200, self.tick)
        # Set Day of the Week
        weekday2 = time.strftime('%A')
        if weekday2 != self.weekday1:
            self.weekday1 = weekday2
            self.weekdayLbl.config(text=weekday2)
        # Set date
        date2 = time.strftime("%d %b, %Y")
        if date2 != self.date1:
            self.date1 = date2
            self.dateLbl.config(text=date2)
class Weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        #Temperature Label
        self.temperature = ''
        self.temperatureLbl = Label(self, font=(font_type, xlarge_text_size), fg=font_colour, bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        #UV Level Label
        self.uv = ''
        self.uvLbl = Label(self, font=(font_type, large_text_size), fg=font_colour, bg="black")
        self.uvLbl.pack(side=LEFT, anchor=N)
        #Humidity Label
        self.humidity = ''
        self.humidityLbl = Label(self, font=(font_type, medium_text_size),fg=font_colour,bg="black")
        self.humidityLbl.pack(side=LEFT, anchor=N)
        #Apparent Temperature Label
        self.apparenttemp = ''
        self.apparenttempLbl = Label(self, font=(font_type, medium_text_size), fg=font_colour, bg="black")
        self.apparenttempLbl.pack(side=LEFT, anchor=N)

        self.get_local_weather()

    def get_local_weather(self):
        try:
            degree_sign = u'\N{DEGREE SIGN}'
            tempval = ''
            humidval = ''
            uvval = ''
            apptempval = ''

            api_information = ("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID, READ_API_KEY))

            response = requests.get(api_information)
            data = response.json()

            tempval = "%.2f%s" % (float(str(data['field1'])), degree_sign)
            humidval = "%s%.2f%s" % ("Humidity ", float(str(data['field2'])), "%")
            uvval = "%s%s" % ("UV Level ", int(data['field3']))
            apptempval = "%s%.2f%s" % ("Feel's like ", float(str(data['field4'])), degree_sign)

            if self.temperature != None:
                self.temperature = tempval
                self.temperatureLbl.config(text=tempval)

            if self.humidity != None:
                self.humidity = humidval
                self.humidityLbl.config(text=humidval)

            if self.uv != None:
                self.uv = uvval
                self.uvLbl.config(text=uvval)

            if self.apparenttemp != None:
                self.apparenttemp = apptempval
                self.apparenttempLbl.config(text=apptempval)

        except Exception as e:
            traceback.print_exc()
            print ("Error: %s. Cannot get weather.") % e

        self.after(500, self.get_local_weather)
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
        #Clock Location
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)
        #Weather Location
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT,anchor=N, padx=100, pady=60)

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
