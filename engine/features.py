import os
from playsound import playsound 
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
#playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()


    if query!="":
        speak("Opening "+query)
        os.system("start "+query)
    else:
        speak("not found")

def playYoutube(query):
    serch_term = extract_yt_term(query)
    speak("playing "+serch_term+" on youtube")
    kit.playonyt(serch_term)

def extract_yt_term(command):
    #Define a regular expression to pattern to capture the song name 
    pattern = r'play\s? (.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command 
    match = re.search(pattern, command, re.IGNORECASE)
    #if a match is found, return the extracted song name; otherwise, return None 
    return match.group(1) if match else None