# imports
from ast import main
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import csv

# #variables
# for voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# for time
hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)

# #functions
# say fun
def say(audio):
    engine.say(audio)
    engine.runAndWait()

#wishme fun   
def wishMe():
    if hour >= 0 and hour < 12:
        say("Good Morning")
        
    elif hour >= 12 and hour < 18:
        say("Good Afternoon")
        
    else:
        say("Good evening")
        
    say("I am Jarvis. How can I assist you today?")
    
#function for taking commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenting...")
        r.pause_threshold=1
        r.energy_threshold=200
        audio = r.listen(source)
        
    try:
       print("Recognizing...")
       query = r.recognize_google(audio, language="en-us")
       print(f"User Said: {query}")
       
    except sr.UnknownValueError:
        print("Sorry, I didn't get that Please say that again.")
        return "None"
    except sr.RequestError as e:
        print(f"Sorry, an error occurred; {e}")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    #main Loop
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            say("Searching Wikipedia")
            print("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            print(results)
            say(results)
            
        elif 'play music' in query:
            music_dir = "C:\\Users\\Administrator\\Desktop\\Favorite"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'quit' in query:
            break
        
        elif 'open github' in query:
            webbrowser.open("https://www.github.com/dashboard")
            
        elif 'open stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com/dashboard")
            
