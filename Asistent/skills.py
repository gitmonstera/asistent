import webbrowser
import sys
import subprocess
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 180)


def speaker(text):
    engine.say(text)
    engine.runAndWait()

def weather():
    print('weather')


def game():
    print('game')


def telegram():
    webbrowser.open('', new=2)


def browsergoogle():
    webbrowser.open('https://www.google.com', new=2)


def offBot():
    sys.exit()


def passive():
    pass
