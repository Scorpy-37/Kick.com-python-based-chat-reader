Hello! Thank you for using my script for reading Kick.com chat messages :3

Need help with anything? Contact me on Discord at 37scorpions!
Just please DM me saying what you want, don't just go "hi" and wait for my response.
Also before you ask me to explain you anything please tell me your skill level: Have you used a computer? Have you used a command prompt? Have you used Python? This helps me determine how much I need to explain to you as I may just start explaining the history of python.
Brief warning before you contact me though, I'm a furry and I like boys.

If you don't like reading, just quickly skim over this file and read anything that catches your eye. It is quite important to read this to understand how to use it.



IMPORTANT NOTE TO FUTURE PEOPLE:

So as I watch my script age I notice how in the future it will most likely become rather useless. Why may you ask? Well, you see, this script was made at the very start of Kick.com when no one had their hands on any APIs or API wrappers. This script opens a browser and reads the messages through it, but I see people venturing into the Kick.com API and making easier to use and generally more practical API wrappers which not only improve the chat reading but also add ways to send messages into chat. Even if you just want to use this script to read your chat I advise you find something else only using this script as a last resort. This script breaks very fast if the structure of Kick changes, meanwhile an API wrapper is going to be more maintained and stable. I just want to mention this because a few people have come to me asking why I did it the way I did it, and this is the answer.
If you want a good API wrapper, I linked one at the bottom of this file.

TLDR: Script is old (but still maintained), use other newer script for better experiance. 



SETUP:

1: Run "install.py" to install required packages
2: Open the channel.txt file and enter your channels username
3: Open script.py with notepad, notepad++, sublime text or whatever you want
4: Edit the code to do what you want it to do
5: Save it and run executor.py
6: Done!



NOTES:

- Make sure to run update.py every once in a while to check for new updates to the script.
- You don't need to be streaming for this script to work.
- Make sure you have Chrome installed, undetected-chromedriver may not function without it.
- If the script doesn't work, give it a kiss and try again.
- If the script still doesn't work, contact me on Discord.
- If you have package related issues (ones coming from packages instead of the scripts themselves) try installing these specific versions of the required packages: selenium 4.10.0, undetected_chromedriver 3.5.3



Q&A:

- How does it work?
It launches a browser (Chrome), goes to your channels chatroom page on Kick.com and reads the page source to fetch messages.

- Is this allowed?
I have no idea. Other Kick.com bots like Botrix use a browser extension to view things like alerts and such, I don't think this is that far from that.

- Why should I use this?
No reason, as people look deeper and deeper into Kicks API a lot of more conviniant wrappers are getting out into the public. This script was made at the very start of Kick when no one knew anything about the API so it was pretty useful back then, now it's kind of useless.

- Is it reliable?
Since v1.6 the script is way more reliable as it never gets detected as a fake browser. In terms of being up to date to the website, as I no longer stream myself I may not notice if the script breaks due to a website HTML structure update, though if you notify me I will try to push a fix as soon as possible. If you noticed the script doesn't work and you believe it's the scripts fault, you can always contact me on Discord.

- Can I send chat messages with this?
Yes, but no... well, you kind of could but not anymore. If you're looking to use this as a simple chat reader, go ahead, though if you want to make something more complex like a bot I heavily advise you to go out and look for an API wrapper made by someone else, or even make your own. This script uses a browser to fetch messages from the core browser source rather than the core API so that introduces a few obsticles into the message sending process such as needing to log in each time you launch the script and that you have to focus the browser all of the time in order to send messages, so you technically could send messages but I removed the functions to not cause any confusion. Again, if you want to send messages, find an API wrapper.

- Does this come with premade scripts?
Yes, one. It's a text to speech script that reads chat messages aloud. You can find it in the extras folder.

- Do I need to credit you?
No... Unless you want to.

- I want to read and send messages using the API, what projects do that?
I have linked a working async API wrapper for kick.com at the bottom of this file, check it out if you want.

- Can I install this script as a package using PIP?
No, I cannot be bothered to find a way to make this into a PIP package, you can only use this by downloading the project files and modifying the script.py file.

- Is this a virus?
No, but good that you're being cautious. For your own safety make sure to review this script (and any script you get in the future) to make sure it won't perform malicious actions on your device. Stay safe out there!



IDEAS:

- Chat message TTS
Read chat messages using the pyttsx3 text to speech package. (https://pypi.org/project/pyttsx3/)
   Available in Extras folder!!!

- Chat sound effects
Play sounds when chat uses certain commands, for example !fart

- Chat plays
Allow chat to use your keyboard/mouse by making commands to use them, for example !mouse up, !move left

- Welcome messages
Welcome new people in chat by displaying a file on your stream that says the users name

- Polls
Make chat be able to vote by inputting numbers in chat

and much more! The limit is your imagination... and your python knowledge.



MORE INFO:

So you want to know how this script works in depth? Mayhaps you want to edit the scripts to work how you want it? Sure! Here's me explaining how it works.

 - install.py is a short script which runs "pip install" commands on the two required packages for this script: undetected_chromedriver and bs4 (bs4 is no longer used).
 - update.py is another short script which opens a browser, goes to the github repository for this script, reads the version file and sees if the users version is the same as the one found in the browser. It knows the current version by checking the hidden "version" file in this folder.
 - script.py is where the user is meant to input their code, when executor.py is ran it will read the code in script.py and reader.py and run them.

Now, reader.py, the main meat of this script:
First off it gets the "channel.txt" file to get the users channel. It then appends "https://www.kick.com/" to the start of it and "/chatroom" to the end of it to create the link to that users channel chatroom. It uses undetected_chromedrivers webdriver to open Chrome and gets the source code of the url. Then it just runs an infinite loop that checks for new messages every set amount of seconds. It does this by getting the page source, splits that page source into pieces to understand where are which messages (if you're wondering what the html jamble means, it's just stuff I found that usually occurs before and after messages in the HTML code and I use it to split the text), it compiles the found messages into a list and then checks if any messages haven't been read yet. If one hasn't, the script get's that message, sends it to the message_event function and appends the message to the readenMessages array.

Aaand that's all I think. Please don't judge my choice of names for the variables, I'm really bad at naming variables in my code. DM me on Discord if you need any help with understanding the code!



END OF FILE:

Thanks to DKnightX91 for showing me undetected_chromedriver!
Want to support me? Just a thanks is enough <3
My channel: https://www.twitch.tv/37scorpions

If you're looking for an API wrapper capable of reading AND sending messages you can check out https://github.com/cibere/kick.py, haven't tried it myself but it looks like a good async API wrapper.



Wow, you really read the entire file. Nice.
Have fun now I guess