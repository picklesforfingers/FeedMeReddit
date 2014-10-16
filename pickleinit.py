"""Temporary file for testing purposes. Creates pickle objects when needed"""
import pickle
import requests

if __name__ == '__main__':

    r = requests.get(r'http://www.reddit.com/r/programming/new/.json', timeout=60)
    data = r.json()
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