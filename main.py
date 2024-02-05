import speech_recognition as sr
import pyttsx3
import pyjokes
import requests
from datetime import *
import winsound
import holidays
import webbrowser
from bs4 import BeautifulSoup

# basic commands, integrate weather api, datetime, send email using smtp port(?),open website on command
# jokes,

# text to speech library
# object creation
engine = pyttsx3.init('sapi5')
# init function to get an engine instance for the speech synthesis
# sapi5 is the pyttsx3.drivers module name for windows to load and use
voices = engine.getProperty('voices')
# getting details of current voice
engine.setProperty('voice', voices[1].id)
# 0 for male voice and 1 for female voice
# RATE
rate = engine.getProperty('rate')
# getting details of the current speaking rate
print(rate)
engine.setProperty('rate', 200)
volume = engine.getProperty('volume')
print(volume)

name = "Jarvis"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def list_of_holidays():
    ind_holidays = holidays.country_holidays(country="India", years=date.today().year)

    for holiday in ind_holidays.items():
        print(holiday)

# engine.say("Good Morning")
# engine.runAndWait()
# run and wait method, it processes the voice commands.
# engine.stop()

# recognizer object
# speech = sr.Recognizer()


# jokes object
def jokes():
    joke = pyjokes.get_joke('en', 'all')
    speak(joke)
    print(joke)

# use the recognizer object to recognize speech from a microphone
# with sr.Microphone() as source:
#     audio = speech.listen(source)


def wishme():
    hour = int(datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good evening Sir")
    speak("I am your Assistant")
    speak(name)


# wishme()
# jokes()


def user_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


# def user_input():
#     speech = sr.Recognizer()
#     with sr.Microphone() as source:
#         speech.pause_threshold = 1
#         audio = speech.listen(source)
#
#     try:
#         commands = speech.recognize_google_cloud(audio, language='en-in')
#         print(commands)
#
#     except Exception as e:
#         print(e)
#         print("Unable to Recognize your voice")
#         return "None"
#
#     return commands


while True:
    query = user_input().lower()

    if "hello" in query:
        speak("hello ")

    elif "Jarvis" in query:
        wishme()

    elif "what is your name" in query or "what's your name" in query:
        speak("My Friends call me")
        speak(name)
        print("My friends call me", name)

    elif "How are you" in query:
        speak("I'm fine")

    elif "I love you" in query:
        speak("I am rather flabbergasted . ")

    elif "list of holidays " in query:
        speak("Here is the List of Holidays:")
        list_of_holidays()

    # elif "weather" in query:
    #     api_key = "Api key"
    #     base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    #     speak(" City name ")
    #     print("City name : ")
    #     city_name = user_input()
    #     complete_url = base_url + "api_id =" + api_key + "&q =" + city_name
    #     response = requests.get(complete_url)
    #     x = response.json()

    elif "temperature" in query:
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current{search} is {temp}")

    elif "weather" in query:
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current{search} is {temp}")

    elif "Tell me a Joke " in query:
        jokes()

    elif "set an alarm" in query:
        speak("what time?")
        time = user_input()
        now = datetime.now()
        delta = time-now
        sec = delta.total_seconds()
        time.sleep(sec)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com/")

    elif "open google" in query:
        webbrowser.open("https://www.google.com/")


