"""Temporary file for testing purposes. Creates pickle objects when needed"""
import pickle
import json
import requests
import urllib.request

if __name__ == '__main__':

    r = urllib.request.urlopen(r'http://www.reddit.com/r/programming/new/.json', timeout=60).read().decode("utf-8")
    data = json.loads(r)
    t = []
    u = []

    title = open("title.obj", 'wb')
    url = open("url.obj", 'wb')

    for i in range(0,20):
        t.append(data['data']['children'][i]['data']['title'])  #Gets title
        u.append(data['data']['children'][i]['data']['url'])  #Gets URL
    pickle.dump(t, title)
    pickle.dump(u, url)
    title.close()
    url.close()