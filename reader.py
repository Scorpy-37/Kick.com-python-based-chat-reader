from selenium import webdriver
from time import sleep as wait
from bs4 import BeautifulSoup as bs
from os import system as sys
from tkinter import messagebox

channel = open("channel.txt",'r').read()

url = "https://www.kick.com/"+channel

browser = webdriver.Chrome()
browser.get(url)

skipwarns = eval(open("skip_warnings.txt").read())

if not skipwarns:
    messagebox.showwarning("Important", "If you're not streaming, please press the 'Chat' button to open the chat, otherwise the script will fail to receive usernames.")

readenMessages = []

def preheat():
    global browser
    global readenMessages
    sample = browser.page_source
    
    if sample.find("Oops, Something went wrong") != -1:
        messagebox.showwarning("Warning", "The browser seems to have gotten a 404 error, make sure you entered your channel name into channel.txt correctly. If you did, restart the script and try again. If this problem persists please contact the developer at Scorp#1348 on Discord.")
    if sample.find('<div data-v-1e3ffa3e="" data-v-46a070dd="" class="quick-emotes-holder">') == -1:
        messagebox.showwarning("Warning", "The 'quick-emotes-holder' seems to not show up, this most likely indicates that chat will not receive messages. Try restarting the script. If this problem persists please contact the developer at Scorp#1348 on Discord.")

    sample = bs(sample, "html.parser")
    container = sample.find("div",{"id":"chatroom"})
    messages = str(container)
    
    messagesFormatted = []
    
    msgSplit = messages.split('<div class="break-all mt-0.5"')
    del msgSplit[0]
    msgs = []
    usrs = []
    ids = []
    for v in msgSplit:
        ids.append(v.split('data-chat-entry="')[1].split('"')[0])
        currentMsgList = v.split('<span class="chat-entry-content" data-v-89ba08de="">')
        del currentMsgList[0]
        currentMsg = ""
        for i in currentMsgList:
            currentMsg += i.split("</span>")[0] + " "
        currentMsg = currentMsg[0:len(currentMsg)-1]
        msgs.append(currentMsg)
    
    for v in msgSplit:
        usrs.append(v.split('data-chat-entry-user="')[1].split('"')[0])
    
    for i,v in enumerate(msgs):
        messagesFormatted.append([usrs[i],msgs[i],ids[i]])

    for i,v in enumerate(messagesFormatted):
        if v[2] not in readenMessages:
            readenMessages.append(v[2])

preheat()
ready_event(channel, url)
while True:
    try:
        sample = browser.page_source
        
        if sample.find("Oops, Something went wrong") != -1:
            messagebox.showwarning("Warning", "The browser seems to have gotten a 404 error, make sure you entered your channel name into channel.txt correctly. If you did, restart the script and try again. If this problem persists please contact the developer at Scorp#1348 on Discord.")
        if sample.find('<div data-v-1e3ffa3e="" data-v-46a070dd="" class="quick-emotes-holder">') == -1:
            messagebox.showwarning("Warning", "The 'quick-emotes-holder' seems to not show up, this most likely indicates that chat will not receive messages. Try restarting the script. If this problem persists please contact the developer at Scorp#1348 on Discord.")

        sample = bs(sample, "html.parser")
        container = sample.find("div",{"id":"chatroom"})
        messages = str(container)
        
        messagesFormatted = []
        
        msgSplit = messages.split('<div class="break-all mt-0.5"')
        del msgSplit[0]
        msgs = []
        usrs = []
        ids = []
        for v in msgSplit:
            ids.append(v.split('data-chat-entry="')[1].split('"')[0])
            currentMsgList = v.split('<span class="chat-entry-content" data-v-89ba08de="">')
            del currentMsgList[0]
            currentMsg = ""
            for i in currentMsgList:
                currentMsg += i.split("</span>")[0] + " "
            currentMsg = currentMsg[0:len(currentMsg)-1]
            msgs.append(currentMsg)
        
        for v in msgSplit:
            usrs.append(v.split('data-chat-entry-user="')[1].split('"')[0])
        
        for i,v in enumerate(msgs):
            messagesFormatted.append([usrs[i],msgs[i],ids[i]])

        for i,v in enumerate(messagesFormatted):
            if v[2] not in readenMessages:
                newMsg = v
                message_event(newMsg)
                readenMessages.append(v[2])

        wait(0.05)
    except Exception as e:
        error_event("[Caught error in reader.py]: "+e)