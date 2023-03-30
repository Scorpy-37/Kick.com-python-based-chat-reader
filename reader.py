from selenium import webdriver
from time import sleep as wait
from bs4 import BeautifulSoup as bs

channel = open("channel.txt",'r').read()

url = "https://kick.com/"+channel

browser = webdriver.Edge()
browser.get(url)

lastData = ""
firstRun = True

while True:
    sample = browser.page_source

    sample = bs(sample, "html.parser")
    container = sample.find("div",{"id":"messagesContainer"})
    messages = str(container)
    
    messagesFormatted = []
    
    msgSplit = messages.split('<div class="w-full pr-5 text-sm" data-v-5ccda75c="">')
    del msgSplit[0]
    msgs = []
    usrs = []
    for v in msgSplit:
        currentMsgList = v.split('<span class="break-words" data-v-b948c69d=""><span class="align-middle" data-v-b948c69d="">')
        del currentMsgList[0]
        currentMsg = ""
        for i in currentMsgList:
            currentMsg += i.split("</span></span>")[0] + " "
        currentMsg = currentMsg[0:len(currentMsg)-1]
        msgs.append(currentMsg.replace("\xa0",""))
        
    for v in msgSplit:
        usrs.append(v.split('<span class="inline-flex items-center align-middle font-bold" data-v-b948c69d="" style="color: rgb(')[1].split(">")[1].split("<")[0])
    
    for i,v in enumerate(msgs):
        messagesFormatted.append([usrs[i],msgs[i]])

    if str(messagesFormatted) != lastData and not firstRun:
        latestMessage = messagesFormatted[len(messagesFormatted)-1]
        message_event(latestMessage)
    firstRun = False
    lastData = str(messagesFormatted)

    wait(0.1)