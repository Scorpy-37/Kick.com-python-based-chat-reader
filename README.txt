Hi, thanks for using my script for reading Kick.com chat messages uwu

Do note that this is a pretty scuffed way of doing it, though it's the only way I thought of doing it as Kick didn't provide a public API for it, the method I used is to launch a browser window, go to the channel page, read the inspect element window, get the message container section on a channel and then split that container into pieces to compile a list of visible messages and usernames. Then it constantly checks if there are changes in the list of messages, if so it fires the message event function with the latest message. It could possibly miss some messages if two get sent at the exact same time, though it shouldn't happen a lot.

Know that this can only read messages after you launch the script, any messages before will not show up in the channel page chat section, also know that it cannot pick up on emojis and just skips over them.

I just wanted to make a way to read chat messages ASAP as Kick is yet to have a public API for this stuff (like Twitch does). Reading chat messages can be neat for things like TTS, chat commands, sound effects so if you type !fart it plays le fart sound, chat polls and etc.
Oh yeah, if it wasn't clear: no, you cannot send chat messages using this.



   HOW TO RUN:

(I expect you to have atleast some Python programming knowledge)

Before running the script make sure you have Microsoft Edge installed (the browser this script uses) and that channel.txt has your channel username in it.

To make the script do things, open main.py with notepad++ and add any code that you want in the message_event function.

Once done, save the file and run the main.py script.

If you run the script and the browser shows up saying "Page not found" or something along those lines, it probably means they detected you as a bot, it always fixes it for me if I just close the script, wait a few minutes and then launch it again. If you're having issues for a solid while please do contact me on Discord (Scorp#1348)

If everything is working you should see chat messages show up in the console, then you can minimize the windows and run them in the background.



IF YOU ENCOUNTER ANY BUGS, ERRORS OR NEED HELP WITH SOMETHING, PLEASE DO DM ME ON DISCORD AT Scorp#1348
If you use this for your streams it'd be cool if you'd credit me somewhere... or not... thanks for using this either way.
