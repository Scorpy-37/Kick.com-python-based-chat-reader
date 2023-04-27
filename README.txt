Hello! Thank you for using my script for reading KickStreaming chat messages uwu

Need help with anything? Contact me on Discord at Scorp#1348!
Just please DM me saying what you want, don't just go "hi" and wait for my response.

If you don't like reading, just quickly skim over this file and read anything that catches your eye. It is quite important to read this to understand how to use it.



SETUP:

1: Run "install.py" to install required packages
2: Open the channel.txt file and enter your channels username
3: Open script.py with notepad, notepad++, sublime text or whatever you want
4: Edit the code to do what you want it to do
5: Save it and run executor.py
6: Done!



NOTES:

- Make sure to run update.py every once in a while to check for new updates to the script
- You don't need to be streaming for this script to work.
- Make sure to pause the stream in the browser window if you're streaming to not slow down your pc and wifi
- If the browser comes up saying "Oops, Something went wrong", make sure you entered the right channel name
- Since update v1.6 you don't need to keep the browser not minimized and the 404 error only comes up when you enter the wrong channel name



Q&A:

- How does it work?
It launches a browser (Chrome), goes to your channel page on Kick.com and reads the page source to view the message container.

- Is this allowed?
I... have no idea. Other KickStreaming bots like BotRix Beta use a browser extension to view things like alerts and such, I don't think this is that far from that.

- Why should I use this?
Because it's probably one of the few public scripts for reading chat messages on Kick.com, considering they didn't make a public API for it themselves like Twitch did. Also this supports python, and who doesn't love python.

- Is it reliable?
Since v1.6 the script is way more reliable never getting detected as a fake browser. In terms of being up to date to the website, as I stream myself I will notice if the script breaks due to a website structure update and I will try to push a fix as soon as possible. If you noticed the script doesn't work and you believe it's the scripts fault, you can always contact me on Discord.

- Can I send chat messages with this?
No.

- Does this come with premade functions?
Kind of, yes. You can find some free scripts in the extras folder.

- Do I need to credit you?
No... Unless you want to.



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

install.py is a short script which runs "pip install" commands on the two required packages for this script: undetected_chromedriver and bs4 (beautiful soup).
update.py is another short script which opens a browser, goes to the github repository for this script, reads the version file and sees if the users version is the same as the one found in the browser. It knows the current version by checking the hidden "version" file in this folder.
The script.py is where the user is meant to input their code, when executor.py is ran it will read the code in script.py and reader.py and run them.

Now, reader.py, the main meat of this project/script:
First off it gets the "channel.txt" file to get the users channel. It then appends "https://www.kick.com/" to the start of it to create the link to that users channel. It uses undetected_chromedriver's webdriver to open Chrome and gets the source code of the url. Then it just runs an infinite loop that checks for new messages every set amount of seconds. It does this by getting the page source, using bs4 to find the chat div in the source code (which contains the messages), splits that container into pieces to understand where are which messages (if you're wondering what the html jamble means, it's just stuff I found that usually occurs before and after messages in the HTML code and I use it to split the text), it compiles the found messages into a list and then checks if any messages haven't been read yet. If one hasn't, the script get's that message, sends it to the message_event function and appends the message to the readenMessages array.

Aaand that's all I think. Please don't judge my choice of names for the variables, I'm really bad at naming variables in my code. DM me on Discord if you need any help with understanding the code!



My channel: kick.com/37Scorpions
Thanks to DKnightX91 for showing me undetected_chromedriver!
Want to support me? Just a thanks is enough <3



Wow, you really read the entire file. Nice.
Have fun now I guess