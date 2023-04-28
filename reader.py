from undetected_chromedriver import Chrome, By
from time import sleep as wait
from bs4 import BeautifulSoup as bs
from os import system as sys
from tkinter import messagebox

channel = open("channel.txt",'r').read()

url = "https://www.kick.com/"+channel

browser = Chrome(use_subprocess=True)
browser.get(url)

readenMessages = []
history = []
loggedIn = False
firstRun = True
targetInterval = 0.05

def retrieve_past():
    return history
def change_interval(target):
    targetInterval = target

def login(username = None, password = None):
    if username == None or password == None:
        print("Username or password not specified!\nUsage: login(username, password)")
        return

    global firstRun
    global loggedIn

    print("Logging in...")

    elm = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/nav/div/div[3]/div[2]/button[1]")
    elm.click()
    wait(1)
    elm = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/form/div/div/form/div[2]/input")
    elm.send_keys(username)
    elm = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/form/div/div/form/div[3]/div/input")
    elm.send_keys(password)
    wait(1)
    elm = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/form/div/div/form/button")
    elm.click()
    wait(1)
    browser.get(url)
    firstRun = True
    wait(2.5)
    loggedIn = True
    print("Successfully logged in to "+username+"!")

def send_message(content):
    if not loggedIn:
        print("Sending message without being logged in!\nPlease use login() before sending messages.")
        return
    elm = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div[2]/div/div")
    elm.send_keys(content)
    wait(0.1)
    elm = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button")
    elm.click()

wait(2.5)

ready_event(channel, url)
while True:
    sample = browser.page_source
    
    if sample.find("Oops, Something went wrong") != -1:
        messagebox.showwarning("Warning", "The browser seems to have gotten a 404 error, make sure you entered your channel name into channel.txt correctly. It is case sensitive, make sure you enter just the username, not the full channel url.")

    sample = bs(sample, "html.parser")
    container = sample.find("div",{"id":"chatroom"})
    messages = str(container)

    messagesFormatted = []
    
    msgSplit = messages.split('</div><div class="break-all mt-0.5"')

    del msgSplit[0]
    for i in range(len(msgSplit) - 1):
        if msgSplit[i].find('"history_breaker"') != -1:
            del msgSplit[i]

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