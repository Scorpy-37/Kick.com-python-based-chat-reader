from undetected_chromedriver import Chrome, By
import undetected_chromedriver as uc
from time import sleep as wait
from os import system as sys
from tkinter import messagebox

channel = open("channel.txt",'r').read()

url = "https://www.kick.com/"+channel+"/chatroom"

options = uc.ChromeOptions()
options.add_argument('--headless')
browser = Chrome(use_subprocess=True, options=options)
browser.get(url)

sys('cls')

readenMessages = []
history = []
loggedIn = False
firstRun = True
targetInterval = 0.05

def retrieve_past():
    return history
def change_interval(target):
    targetInterval = target

wait(2.5)

ready_event(channel, url)
while True:
    sample = browser.page_source
    
    if sample.find("Oops, Something went wrong") != -1:
        messagebox.showwarning("Warning", "The browser seems to have gotten a 404 error, make sure you entered your channel name into channel.txt correctly. It is case sensitive, make sure you enter just the username, not the full channel url.")

    messagesFormatted = []
    
    msgSplit = sample.split('data-chat-entry="')
    del msgSplit[0]

    msgs = []
    usrs = []
    usrs_ids = []
    ids = []

    for v in msgSplit:
        if (v.find("chatroom-history-breaker") != -1):
            continue

        ids.append(v.split('"')[0])

        currentMsgList = v.split('class="chat-entry-content">')
        del currentMsgList[0]
        currentMsg = ""

        for i in currentMsgList:
            currentMsg += i.split("</span>")[0] + " "
        currentMsg = currentMsg[0:len(currentMsg)-1]
        msgs.append(currentMsg)

        usrs.append(v.split(');">')[1].split("</")[0])
        usrs_ids.append(v.split('data-chat-entry-user-id="')[1].split('"')[0])
    
    for i,v in enumerate(msgs):
        messagesFormatted.append([usrs[i],msgs[i],ids[i],usrs_ids[i]])

    for i,v in enumerate(messagesFormatted):
        if v[2] not in readenMessages:
            newMsg = v
            if not firstRun:
                message_event(newMsg)
            else:
                history.append(newMsg)
            readenMessages.append(v[2])

    firstRun = False
    wait(targetInterval)
    tick()