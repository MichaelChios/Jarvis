import speech_recognition as sr
import aspose.words as aw
import webbrowser
import subprocess
import pyautogui
import keyboard
import pywhatkit
import clipboard
import requests
import datetime
import platform
import random
import smtplib
import pyttsx3
import ctypes
import psutil
import urllib
import os
import time as tt
from email.message import EmailMessage
from secret import senderemail, password
from face_training import trainProgram
from urllib.request import urlopen
from datetime import datetime
from faceRecognition import *
from datetime import date
from requests import get
from JarvisTry import *

def wordDocumentButton():
    type = "docx"
    speak("How should I name the document?")
    name = getFileName()
        
    speak("What should I write in it?")
    text = getText()

    speak("Creating " + name + ".docx...")
    createFile(name, type, text)
    speak("Word document is ready.")

def pdfFileButton():
    type = "pdf"
    speak("How should I name the document?")
    name = getFileName()
        
    speak("What should I write in it?")
    text = getText()

    speak("Creating " + name + ".pdf...")
    createFile(name, type, text)
    speak("The pdf file is ready.")

def txtFileButton():
    type = "txt"
    speak("How should I name the document?")
    name = getFileName()
        
    speak("What should I write in it?")
    text = getText()

    speak("Creating " + name + ".txt...")
    createFile(name, type, text)
    speak("The text file is ready.")

def googleSearchButton():
    speak("What information do you need?")
    sr = speechToText()
    while (sr == "None"):
        speak("Could you say that again, please?")
        sr = speechToText()

    speak("Opening Google Search...")
    speak("Searching for " +sr)
    googleSearch(sr)
    speak("Here's the information you need")

def YouTubeButton():
    speak2("What do you want to watch on YouTube?")
    topic = speechToText()
    speak("Playing " + topic + " on YouTube...")
    pywhatkit.playonyt(topic)













                            
