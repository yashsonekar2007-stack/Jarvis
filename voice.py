import pyttsx3
import time

def speak(text):
    print("Jarvis:", text)

    engine = pyttsx3.init()   # 🔥 fresh engine
    engine.setProperty('rate', 170)

    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

    engine.stop()
    del engine          # 🔥 force cleanup
    time.sleep(0.1)     # 🔥 VERY IMPORTANT

