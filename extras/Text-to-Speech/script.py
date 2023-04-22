from os import system as installer
installer("pip install pyttsx3")
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)
def Speak(text):
    engine.setProperty(
        'voice', 
        engine.getProperty('voices')[
            int(open("voice_index.txt").read())
        ].id
    )
    engine.say(text)
    engine.runAndWait()

def ready_event(channel, link):
    print("Listening to "+channel+" at "+link)
    Speak("Listening to "+channel)

def message_event(msg):
    author = msg[0]
    content = msg[1]
    id = msg[2]
    
    print(author+": "+content)
    Speak(content)