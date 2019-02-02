#!/usr/bin/python3
import webbrowser
import time


mysocialsites = ['https://google.com', 'https://facebook.com', 'https://twitter.com', 'https://coinmarketcap.com',
                 'https://youtube.com']
answer = input('Would you like to add a new webpage to your existing Newsfeeder(y/n)? ')

if answer == 'y' or answer == 'n':

    if answer == 'n':

        for x in mysocialsites:
            webbrowser.open(x)
            time.sleep(2)

    else:
        newWebsite = input('Please enter new website url: ')
        mysocialsites.append(newWebsite)
        #print(mysocialsites)

        for y in mysocialsites:
            webbrowser.open(y)
            time.sleep(2)
else:
    for x in mysocialsites:
        webbrowser.open(x)
        time.sleep(2)   

