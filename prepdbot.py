__author__ = "Isaac Lo"
__copyright__ = "Copyright 2015"

import feedparser
import time
import pyautogui
from subprocess import Popen

#variables
UserName = "john"
Password = "smith"
FolderName = "Articles"
WaitTime = 9
ChromiumBinary = "chromium-browser"
UserNameLocation = [403,192]
PasswordLocation = [387,237]
PrepdButtonLocation = [754,70]
FolderSelectLocation = [412,260]
CatchButtonLocation = [672,341]
#note: these coordinates given are for a 800x600 screen

#feed urls
RSSFeeds = ["feed1", "feed2", "feed3"]

FeedLinks = []

FirstBool = True

def cut(link):
    global UserName
    global Password
    global FolderName
    global WaitTime
    global ChromiumBinary
    global UserNameLocation
    global PasswordLocation
    global PrepdButtonLocation
    global FolderSelectLocation
    global CatchButtonLocation
    global FirstBool

    Popen([ChromiumBinary, link])
    print "went to rss link"
    time.sleep(WaitTime)

    pyautogui.moveTo(PrepdButtonLocation[0], PrepdButtonLocation[1])
    pyautogui.click()
    print "clicked on prepd button"
    time.sleep(WaitTime)

    if FirstBool == True:
        #login
        time.sleep(WaitTime)

        pyautogui.moveTo(PasswordLocation[0], PasswordLocation[1])
        pyautogui.click()
        pyautogui.typewrite(Password, interval=0.05)
        print "typed password"

        pyautogui.moveTo(UserNameLocation[0], UserNameLocation[1])
        pyautogui.click()
        pyautogui.typewrite(UserName, interval=0.05)
        print "typed username"

        pyautogui.press('enter')
        print "logged in"

        time.sleep(WaitTime)

    pyautogui.moveTo(FolderSelectLocation[0], FolderSelectLocation[1])
    pyautogui.click()
    print "clicked on folder selection"

    pyautogui.typewrite(FolderName, interval=0.05)
    pyautogui.press('enter')
    print "typed into folder selection"


    pyautogui.moveTo(CatchButtonLocation[0], CatchButtonLocation[1])
    pyautogui.click()
    time.sleep(WaitTime)
    print "caught article"

    pyautogui.press("esc")

    pyautogui.hotkey('ctrl', 'w')
    print "closed tab"

    #exit()

Popen([ChromiumBinary, "--start-maximized"])
print "done"

while True:
    for i in xrange(0,len(RSSFeeds)):
        links = feedparser.parse(RSSFeeds[i])

        for j in xrange(0,len(links["entries"])):
            FeedLinks.append(links.entries[j]['link'])
            print links.entries[j]['link']
            #run cutting function
            cut(links.entries[j]['link'])
            FirstBool = False

        print FeedLinks

        #delete all the content of FeedLinks
        del FeedLinks[:]
