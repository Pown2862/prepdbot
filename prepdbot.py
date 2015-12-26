#cutbot

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
RSSFeeds = ["http://rss.cnn.com/rss/cnn_topstories.rss", "http://feeds.nytimes.com/nyt/rss/HomePage", "http://www.washingtonpost.com/rss", "http://hosted.ap.org/lineups/USHEADS-rss_2.0.xml?SITE=RANDOM&SECTION=HOME", "http://rssfeeds.usatoday.com/usatoday-NewsTopStories", "http://www.npr.org/rss/rss.php?id=1001" "http://newsrss.bbc.co.uk/rss/newsonline_world_edition/americas/rss.xml", "http://hosted.ap.org/lineups/SCIENCEHEADS-rss_2.0.xml?SITE=OHLIM&SECTION=HOME", "http://feeds.sciencedaily.com/sciencedaily", "http://feeds.nature.com/nature/rss/current", "http://www.techlearning.com/RSS", "http://feeds.wired.com/wired/index", "http://feeds.nytimes.com/nyt/rss/Technology", "http://www.npr.org/rss/rss.php?id=1019", "http://feeds.feedburner.com/FrontlineEditorsNotes", "http://www.npr.org/rss/rss.php?id=1008", "http://www.salon.com/?source=rss&aim=/"]

FeedLinks = []


def wait(ATime):
    if ATime == "long":
        time.sleep(7.5)
    if ATime == "short":
        time.sleep(0.2)

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

        for j in xrange(0,len(links["entries"])):
            FeedLinks.append(links.entries[j]['link'])
            print links.entries[j]['link']
            #run cutting function
            cut(links.entries[j]['link'])

        print FeedLinks

        #delete all the content of FeedLinks
        del FeedLinks[:]
