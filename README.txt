Hello! Thank you for using my script for reading Kick.com chat messages uwu

Need help with anything? Contact me on Discord at Scorp#1348!
Just please DM me saying what you want, don't just go "hi" and wait for my response.



SETUP:

1. Run "install.py" to install required packages
2. Open the channel.txt file and enter your channels username
3. Open script.py with notepad, notepad++, sublime text or whatever you want
4. Edit the code to do what you want it to do
5. Save it and run executor.py
6. Done!

Make sure to not minimize the browser and just keep it running in the background, minimizing it could cause it to become inactive and stop picking up on new messages.



NOTES:

- Make sure to run update.py every once in a while to check for new updates to the script
- You don't need to be streaming for this script to work
- Make sure to pause the stream in the browser window if you're streaming to not slow down your pc and wifi
- If the browser comes up saying "Oops, Something went wrong", check the console for help
- IMPORTANT!!! If the browser comes up without the emoji picker above the chat message input box, the browser won't pick up on messages. I have no idea why it is like that, but the browser randomly decides to make the chat not work. Probably Kicks way to prevent people from using the website on a browser handled by a script (most likely to prevent botting). Either way, if you encounter this, restart the script. Try restarting it until the emoji picker and chat messages start working, everything should be working fine then.



QNA:

- How does it do it?
It launches a browser (Edge), goes to your channel page on Kick.com and reads the page source to view the message container.

- Is this allowed?
I... have no idea. Other Kick.com bots like BotRix Beta use a browser extension to view things like alerts and such, I don't think this is that far from that.

- Why should I use this?
Because it's probably one of the few public scripts for reading chat messages on Kick.com, considering they didn't make a public API for it themselves like Twitch did. Also this supports python, and who doesn't love python.

- Is it reliable?
Kind of, since I stream myself I will probably realize when and if the script breaks or becomes outdated. Make sure to check for updates in case you have any issues. It checks for common things coming before and after messages/usernames to cut them out of the page source code meaning if the websites style, html code or things like that change this script will most likely break.

- Can I send chat messages with this?
No.

- Does this come with premade functions?
No... Well, a few, you can find them in the Extras folder, but you should code your own.

- Do I need to credit you?
No. It would be nice though if you did!



IDEAS:

- Chat message TTS
Read chat messages using the pyttsx3 text to speech package. (https://pypi.org/project/pyttsx3/)
Now available in Extras folder!!!

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

install.py is a short script which runs "pip install" commands on the two required packages for this script: selenium and bs4 (beautiful soup).
update.py is another short script which opens a browser, goes to the github repository for this script, reads the version file and sees if the users version is the same as the one found in the browser. It knows the current version by checking the hidden "version" file in this folder.
The script.py is where the user is meant to input their code, when executor.py is ran it will read the code in script.py and reader.py and run them.

Now, reader.py, the main meat of this project/script:

First off it gets the "channel.txt" file to get the users channel. It then appends "https://www.kick.com/" to the start of it to create the link to that users channel. It uses seleniums webdriver to open Edge and gets the source code of the url. Then it just runs an infinite loop that checks for new messages every 0.1 seconds. It does this by getting the page source, using bs4 to find the "messagesContainer" div in the source code (which contains the messages), splits that container into pieces to understand where are which messages (if you're wondering what the html jamble means, it's just stuff I found that usually occurs before and after messages in the HTML code and I use it to split the text), it compiles the found messages into a list and then checks if any messages haven't been read yet. If one hasn't, the script get's that message, sends it to the message_event function and appends the message to the readenMessages array.

Aaand that's all I think. Please don't judge my choice of names for the variables, I'm really bad at naming variables in my code.
If there's any confusion and you want to change something, hit me up on Discord at Scorp#1348 and I'll be glad to help!





Wow, you really read the entire file. Nice.
Have fun now I guess



My channel: kick.com/37Scorpions
(I count saying thanks as credit too)