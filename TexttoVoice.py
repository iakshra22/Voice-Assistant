import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import random
import wikipedia
import pyjokes 
import pyautogui
import os
 
# Initialize TTS engine
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 150)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish user according to time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hey there! I’m your voice assistant created by Akshra.")
    speak("So, what can I help you with today?")

wishme()

# Function to take user's voice input
def takeCommand():
    global query
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in').lower()
        print(f"User said: {query}\n")

        if "open google" in query:
            speak("Opening Google now.")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in query:
            speak("Opening YouTube for you.")
            webbrowser.open("https://www.youtube.com")

        elif "open instagram" in query:
            speak("Taking you to Instagram.")
            webbrowser.open("https://www.instagram.com")

        elif "open gpt" in query:
            speak("Launching ChatGPT.")
            webbrowser.open("https://openai.com/index/chatgpt/")

        elif "wikipedia" in query:
            speak("Let me search that on Wikipedia.")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif "volume up" in query:
            speak("Increasing the volume.")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            speak("Decreasing the volume.")
            pyautogui.press("volumedown")

        elif "mute" in query:
            speak("Muting the volume.")
            pyautogui.press("volumemute")

        elif "unmute" in query:
            speak("Unmuting the volume.")
            pyautogui.press("volumemute")

        elif "volume full" in query:
            speak("Maximizing the volume.")
            pyautogui.press("volumeup", presses=100)

        elif "brightness full" in query:
            speak("Turning brightness to full.")
            pyautogui.press("brightness up", presses=100)

        elif "brightness low" in query:
            speak("Dimming the screen.")
            pyautogui.press("brightness down", presses=100)

        elif "hello" in query:
            responses = [
                "Hello ma'am, how can I assist you?",
                "Hi! I'm here for you.",
                "Hey! What would you like me to do?",
                "Hello again, ready when you are!",
                "Nice to hear you!"
            ]
            speak(random.choice(responses))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak("Here's a light joke for you.")
            speak(joke)

        elif "what time is it" in query or "current time" in query:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

    except Exception:
        speak("I’m still here... just say that again slowly.")
        return "None"

# Run the assistant once
def bolore():
    takeCommand()

bolore()
