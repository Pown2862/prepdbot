#Reuters cutbot

import feedparser
import time
import pyautogui
from subprocess import Popen

#mouse variables
PrepdButtonLocation = [754,70]
FolderSelectLocation = [412,260]
CatchButtonLocation = [672,341]

print "Log into the Prepd extension on a chrome window and leave it open.\nThen hit the return key."
raw_input()

#feed urls
RSSFeeds = ["http://feeds.reuters.com/reuters/businessNews", "http://feeds.reuters.com/reuters/environment", "http://feeds.reuters.com/news/wealth", "http://feeds.reuters.com/Reuters/PoliticsNews", "http://feeds.reuters.com/reuters/scienceNews", "http://feeds.reuters.com/reuters/technologyNews"]

#start by placing first link here (to compare when links overlap)
FirstLinks = [None] * len(RSSFeeds)

FeedLinks = []


def wait(ATime):
    if ATime == "long":
        time.sleep(8)
    if ATime == "short":
        time.sleep(0.5)

def cut(link):
    global PrepdButtonLocation
    global FolderSelectLocation
    global CatchButtonLocation

    Popen(["chromium-browser", link])
    print "went to rss link"
    wait("long")

    pyautogui.moveTo(PrepdButtonLocation[0], PrepdButtonLocation[1])
    pyautogui.click()
    print "clicked on prepd button"
    wait("long")

    pyautogui.moveTo(FolderSelectLocation[0], FolderSelectLocation[1])
    pyautogui.click()
    print "clicked on folder selection"
    wait("short")

    pyautogui.typewrite('Articles', interval=0.05)
    pyautogui.press('enter')
    print "typed into folder selection"
    wait("short")

    pyautogui.moveTo(CatchButtonLocation[0], CatchButtonLocation[1])
    pyautogui.click()
    wait("long")

    pyautogui.press("esc")

    pyautogui.hotkey('ctrl', 'w')

    #exit()

Popen(["chromium-browser", "--start-maximized"])
print "done"

while True:

    for i in xrange(0,len(RSSFeeds)):
        links = feedparser.parse(RSSFeeds[i])

        #to see when feeds overlap
        for j in xrange(0,len(links["entries"])):
            if links.entries[j]['link'] == FirstLinks[i]:
                break
            else:
                FeedLinks.append(links.entries[j]['link'])
                print links.entries[j]['link']
                #run cutting function
                cut(links.entries[j]['link'])
        FirstLinks.append(links.entries[0]['link'])


        print FeedLinks

        #delete all the content of FeedLinks
        del FeedLinks[:]
