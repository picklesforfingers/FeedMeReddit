""" Initializes Pickly Files"""
import pickle
import json
import requests
import urllib.request

def guiinit(sub):

    #Gets information from Reddit
    r = urllib.request.urlopen(r'http://www.reddit.com/r/' + sub + '/new/.json', timeout=60).read().decode("utf-8")
    data = json.loads(r)

    #Creates ists to hold data
    titlelist = []
    urllist = []
    permalinklist = []

    #Creats Files
    title = open("title.obj", 'wb')
    url = open("url.obj", 'wb')
    permalink = open("perma.obj", 'wb')

    #Appends Data from Reddit API to lists
    for i in range(0,20):
        titlelist.append(data['data']['children'][i]['data']['title'])  #Gets title
        urllist.append(data['data']['children'][i]['data']['url'])  #Gets URL
        permalinklist.append("http://www.reddit.com" + data['data']['children'][i]['data']['permalink'])  #Gets Comments

    #Dumps lists to files
    pickle.dump(titlelist, title)
    pickle.dump(urllist, url)
    pickle.dump(permalinklist, permalink)

    #Closes files
    title.close()
    url.close()
    permalink.close()