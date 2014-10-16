"""This is the gui that everything displays on. It uses the tkinter framework

Last Updated 16 October 2014
"""

from tkinter import *
import pickle
from FeedMeReddit import feeder
from FeedMeReddit import manager
import webbrowser

class Display(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    """Opens the address of the reddit post picked"""
    def urlOpen(self, feed, var):
        webbrowser.open(feed[var], new=0, autoraise=True)

    """Creates button"""
    def createWidgets(self):
        #Grabs titles and urls
        self.feed = self.getPickle()
        
        #Creates buttons
        for x in range(len(self.feed[0])):
            self.var = x
            self.button = Button(self)
            self.button["text"] = self.feed[0][x],
            self.button["command"] = lambda: self.urlOpen(self.feed[1], self.var)
            self.button.pack({"side": "top"})

    """Gets pickle data"""
    def getPickle(self):
        #Temporary gui initialization
        feeder.gethistory(20, 'programming')
        manager.picklefix()
        
        #Loads Titles
        self.title = open("title.obj", "rb")
        self.thist = pickle.load(self.title)
        self.title.close()

        #Loads URLS
        self.url = open("url.obj", "rb")
        self.uhist = pickle.load(self.url)
        self.url.close()
    
        self.list = [self.thist, self.uhist]

        return self.list

#Frame Loop
app = Tk()
gui = Display(master=app)
gui.mainloop()
app.destroy()
