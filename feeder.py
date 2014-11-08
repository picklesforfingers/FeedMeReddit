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
    #Titles
    thist = open("title.obj", 'rb')
    titlehistory = pickle.load(thist)
    thist.close()
    #URLs
    uhist = open("url.obj", 'rb')
    urlhistory = pickle.load(uhist)
    uhist.close()
    #Comment Permalinks
    phist = open("perma.obj", 'rb')
    permahistory = pickle.load(phist)
    phist.close()


    #Gets new posts from subreddit
    r = urllib.request.urlopen(r'http://www.reddit.com/r/programming/new/.json', timeout = 60).read().decode("utf-8")
    data = json.loads(r)

    #Creates lists to store data
    title =[]
    url = []
    permalink = []

    #Stores titles and urls to lists
    for i in range(0,limit):
        title.append(data['data']['children'][i]['data']['title'])  #Gets title
        url.append(data['data']['children'][i]['data']['url'])  #Gets URL
        permalink.append("http://www.reddit.com" + data['data']['children'][i]['data']['permalink'])  #Gets Comments

    for i in range(len(title)):
        titlehistory.append(title[i])

    for i in range(len(url)):
        urlhistory.append(url[i])

    for i in range(len(permalink)):
        permahistory.append(url[i])


    #Pickles title history
    thist = open("title.obj", 'wb')
    pickle.dump(titlehistory, thist)
    thist.close()

    #Pickles url history
    turl = open("url.obj", 'wb')
    pickle.dump(urlhistory, turl)
    turl.close()

    #Pickles permalink history
    tperma = open("perma.obj", 'wb')
    pickle.dump(permahistory, tperma)
    tperma.close()