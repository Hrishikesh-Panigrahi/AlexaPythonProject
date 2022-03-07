"""from flask import Flask,render_template,redirect,request
import warnings
warnings.filterwarnings('ignore')"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import os.path
import requests, json 
import os

listener = sr.Recognizer()
# app = Flask("__name__")

def create_file(file_name, write ):
    if os.path.isfile(file_name):
        with open (file_name, 'w') as f:
            f.write(write)
    else:
        with open (file_name, 'w+') as f:
            f.write(write)

def replace (variable, command):
    command = command.replace(variable, "")
    return command

def nandini_talks(text):
    """ To change to male to female or vice versa --- use getproperty and set it to voices and then using setperoperty we can change it's index"""
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
                command = replace('nandini',command)
                print(command)

    except:
        pass
    return command

def run_nandini():
    command = user_inputs()                   # taking inputs from user

    if "play" in command:
        command = replace("play",command)
        pywhatkit.playonyt(command)
        nandini_talks("Playing " + command)    #engine will speak

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        nandini_talks('the current time now ' + time)  # engine will speak

    elif "who is" in command:
        inp = replace("who is",command)
        info = wikipedia.summary(inp, 1)
        print(info)
        nandini_talks(info)

    elif "joke" in command:
        laugh = pyjokes.get_joke()
        print(laugh)
        nandini_talks(laugh)

    elif "send whatsapp message" in command:
        command = replace("send whatsapp message",command)
        command = replace("to",command)
        command = "+91" + command  
        nandini_talks("Will send message to" + command)
        print(command)
        nandini_talks("What message you want to send?")
        message = user_inputs()
        pywhatkit.sendwhatmsg(command, message , 15, 35)
     
    elif "weather" in command:
        print("kuch bhi")

    elif "stop" in command:
        nandini_talks("System shutting down.")
        sys.exit()

    elif "create" in command:
        file_name = replace("create",command)
        nandini_talks("Creating" + file_name)
        nandini_talks("What you want to write?")
        write = user_inputs()
        create_file(file_name, write)

    elif "pallindrome" in command or "palindrome" in command:
        name = replace("a", command)
        name = replace("palindrome", command)
        name = replace("is", command)
        temp = name.find(name[::-1])
        if temp:
            nandini_talks(name + "is a palindrome")
            print(name)

    else:
        nandini_talks("again please")

run_nandini()

"""
@app.route('/')
def hello():
    return render_template("main.html")

@app.route("/home")
def home():
    return redirect('/')

@app.route('/',methods=['POST', 'GET'])
def submit():
    while True:
        run_nandini()
    return render_template("main.html")
        

if __name__ =="__main__":
    app.run(debug=True)"""