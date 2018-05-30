from Tkinter import *
import locale
import threading
import time
import requests
import feedparser
import json
import traceback
import urllib2
import praw

from PIL import Image, ImageTk
from contextlib import contextmanager


ui_locale = ''
time_format = 12 # 12 or 24
date_format = "%b %d, %Y"
news_country_code = 'au'
READ_API_KEY = 'D71A7607GOWJSZ6D'
CHANNEL_ID = 502804
xlarge_text_size = 48
large_text_size = 28
medium_text_size = 18
small_text_size = 12

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
        time2 = time.strftime('%H:%M')
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
        self.temperature = ''
        self.humidity = ''
        self.uv = ''
        self.apparenttemp = ''
        self.icon = ''

        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=W)

        self.temperatureLbl = Label(self.degreeFrm, font=('Helvetica', xlarge_text_size), fg="white", bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N)

        self.uvLbl = Label(self, font=('Helvetica', large_text_size), fg="white", bg="black")
        self.uvLbl.pack(side=TOP, anchor=W)

        self.humidityLbl = Label(self, font=('Helvetica', medium_text_size),fg="white",bg="black")
        self.humidityLbl.pack(side=TOP, anchor=W)

        self.apparenttempLbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.apparenttempLbl.pack(side=TOP, anchor=W)

        self.get_local_weather()

    def get_local_weather(self):
        try:
            degree_sign = u'\N{DEGREE SIGN}'
            tempval = ''
            humidval = ''
            uvval = ''
            apptempval = ''

            conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID, READ_API_KEY))

            response = conn.read()
            data = json.loads(response)
            conn.close()

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
            print "Error: %s. Cannot get weather." % e

        self.after(500, self.get_local_weather)
class News(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'News'
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        try:
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            if news_country_code == None:
                headlines_url = "https://news.google.com/news?ned=au&output=rss"
            else:
                headlines_url = "https://news.google.com/news?ned=%s&output=rss" % news_country_code

            feed = feedparser.parse(headlines_url)

            for post in feed.entries[0:5]:
                headline = NewsHeadline(self.headlinesContainer, post.title)
                headline.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            print "Error: %s. Cannot get news." % e

        self.after(600000, self.get_headlines)
class NewsHeadline(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')

        image = Image.open("assets/Newspaper.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)

        self.eventName = event_name
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.eventNameLbl.pack(side=LEFT, anchor=N)
'''
class Reddit(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.post1 = ''
        self.post2 = ''
        self.post3 = ''
        self.post4 = ''

        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=BOTTOM, anchor=E)

        self.post1Lbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.post1Lbl.pack(side=RIGHT, anchor=E)

        self.post2Lbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.post2Lbl.pack(side=RIGHT, anchor=E)

        self.post3Lbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.post3Lbl.pack(side=RIGHT, anchor=E)

        self.post4Lbl = Label(self, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.post4Lbl.pack(side=RIGHT, anchor=E)


        self.get_reddit()

    def get_reddit(self):
        try:

            reddit = praw.Reddit(client_id='44Ludf0cmZiLTg',
                     client_secret='NxpTIa74hi4udO6Mi3mSaJuNjRU', password='Sasha18898',
                     user_agent='redditapi', username='Web_Hoon')

            subreddit = reddit.subreddit('python')
            top_subreddit = subreddit.top(5)
            hot_python1 = subreddit.hot(limit=3)
            hot_python2 = subreddit.hot(limit=4)
            hot_python3 = subreddit.hot(limit=5)
            hot_python4 = subreddit.hot(limit=6)

            for submission in hot_python1:
                if not submission.stickied:
                    postval1 = "%s" % (submission.title)

            for submission in hot_python2:
                if not submission.stickied:
                    postval2 = "%s" % (submission.title)

            for submission in hot_python3:
                if not submission.stickied:
                    postval3 = "%s" % (submission.title)

            for submission in hot_python4:
                if not submission.stickied:
                    postval4 = "%s" % (submission.title)

            if self.post1 != None:
                self.post1 = postval1
                self.post1Lbl.config(text=postval1)

            if self.post2 != None:
                self.post2 = postval2
                self.post2Lbl.config(text=postval2)

            if self.post3 != None:
                self.post3 = postval3
                self.post3Lbl.config(text=postval3)

            if self.post4 != None:
                self.post4 = postval4
                self.post4Lbl.config(text=postval4)

        except Exception as d:
            traceback.print_exc()
            print "Error: %s. Cannot get reddit feed." % d

        self.after(500, self.get_reddit)
'''
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
        # weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)
        # news
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=100, pady=60)
        # reddit - removing for now
        '''
        self.reddit = Reddit(self.bottomFrame)
        self.reddit.pack(side = RIGHT, anchor=S, padx=100, pady=60)
        '''
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    w = FullscreenWindow()
    w.tk.mainloop()
