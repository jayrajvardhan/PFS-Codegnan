import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
engine = pyttsx3.init()
def speak(text):
    engine.say("hello jai")
    engine.runAndWait()



def speak(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.pause_threshold=1
        audio = recognizer.listen(source)
    try:
        print("Recognizing.....")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except Exception:
        print("Sorry please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning \n Iam your virtual assistant")
    elif hour > 18:
        speak("Good Afternoon \n Iam your virtual assistant")
    else:
        speak("Good Evening \n Iam your virtual assistant")
wish_user()
while True:
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I : %M %P")
        speak(f"the time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
    elif "open whatsapp" in command:
        webbrowser.open("https://www.whatsapp.com")
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person,2)
        print(info)
        speak(info)

    elif "exit" in command:
        speak("Goodbye")
        break
    
