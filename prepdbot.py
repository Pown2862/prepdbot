__author__ = "Isaac Lo"
__copyright__ = "Copyright 2015"
#PrepdBot Standalone

import time
import pyautogui
import feedparser
from subprocess import Popen

#variables
UserName = "john"
Password = "smith"
WaitTime = 9
ChromiumBinary = "chromium-browser"

#note: these coordinates given are for a 800x600 screen
UserNameLocation = [403,192]
PasswordLocation = [387,237]
PrepdButtonLocation = [754,70]
FolderSelectLocation = [412,260]
CatchButtonLocation = [672,341]

#feed urls
RSSFeeds = [
["http://feeds.reuters.com/reuters/businessNews", "Buisness"],
["http://feeds.reuters.com/reuters/companyNews", "Companies"],
["http://feeds.reuters.com/reuters/environment", "Environment"],
["http://feeds.reuters.com/news/wealth", "Money"],
["http://feeds.reuters.com/Reuters/PoliticsNews", "Politics"],
["http://feeds.reuters.com/Reuters/domesticNews", "Domestic News"]
]


FirstBool = True

def cut(link, FolderName):
    global UserName
    global Password
    global WaitTime
    global ChromiumBinary
    global UserNameLocation
    global PasswordLocation
    global PrepdButtonLocation
    global FolderSelectLocation
    global CatchButtonLocation
    global FirstBool

    print "Link: " + link
    print "Folder Name: " + FolderName + "\n"

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
    print "closed tab\n"

Popen([ChromiumBinary, "--start-maximized"])
time.sleep(WaitTime)
print "done"

Cuts = 0

while True:
    for i in xrange(0,len(RSSFeeds)):
        links = feedparser.parse(RSSFeeds[i][0])

        for j in xrange(0,len(links["entries"])):
            TheLink = links.entries[j]['link']
            FolderName = RSSFeeds[i][1]
            print "Link: " + TheLink
            print "Folder Name: " + FolderName
            #increment number of articles cut
            cut(TheLink, FolderName)
            FirstBool = False

            Cuts = Cuts + 1
            print "Articles Cut: " + str(Cuts) + "\n"
