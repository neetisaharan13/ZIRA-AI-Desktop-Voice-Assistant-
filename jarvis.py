import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("I am ZIRA . Please tell me how may i help you?")


def takeCommand():
    '''
    it takes microphone input from the user and returns the string output.
    '''
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
        print("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('neetisaharan1307@gmail.com', 'passowrd###')
    server.sendmail('neetisaharan1307@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia... ")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia, ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hello, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'email to neeti' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "neetisaharan1307@gmail.com"
                sendEmail(to, content)
                speak("email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")
