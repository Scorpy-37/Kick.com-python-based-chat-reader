import undetected_chromedriver as webdriver
from os import system as sys
from time import sleep as wait
from selenium.webdriver.chrome.options import Options

print("Checking...")

opts = webdriver.ChromeOptions()
opts.add_argument("--headless")
browser = webdriver.Chrome(options=opts,use_subprocess=True)

browser.get("https://raw.githubusercontent.com/Scorpy-37/Kick.com-python-based-chat-reader/main/version")
sample = browser.page_source
browser.close()

detectedVersion = str(open("version").read())
latestVersion = sample.split('pre-wrap;">')[1].split("</pre></body></html>")[0]
sys("cls")
statement = ""
if detectedVersion != latestVersion:
    print("[Updater] Looks like there's a newer version available!\n\nYou're running: "+detectedVersion+"\nLatest version: "+latestVersion)
    print("\nYou can get the newer version from https://github.com/Scorpy-37/KickStreaming-chat-reader")
else:
    print("[Updater] The script is up to date!")

input()