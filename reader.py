from selenium import webdriver
from time import sleep as wait
from bs4 import BeautifulSoup as bs
from os import system as sys

channel = open("channel.txt",'r').read()

url = "https://www.kick.com/"+channel

browser = webdriver.Edge()
browser.get(url)

readenMessages = []

ready_event(channel, url)
while True:
    sample = browser.page_source
    
    if sample.find("Oops, Something went wrong") != -1:
        sys("cls")
        input("[KickStreaming Chat Reader] Looks like something went wrong when loading the page!\nAre you sure that "+url+" leads to your channel page?\nIf not please configure the channel.txt file to have your channel username in it.\nIf the channel name is correct try closing the script and running it again.\nIf you have consistant problems for a while please contact me on Discord at Scorp#1348\n\n")

    sample = bs(sample, "html.parser")
    container = sample.find("div",{"id":"messagesContainer"})
    messages = str(container)
    
    messagesFormatted = []
    
    msgSplit = messages.split('<div class="message"')
    del msgSplit[0]
    msgs = []
    usrs = []
    ids = []
    for v in msgSplit:
        ids.append(v.split('="" id="message-')[1].split('"')[0])
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
        messagesFormatted.append([usrs[i],msgs[i],ids[i]])

    for i,v in enumerate(messagesFormatted):
        if v[2] not in readenMessages:
            newMsg = v
            message_event(newMsg)
            readenMessages.append(v[2])

    wait(0.05)