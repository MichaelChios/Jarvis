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
from urllib.request import urlopen
from datetime import datetime
from faceRecognition import recognizeFaces
from datetime import date
from requests import get
from tensorflow.keras.models import load_model # type: ignore
from dotenv import load_dotenv


###########################################################################################################
#Speech to text and text to speech functions
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#For Jarvis to speak with the default voice
def speak(audio):
    print("Jarvis:", audio)
    engine.say(audio)
    engine.runAndWait()

#Returns a list with responses for Jarvis when he didn't understand what you said
def responses(file):
    f = open(file + '.txt', 'r')
    s = f.readlines()
    f.close()
    return s

#Speaking to Jarvis
def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        speech = r.recognize_google(audio, language = 'eng-in')
        print(f"Me: {speech}")
    except Exception as e:
        return "None"
    return speech

###########################################################################################################
#Says hi
def sayHi(speech):
    if ("Jarvis are you up" in speech):
        speak("For you sir, always.")

    elif ("hello" in speech):
        speak("Hello sir. How can I be of service?")

def greeting():
    hour = datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good morning, sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon, sir!")
    elif (hour >= 18 and hour < 24):
        speak("Good evening, sir!")
    else:
        speak("Good night, sir!")

###########################################################################################################
#Functions about file management
#Creates a file
def createFile(name, type, text):
    f = aw.Document()
    builder = aw.DocumentBuilder(f)
    font = builder.font
    font.size = 16
    font.bold = True
    font.name = "Arial"
    paragraphFormat = builder.paragraph_format
    paragraphFormat.first_line_indent = 8
    paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY
    paragraphFormat.keep_together = True
    builder.writeln("{}".format(text))
    f.save("{}.{}".format(name, type))

#Input for file name
def getFileName():
    s = speechToText()
    while (s == "None"):
        speak("Please give me a name for the document.")
        s = speechToText()
    if ("type" in s or "keyboard" in s):
        speak("Type the name of the file below: ")
        name = input("Name: ")
    else:
        name = s
    return name

#Input for text
def getText():
    s = speechToText()
    while (s == "None"):
        speak("Please tell me what to write in the file.")
        s = speechToText()
    if ("type" in s or "keyboard" in s):
        speak("Write the text below: ")
        text = input("Text: ")
    else:
        text = s
    return text

#Creates a word document
def wordDocument(speech):
    if ("word" in speech or "Word" in speech):
        type = "docx"
        speak("How should I name the document?")
        name = getFileName()
        
        speak("What should I write in it?")
        text = getText()

        speak("Creating " + name + ".docx...")
        createFile(name, type, text)
        speak("Word document is ready.")
        if ("open" in speech):
            speak("Opening " + name + ".docx...")
            openFiles(name, type)
            return True                                                 # For the openFiles2 function
        else:
            return False

#Creates a pdf file
def pdfFile(speech):
    if ("pdf" in speech or "PDF" in speech):
        type = "pdf"
        speak("How should I name the file?")
        name = getFileName()

        speak("What should I write in it?")
        text = getText()

        speak("Creating " + name + ".pdf...")
        createFile(name, type, text)
        speak("The pdf file is ready.")
        if ("open" in speech):
            speak("Opening " + name + ".pdf...")
            openFiles(name, type)
            return True                                                 # For the openFiles2 function
        else:
            return False

#Creates a txt file
def txtFile(speech):
    if ("txt" in speech or "text" in speech or "note" in speech):
        type = "txt"
        speak("How should I name the file?")
        name = getFileName()

        speak("What should I write in it?")
        text = getText()

        speak("Creating " + name + ".txt...")
        createFile(name, type, text)
        speak("The text file is ready.")
        if ("open" in speech):
            speak("Opening " + name + ".txt...")
            openFiles(name, type)
            return True                                                 # For the openFiles2 function
        else:
            return False

#Executes the command "Create a document"
def doCreateFile(speech):
    if ("file" in speech or "document" in speech):
        x = wordDocument(speech)
        if (x == None):
            x = pdfFile(speech)
        if (x == None):
            x = txtFile(speech)
        return x

#Opens a file that was just created in the same directory with the code
def openFiles(name, type):
    subprocess.Popen(["{}.{}".format(name, type)], shell=True)

#Returns the name of the file I want to open
def getFile():
    speak("Give me the name of the file below: ")
    inp = input()
    counter = 0
    list = []
    thisdir = os.getcwd()
    speak("Searching for "+inp+" in the database.")
    speak("This may take a couple of minutes. Please wait.")
    for r, d, f in os.walk("C:\\"):
        for file in f:
            filepath = os.path.join(r, "")
            if (inp == file):
                counter += 1
                break
        if (counter !=0):
            break
    if (counter == 0):
        return False
    else:
        list.append(filepath)
        list.append(inp)
        return list

#Opens a file from any directory
def openFiles2():
    f = getFile()
    while (f == False):
        speak("File not found")
        f = getFile()

    wd = os.getcwd()
    os.chdir(f[0])
    speak("Opening "+f[1]+"...")
    subprocess.Popen([f[1]], shell=True)
    os.chdir(wd)

def doOpenFiles(speech):
    if ("open" in speech and "file" in speech):
        openFiles2()

###########################################################################################################
#Google search functions
#Does a Google search
def googleSearch(search):
    webbrowser.open("https://www.google.com/search?q=" + search)

#Executes the command "Search for something"
def doGoogleSearch(speech):
    if ("search" in speech):
        for i in range (len(speech)+1):
            for j in range(i, len(speech)+1):
                if (speech[i:j] == "search"):
                    if (speech.replace(speech[0:j+1], "") == "" or speech.replace(speech[0:j+1], "") == " "):
                        speak("What information do you need?")
                        sr = speechToText()
                        while (sr == "None"):
                            speak("Could you say that again, please?")
                            sr = speechToText()
                    else:
                        sr = speech.replace(speech[0:j+1], "")
                        break

        speak("Opening Google Search...")
        speak("Searching for " +sr)
        googleSearch(sr)
        speak("Here's the information you need")

###########################################################################################################
#Plays a video on YouTube
def YouTube(speech):
    if ("YouTube" in speech or "youtube" in speech or "you tube" in speech or "You Tube" in speech):
        speak("What do you want to watch on YouTube?")
        topic = speechToText()
        speak("Playing " + topic + " on YouTube...")
        pywhatkit.playonyt(topic)

###########################################################################################################
#Send emails
def sendEmail(receiver, subject, content):
    load_dotenv()
    senderemail = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, password)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def getSubject():
    subject = speechToText()
    while(subject == "None"):
        speak("Repeat the subject or ask me to give you access from keyboard.")
        subject = speechToText()
    if ("keyboard" in subject):
        print("Subject: ")
        subject = input()
    return subject

def getMessage():
    message = speechToText()
    while(message == "None"):
        speak("Repeat the message or ask me to give you access from keyboard.")
        message = speechToText()
    if ("keyboard" in message):
        print("Message: ")
        message = input()
    return message

def doSendEmail(speech):
    if ("mail" in speech or "email" in speech):
        load_dotenv()
        speak("To whom should I send the email?")
        receiver = os.getenv('RECEIVER')
        
        speak("What is the subject?")
        subject = getSubject()

        speak("What is the message?")
        message = getMessage()        

        sendEmail(receiver, subject, message)
        speak("Email sent.")

###########################################################################################################
#Internet connection functions
#Detects internet connection
def internetConnection():
    try:
        urlopen('https://www.google.gr/?hl=el', timeout = 1)
        return True
    except urllib.error.URLError as e:
        return False

#Connects to my wifi
def connectToWiFi():
    os.system('cmd /c "netsh wlan show networks" ')
    name_of_router = "WindWiFi_A8E415" # Replace with your router's name
    os.system(f'''cmd /c "netsh wlan connect name={name_of_router}" ''')

###########################################################################################################
#Location and weather information
#Finds my IP Address
def findIPAddress():
    return get("https://api.ipify.org").text

#Finds my location from my IP Address
def findLocation():
    loc = []
    response = requests.post("http://ip-api.com/batch", json = [
    {"query": findIPAddress()}
    ]).json()
    for ip_info in response:
        loc.append(ip_info["regionName"])
        loc.append(ip_info["city"])
    return loc

#Executes the command "Find my IP Address"
def doFindIPAddress(speech):
    if (" ip " in speech or " IP " in speech):
        speak("Your IP Address is: " + findIPAddress())

#Executes the command "Find my location"
def doFindLocation(speech):
    if ("location" in speech):
        speak("You are in " + findLocation()[0] + ", " + findLocation()[1])

#Finds weather information about my area
def weather(loc):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "557d9e4ba7a63109e7c54942c06972c3"
    url = base_url + "appid=" + api_key + "&q=" + loc + "&units=metric"
    res = requests.get(url)
    data = res.json()
    temp = round(data['main']['temp'])
    feel = round(data['main']['feels_like'])
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    w = f"Temperature: {temp}°C\nFeels like: {feel}°C\nDescription: {description}\nHumidity: {humidity} %\nPressure: {pressure} hPa\nWind speed: {wind} m/s."
    return w

#Shows weather information
def showWeather(speech):
    if ("weather" in speech):
        if ("my area" in speech or "my location" in speech or "my region" in speech):
            location = findLocation()[1]
        else:
            speak("For which area do you want weather information?")
            location = speechToText()
            
        speak("Here's the weather information for " + location)
        w = weather(location)
        print(w)

###########################################################################################################
#Date and time functions
#Tells today's date
def currentDate():
    today = date.today()
    return today.strftime("%B %d %Y")

#Tells the time
def currentTime():
    time = datetime.now()
    return time.strftime("%H:%M:%S")

#Executes the command "Tell me today's date"
def tellDate(speech):
    if ("date" in speech):
        speak("Today's date is "+ currentDate())

#Executes the command "What time is it?"
def tellTime(speech):
    if ("time" in speech):
        speak("The time is "+ currentTime())

###########################################################################################################
#Executes the command "Lock the screen"
def lockScreen(speech):
    if ("sleep" in speech or "lock the screen" in speech or "lock my screen" in speech):
        ctypes.windll.user32.LockWorkStation()

###########################################################################################################
#Takes a screenshot
def screenshot():
    name_img = 0
    name_img = (int)(lastImage()) +1
    saveImageName((str)(name_img))
    name_img = r"C:\Users\User\Desktop\ScreenshotJarvis\\screenshot_%s.png" % name_img # Or any path you want
    img = pyautogui.screenshot(name_img)
    
def takeScreenshot(speech):
    if ("screenshot" in speech):
        screenshot()
        speak("Screenshot taken")

####Useful functions for screenshot()####
#Saves the screenshot's name in txt
def saveImageName(image):
    f = open("txtFiles/screenshotnames.txt", "w")
    f.write(image)
    f.write("\n")
    f.close()

#Returns the name of the last screenshot taken
def lastImage():
    last_img = ""
    with open("txtFiles/screenshotnames.txt", "r") as file:
        img = file.readlines()[-1]
        last_img = img
    return last_img

###########################################################################################################
#Reads selected text
def readSelectedText():
    text = clipboard.paste()
    speak(text)

def doReadSelectedText(speech):
    if ("read" in speech or "selected text" in speech):
        readSelectedText()
    
###########################################################################################################
#System information functions
#Transforms data sizes
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

#System Information
def systemInfo():
    print("="*30, "System Information", "="*30)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

#Boot Time
def bootTime():
    print("\n" + "="*30, "Boot Time", "="*30)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

#CPU Information
def cpuInfo():
    print("\n" + "="*30, "CPU Info", "="*30)
    #Number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    #CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    #CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

#Memory Information
def memoryInfo():
    print("\n" + "="*30, "Memory Information", "="*30)
    #Memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    #Swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

#Disk Information
def diskInfo():
    print("\n" + "="*30, "Disk Information", "="*30)
    print("Partitions and Usage:")
    #All disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"Mountpoint: {partition.mountpoint}")
        print(f"File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"Total Size: {get_size(partition_usage.total)}")
        print(f"Used: {get_size(partition_usage.used)}")
        print(f"Free: {get_size(partition_usage.free)}")
        print(f"Percentage: {partition_usage.percent}%")
    #IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

#Network Information
def networkInfo():
    print("\n" + "="*30, "Network Information", "="*30)
    #All network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    #IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

#Battery Information
def batteryTime(sec):
    mm, ss = divmod(sec, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def batteryInfo():
    print("\n" + "="*30, "Battery Information", "="*30)
    print("Battery charge: {}%". format(psutil.sensors_battery().percent))
    if(psutil.sensors_battery().secsleft == psutil.POWER_TIME_UNLIMITED):
        print("The battery time is unlimited.")
    else:
        print("Time left: ", batteryTime(psutil.sensors_battery().secsleft))
    print("Plugged in:", psutil.sensors_battery().power_plugged, "\n")
    
def allInfo(speech):
    if ("system information" in speech):
        speak("Getting system information...")
        speak("Here's everything about your computer.")
        systemInfo()
        bootTime()
        cpuInfo()
        memoryInfo()
        diskInfo()
        networkInfo()
        batteryInfo()

###########################################################################################################
#Initializes Jarvis
def initializeJarvis():
    if (internetConnection()):
        speak("Internet connection detected. All systems have been activated.")
        speak("Hold still and look at the camera for face ID authentication.")
        if(faceID()==False):
            speak("Authentication failed. Terminating...")
            return False
        else:
            speak("Authentication successful. Welcome back sir.")
            return True
            
    else:
        speak("No internet connection. Trying to reconnect...")
        connectToWiFi()
        speak("You are now connected to the internet.")
        speak("Hold still and look at the camera for face ID authentication.")
        if(faceID()==False):
            speak("Authentication failed. Terminating...")
            return False
        else:
            speak("Authentication successful. Welcome back sir.")
            return True

###########################################################################################################
#Face Recognition Access
def faceID():
    if(recognizeFaces()==True):
        return True
    else:
        return False

###########################################################################################################
# What can Jarvis do
def help(speech):
    if ("help" in speech or "what can you do" in speech):
        s = responses('txtFiles/whatIcando')
        speak(s[0])
        for i in range(1, len(s)):
            print(s[i])
        
###########################################################################################################
#Jarvis waits for next command
def  doNothing(speech):
    if (speech != "None" or "wait" in speech or "Wait" in speech or "pause" in speech or "Pause" in speech):
        speak("Waiting for your next command. When you need me, press 'Space' and tell me what you want.")
        keyboard.wait('space')

###########################################################################################################
#Terminates Jarvis
def Terminate(speech):
    if ("terminate" in speech):
        speak("Terminating...")
        return True

###########################################################################################################
#Involves all Jarvis' functions
def jarvisFunctions():
    greeting()
    while True:
        x = False
        speak(random.choice(responses('txtFiles/responses2')).strip())
        s = speechToText()
        if (s == "None"):
            speak(random.choice(responses('txtFiles/responses1')).strip())
        sayHi(s)
        if (Terminate(s) == True):
            break
        x = doCreateFile(s)
        if (x == None):
            x = False
        doGoogleSearch(s)
        tellDate(s)
        tellTime(s)
        doFindIPAddress(s)
        doFindLocation(s)
        lockScreen(s)
        showWeather(s)
        doSendEmail(s)
        allInfo(s)
        takeScreenshot(s)
        doReadSelectedText(s)
        YouTube(s)
        help(s)
        if (x == False):
            doOpenFiles(s)
        doNothing(s)

def Jarvis():
    if(initializeJarvis()==False):
        return
    else:
        jarvisFunctions()

def main():
    Jarvis()

if __name__ == '__main__':
    main()
