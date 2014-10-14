"""
This File grabs files from feeder.py and analyzes the data and deletes repeat enteries so that posts do not show up multiple times. This is using URL instead of Title because using title could make posts with the same title but different creators be deleted because it looks like a repost.

Last Updated 14 October 2014
"""

#This file has not yet been tested to see if it runs. Being created away from a python environment

import pickle

"""Loads files containing current feeder history and saves them to a list"""
def loadfiles():
  #Opens files
  title = open('title.obj', 'rb')
  url = open('url.obj', 'rb')
  
  #Saves to list
  tlist = pickle.load(title)
  ulist = pickle.load(url)
  
  #Closes files
  title.close()
  url.close()
  
  #Creates a list holding the titles and urls
  history = [tlist, ulist]
  
  #Returns data
  return history
  

"""Calls loadfiles() then fixes title and url history"""
def managefiles():
  #Gets list of titles and urls
  history = loadfiles()
  
  #Deletes repeat entries
  for i in range(len(history[1])):
    for x in range(len(history[1])):
      if history[1][i] == history[1][x] && i != x:
          history[0].pop(x)
          history[1].pop(x)
          x -= 1 #Not sure about these. 
          if i != 0:  #The thought is that the indexes will change and I should go over them again to prevent errors
            i -= 1 #I will have to test them
  
  #Deletes entery if list is over 100
  if len(history[1]) > 100:
    for i in range(100, len(history[1])):
      history[0].pop(i)
      history[1].pop(i)
  
  #Returns new history
  return history

"""Calls managefiles() which calls loadfiles(). Calling this will fix the histories (so it is the only function that actually needs to be called from manager.py). Also saves everything back to the pickle files"""  
def picklefix():
  #Gets history
  history = managefiles()

  #Opens files to dump to
  title = open('title.obj', 'wb')
  url = open('url.obj', 'wb')
  
  #Dumps lists into files
  pickle.dump(history[0], title)
  pickle.dump(history[1], url
  
  #Closes files
  title.close()
  url.close()




"""For testing"""
#This test assumes feeder.py has already been run and that there are the requested .obj files for loader.py to use
if __init__ == '__main__':
  picklefix()
  
  #Prints content from fixed files 
  #May be unchanged depending on content generated in feeder.py
  title = open('title.obj', 'rb')
  url = open('url.obj', 'rb')
  t = pickle.load(title)
  u = pickle.load(url)
  print (t)
  print (u)
  title.close()
  url.close()
  
