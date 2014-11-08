"""This is the gui that everything displays on. It uses the tkinter framework

Last Updated 6 November 2014
"""

from tkinter import *
import pickle
from FeedMeReddit import feeder
from FeedMeReddit import manager
from FeedMeReddit import pickleinit
import webbrowser


try:
    open("title.obj", "rb")
except OSError as err:
    pickleinit.guiinit()

class Display(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, background = "white")
        self.pack()
        #self.createLabels()
        self.createWidgets()

    """Opens the address of the reddit post picked"""
    def urlOpen(self, feed, perma, x):
        webbrowser.open(feed[x], new=0, autoraise=True)
        webbrowser.open(perma[x], new=0, autoraise=True)


    def createWidgets(self):
        #Subreddit Entry
        self.enterSub = Entry(self)
        self.enterSub["width"] = 25
        self.enterSub.grid(row=1, column=0)

        #Button to Enter Subreddit
        self.enbutton = Button(self)
        self.enbutton["width"] = 5
        self.enbutton["text"] = "enter"
        self.enbutton["command"] = lambda : self.createLabels(self.enterSub.get())
        self.enbutton.grid(row=1, column=1)

    """Creates button"""
    def createLabels(self, sub):
        #Grabs titles and urls
        self.feed = self.getPickle(sub)
        #Creates buttons
        for x in range(len(self.feed[0])):
            self.button = Button(self)
            self.button["anchor"] = CENTER
            if len(self.feed[0][x]) < 37:
                self.button["text"] = self.feed[0][x]
            else:
                self.button["text"] = self.feed[0][x][:36] + "..."
            self.button["command"] = lambda x = x: self.urlOpen(self.feed[1], self.feed[2], x)
            self.button["background"] = "white"
            self.button["width"] = 30

            self.button.grid(row=x+2, column=0)

    """Gets pickle data"""
    def getPickle(self, sub):
        #Gets Posts
        pickleinit.guiinit(sub)
        manager.picklefix()
        
        #Loads Titles
        self.title = open("title.obj", "rb")
        self.thist = pickle.load(self.title)
        self.title.close()

        #Loads URLS
        self.url = open("url.obj", "rb")
        self.uhist = pickle.load(self.url)
        self.url.close()

        #Loads Permas
        self.perma = open("perma.obj", 'rb')
        self.phist = pickle.load(self.perma)
        self.perma.close()

        self.list = [self.thist, self.uhist, self.phist]

        return self.list

#Frame Loop
app = Tk()
app.attributes('-zoomed', True)
app.configure(background='light cyan')
gui = Display(master=app)
gui.mainloop()
app.destroy()
