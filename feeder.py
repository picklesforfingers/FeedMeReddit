"""
Feeder:
This program interacts with the Reddit API. It grabs the most recent posts and stores them in pickle files.

Last update: 6 November 2014
"""

import requests
import urllib
import json
import pickle


#Need to flesh out saving
#Note to self: create better variable names


"""Get history interacts with API then saves lists to pickle files"""
def gethistory(limit,subreddit):
    #Grabs history from files
    thist = open("title.obj", 'rb')
    tinitial = pickle.load(thist)
    thist.close()
    uhist = open("url.obj", 'rb')
    uinitial = pickle.load(uhist)
    uhist.close()


    #Gets new posts from subreddit
    r = urllib.request.urlopen(r'http://www.reddit.com/r/programming/new/.json', timeout = 60).read().decode("utf-8")
    data = json.loads(r)

    #Creates lists to store data
    title =[]
    url = []

    #Stores titles and urls to lists
    for i in range(0,limit):
        title.append(data['data']['children'][i]['data']['title'])  #Gets title
        url.append(data['data']['children'][i]['data']['url'])  #Gets URL

    for i in range(len(title)):
        tinitial.append(title[i])

    for i in range(len(url)):
        uinitial.append(url[i])



    #Pickles title history
    thist = open("title.obj", 'wb')
    pickle.dump(tinitial, thist)
    thist.close()

    #Pickles url history
    turl = open("url.obj", 'wb')
    pickle.dump(uinitial, turl)
    turl.close()

"""For testing
   Uses reddit.com/r/programming/new as example subreddit
   Limits history to 20"""
if __name__ == "__main__":
    gethistory(20, "programming") #(limit, subreddit)
    tfile = open("title.obj", 'rb') #opens title file
    ufile = open("url.obj", 'rb')  #opens url file
    tout = pickle.load(tfile)
    uout = pickle.load(ufile)

    #Prints out data
    for i in range(len(tout)):
        print(tout[i])
        print(uout[i])

    tfile.close()
    ufile.close()
