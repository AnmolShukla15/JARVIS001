import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "linked in" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ") [1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
    else:
        speak("Sorry, I didn't understand that command.")   

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            
            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "jarvis":
                speak("Yes")
                print("Wake word detected: Jarvis")
                
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis is Active... Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)