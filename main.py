import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import time
import musicLibrary
import requests
import client
import voice
import functionality




recognizer = sr.Recognizer()

def aiProcess(command):
    # Send the command to the AI and get a response
    response = client.ask_gemini(command)
    return response



def speak(text):
    print("Jarvis:", text)

    engine = pyttsx3.init()   # 🔥 fresh engine
    engine.setProperty('rate', 170)

    engine.say(text)
    engine.runAndWait()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)

    engine.stop()
    del engine          # 🔥 force cleanup
    time.sleep(0.1)     # 🔥 VERY IMPORTANT

#commands = you can add more functionality here, like opening applications, searching the web, etc.
def processCommand(c):
    if "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
        voice.speak("Opening YouTube")
    elif "open google" in c:
        webbrowser.open("https://www.google.com")
        voice.speak("Opening Google")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
        voice.speak("Opening Facebook")
    elif "open twitter" in c:
        webbrowser.open("https://www.x.com")
        speak("Opening Twitter")
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif "open github" in c:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")
    elif "open stackoverflow" in c:
        webbrowser.open("https://www.stackoverflow.com")
        speak("Opening StackOverflow")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")
        
    elif "tell me a joke" in c:
        joke = functionality.joke("Tell me a joke")
        speak(joke)
    
    elif "play" in c:
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link is None:
            speak(f"Sorry, I don't have {song} in my music library.")
        else:
            webbrowser.open(link)
            speak(f"Playing {song}")
    else:
        outptut = aiProcess(c)
        print(outptut)
        speak(outptut)

voice.speak("initializing voice assistant moon.....")
voice.speak("hello, how can I assist you today?")

# if __name__ == "__main__":
#     speak("initializing voice assistant.....")

r = sr.Recognizer()

while True:
    #listen for the wake word "assistant" or "jarvis"
    
        # recognize speech using google
    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        command = r.recognize_google(audio)

        if command.lower() == "assistant" or command.lower() == "jarvis":
            voice.speak("Yes, how can I assist you?")
            with sr.Microphone() as source:
                print("Listening for command...")
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            c = command.lower()
            processCommand(c)
        
    except sr.UnknownValueError:
        print("assistant is active, say assistant to give a command.")
        
    except sr.RequestError as e:
        print("Error; {0}".format(e))

# speak("Hello, how can I assist you today?")
