import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am sanskrit sir. Please")

def takeCommand():
    #It takes microphone input from the uder and give output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

    #logic
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open dumka engineering college' in query:
            webbrowser.open("dumka engineering college.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\harsh\Desktop\musicc'
            songs = os.listdir(music_dir)
            speak(songs)
            os.startfile(os.path.join(music_dir, songs[random]))
            random.seed(5)
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'swastika' in query:
            picture_location = "C:\swastika ka chitra.jpg"
            os.startfile(picture_location)
       # elif 'email to harsh' in query:
