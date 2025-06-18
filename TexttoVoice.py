import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import random
import wikipedia
import pyjokes
import pyautogui
import os


engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)  
engine.setProperty('rate', 150)  



def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")     
    speak("hey there , i am voice assistant made by Akshra") 
    speak ("tell me what happened ?") 

wishme()


def takeCommand():
    global query
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"User said: {query}\n")

        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            return query
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")
            return query
        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")
        elif "open gpt" in query:
            speak("Opening chatgpt")
            webbrowser.open("https://openai.com/index/chatgpt/")

            return query
        
        
       
            
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            return query  

        elif "volume up" in query:   
            speak("Increasing volume")
            pyautogui.press("volumeup")
            return query

        elif "volume down" in query:
            speak("Decreasing volume")
            pyautogui.press("volumedown")
            return query

        elif "mute" in query:
            speak("Muting volume")
            pyautogui.press("volumemute")
            return query

        elif "unmute" in query:
            speak("Unmuting volume")
            pyautogui.press("volumemute")
            return query

        elif "volume full" in query:
            speak("Setting volume to full")
            pyautogui.press("volumeup", presses=100)
            return query    
        
        elif "brightness full" in query:
            speak("Setting brightness to full")
            pyautogui.press("brightness up", presses=100)
            return query  
        
        elif "brightness low" in query:
            speak("Setting brightness to low")
            pyautogui.press("brightness down", presses=100)
            return query  
        
        elif "Hello" in query:
            speak ("hello maam")
            return query


    except Exception:
        speak("Sorry, I did not understand that. Please say it again.")
        return "None"        






def bolore():
    takeCommand()


bolore()
