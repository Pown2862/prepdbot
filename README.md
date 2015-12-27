# prepdbot
Prepdbot is a script that automatically cuts articles for [Prepd](https://prepd.in) from given RSS feeds.

##Configuration
* UserName: your Prepd username
* Password: your Prepd password
* FolderName: the folder you want you articles to be cut to
* WaitTime: time to wait for your RSS-given webpage or for Prepd to load
* ChromiumBinary: location of your chromium browser binary
* UserNameLocation: location to click to enter your username
* PasswordLocation: location to click to enter your password
* PrepdButtonLocation: location to click you prepd extension button
* FolderSelectLocation: location to enter your folder name for Prepd
* CatchButtonLocation: location to click the Prepd "Catch" button (after folder is entered)
* RSSFeeds: An array with the URLs for the RSS feeds used to cut articles

##Dependacies
* Python 2.7
* feedparser
* pyautogui
* chromium-browser
* (all subdependacies)

##Instructions
1. Ensure that all open chromium windows are closed.
2. Run the prepdbot script.
