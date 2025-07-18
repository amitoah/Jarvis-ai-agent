import os
import re
import webbrowser
import sqlite3
from engine.db import cursor, conn
# Importing playsound for playing audio files
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
    query = query.lower()

    if query!="":
        speak("Opening "+query)
        os.system("start " + query)
    else:
        speak("not found")
    
    
    # if query == "youtube":
    #     speak("Opening YouTube")
    #     os.system("start https://www.youtube.com")
    # elif query != "":
    #     speak("Opening " + query)
    #     os.system("start " + query)
    # else:
    #     speak("not found")
    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_commznd WHERE nmae IN (?)', (app_name))
            results = cursor.fetchall()
            
            if len(results) !=0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name, ))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('strat '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
    


def playYoutube(query):
    serch_term = extract_yt_term(query)
    speak("playing " + str(serch_term) + " on youtube")
    kit.playonyt(serch_term)

def extract_yt_term(command):
    #Define a regular expression to pattern to capture the song name 
    pattern = r'play\s? (.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command 
    match = re.search(pattern, command, re.IGNORECASE)
    #if a match is found, return the extracted song name; otherwise, return None 
    return match.group(1) if match else None
