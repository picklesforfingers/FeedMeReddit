"""
Feeder:
This program interacts with the Reddit API. It grabs the most recent posts and stores them in pickle files.

Last update: 14 October 2014
"""

import requests
import json
import pickle


#Need to flesh out saving

"""Get history interacts with API then saves lists to pickle files"""
def gethistory(limit,subreddit):

    #Gets new posts from subreddit
    r = requests.get(r'http://www.reddit.com/r/' + subreddit + '/new/.json')
    data = r.json()

    #Creates lists to store data
    title =[]
    url = []

    #Stores titles and urls to lists
    for i in range(0,limit):
        title.append(data['data']['children'][i]['data']['title'])  #Gets title
        url.append(data['data']['children'][i]['data']['url'])  #Gets URL

    #Pickles title history
    thist = open("title.obj", 'wb')
    pickle.dump(title, thist)
    thist.close()

    #Pickles url history
    turl = open("url.obj", 'wb')
    pickle.dump(url, turl)
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
