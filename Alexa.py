'''from flask import Flask,render_template,redirect,request
import warnings
warnings.filterwarnings('ignore')'''

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()


""" To change to male to female or vice versa --- use getproperty and set it to voices and then using setperoperty we can change it's index"""


def nandini_talks(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def user_inputs():       #taking the inputs and storing it in command
    try:
        with sr.Microphone() as source:
            print("start")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "nandini" in command:
                command = command.replace("nandini" , "")
                print(command)

    except:
        pass
    return command

def run_nandini():
    command = user_inputs()                   # taking inputs from user

    if "play" in command:
        command = command.replace("play", "")
        pywhatkit.playonyt(command)
        nandini_talks("Playing " + command)    #engine will speak

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        nandini_talks('the current time now ' + time)  # engine will speak

    elif "who is" in command:
        inp = command.replace("who is", "")
        info = wikipedia.summary(inp, 1)
        print(info)
        nandini_talks(info)

    elif "joke" in command:
        laugh = pyjokes.get_joke()
        print(laugh)
        nandini_talks(laugh)
     

    elif "weather" in command:
        print("kuch bhi")

    elif "stop" in command:
        nandini_talks("System shutting down.")
        sys.exit()

    elif "open" in command:
        print("daalna hai ismai")

    else:
        nandini_talks("again please")


run_nandini()