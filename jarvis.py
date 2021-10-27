import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os
import sys
import time
import pyautogui
import pywhatkit as pwt
import pyjokes
import operator
import psutil
import random
import requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import random

# ================================ MEMORY =============================================================#
GREETINGS = ["hello jarvis", "jarvis",  "you there jarvis", "time to work jarvis", "hey jarvis",
            "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                "your wish my command", "how can i help you sir?", "i am online and ready sir"]



# ================================ MEMORY ==============================================================#
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 260)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning Sir!")

    elif 12 <= hour < 17:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir")
        

    speak("I am Jarvis ready to help you!")
    print("I am Jarvis ready to help you!")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('suryansh0408@gmail.com', 'raulrai14')
    server.sendmail('suryansh0408@gmail.com', to, content)
    server.close()


# if __name__ == "__main__":
def task_execution():
    wishMe()
    while True:

        query = takeCommand().lower()

        def Temperature():
            city = query.split("in", 1)
            soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{city[1]}").text, "html.parser")
            region = soup.find("span", class_ = "BNeawe tAd8D AP7Wnd")
            temp = soup.find("div", class_ = "BNeawe iBp4i AP7Wnd")
            day = soup.find("div", class_ = "BNeawe tAd8D AP7Wnd")
            weather = day.text.split("m", 1)
            temperature = temp.text.split("C", 1)
            speak("Its Currently"+weather[1]+" and "+temperature[0]+"Celcius"+"in"+region.text)

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia..")
            speak(results)

        elif 'temperature' in query:
            Temperature()

        elif query in GREETINGS:
            speak(random.choice(GREETINGS_RES))

        elif 'tell me a joke' in query:
            speak("here is a joke for you sir")
            joke = pyjokes.get_joke()
            speak(joke)

        elif "check battery " in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"we have {percentage} percent battery")
            # if percentage>=70:
                # speak("No problem till now we have enough battery sir")
            # elif 70< percentage <= 20:
                # speak("sir we have almost used half percent of battery")
            # else:
                # speak("sir we need to charge battery is running out")

        elif 'open terminal' in query:
            os.system("open /System/Applications/Utilities/Terminal.app")
        # elif 'close terminal' in query:
            # os.system("kill -sigkill 29578")

        elif 'open youtube' in query:
            speak("launching youtube sir")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("what should i search in google")
            cm = takeCommand().lower()
            pwt.search(f"{cm}")
        

        elif "open website" in query:
            speak("which one will you like to open sir")
            new = takeCommand().lower()
            speak(f"opening {new} website")
            webbrowser.open(f"https://www.{new}.com")

        elif 'open facebook' in query:
            speak("launching facebook sir")
            webbrowser.open("https://www.facebook.com")

        elif 'open stackoverflow' in query:
            speak("launching stackoverflow sir")
            webbrowser.open("https://www.stackoverflow.com")

        elif 'open linkedin' in query:
            speak("launching linkedin sir")
            webbrowser.open("https://www.linkedin.com")

        elif 'play music' in query:
            speak ("sir, what should i play")
            cmm = takeCommand().lower()
            speak(f"playing {cmm}")
            pwt.playonyt(cmm)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'open vscode' in query:
            speak("opening vscode")
            os.system("open /Applications/visual\ studio/ code.app")

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            os.system("open /Applications/WhatsApp.app")

        elif 'open eclipse' in query:
            speak("opening eclipse")
            os.system("open /Application/Eclipse.app")

        elif 'open pycharm' in query:
            speak("opening pycharm")
            os.system("open /Applications/pycharm ce.app")

        elif 'open xcode' in query:
            speak("opening xcode")
            os.system("open /Applications/xcode.app")

        elif 'switch window' in query:
            pyautogui.keyDown("command")
            pyautogui.press("tab")
            # pyautogui.press("right arrow key")
            time.sleep(1)
            pyautogui.keyUp("command")

        elif 'switch window to right' in query:
            pyautogui.keyDown("command")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("command")

        elif 'send mail' in query:
            try:
                speak("what should i say")
                content = takeCommand().lower()
                to = "vaibhavchauhan0400@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to send this mail")

        elif 'do calculaton' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("what should i calculate sir")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operater_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divide' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operater_fn(oper)(op1, op2)
            speak("result is")
            speak(eval_binary_expr(*(my_string.split())))
        elif 'you can sleep' in query:
            speak("As you wish sir, you can call me any time")
            break

if __name__ == "__main__":
    task_execution()

    command = takeCommand().lower()

    if 'wake up' in command:
        speak("i am back sir")
        task_execution()
    elif "goodbye" or "take rest" in command:
        speak("bye sir, have a good day")
        sys.exit()
    # elif "temperature " in command:
    #     Temperature()