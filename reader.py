import undetected_chromedriver as uc
from time import sleep as wait
from bs4 import BeautifulSoup as bs
from os import system as sys
from tkinter import messagebox

channel = open("channel.txt",'r').read()

url = "https://www.kick.com/"+channel

browser = uc.Chrome(use_subprocess=True)
browser.get(url)

readenMessages = []
history = []
firstRun = True
targetInterval = 0.05

def retrieve_past():
    return history
def change_interval(target):
    targetInterval = target

wait(5)

ready_event(channel, url)
while True:
    sample = browser.page_source
    
    if sample.find("Oops, Something went wrong") != -1:
        messagebox.showwarning("Warning", "The browser seems to have gotten a 404 error, make sure you entered your channel name into channel.txt correctly. It is case sensitive, make sure you enter just the username, not the full channel url.")

    sample = bs(sample, "html.parser")
    container = sample.find("div",{"id":"chatroom"})
    messages = str(container)

    messagesFormatted = []
    
    msgSplit = messages.split('</span></span></div></div></div><div class="break-all mt-0.5"')

    del msgSplit[0]

    msgs = []
    usrs = []
    usrs_ids = []
    ids = []
    for v in msgSplit:
        ids.append(v.split('data-chat-entry="')[1].split('"')[0])
        currentMsgList = v.split('class="chat-entry-content"')
        del currentMsgList[0]
        currentMsg = ""
        for i in currentMsgList:
            currentMsg += i.split("</span>")[0][len(' data-v-89ba08de="">')::] + " "
        currentMsg = currentMsg[0:len(currentMsg)-1]
        msgs.append(currentMsg)

        usrs.append(v.split('data-chat-entry-user-id="')[1].split("</span>")[0].split(';">')[1])
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