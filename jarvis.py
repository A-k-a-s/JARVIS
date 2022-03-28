import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("this is jarvis how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music = "C:\\songs"
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[0]))

        elif "the time " in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir, the time is {strtime}")

        elif "open chrome" in query:
            chromepath = "C:\\Users\\Dell\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am uable to send this email at the moment")
        elif "close the programme" in query:
            exit()








