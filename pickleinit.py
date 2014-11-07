"""Temporary file for testing purposes. Creates pickle objects when needed"""
import pickle
import json
import requests
import urllib.request

def guiinit():

    r = urllib.request.urlopen(r'http://www.reddit.com/r/programming/new/.json', timeout=60).read().decode("utf-8")
    data = json.loads(r)
    t = []
    u = []
    p = []

    title = open("title.obj", 'wb')
    url = open("url.obj", 'wb')
    permalink = open("perma.obj", 'wb')
    for i in range(0,20):
        t.append(data['data']['children'][i]['data']['title'])  #Gets title
        u.append(data['data']['children'][i]['data']['url'])  #Gets URL
        p.append("http://www.reddit.com" + data['data']['children'][i]['data']['permalink'])  #Gets Comments
    pickle.dump(t, title)
    pickle.dump(u, url)
    pickle.dump(p, permalink)
    title.close()
    url.close()
    permalink.close()