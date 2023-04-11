from selenium import webdriver
from os import system as sys
from time import sleep as wait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://github.com/Scorpy-37/KickStreaming-chat-reader/blob/main/version")
sample = browser.page_source
browser.close()

detectedVersion = str(open("version").read())
latestVersion = sample.split('<td id="LC1" class="blob-code blob-code-inner js-file-line">')[1].split('</td>')[0]

sys("cls")
statement = ""
if detectedVersion != latestVersion:
    print("[Updater] Looks like there's a newer version available!\n\nYou're running: "+detectedVersion+"\nLatest version: "+latestVersion)
    print("\nYou can get the newer version from https://github.com/Scorpy-37/KickStreaming-chat-reader")
else:
    print("[Updater] The script is up to date!")

input()