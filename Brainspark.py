import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    
    speak("I am brainspark . Please tell me how may i help you")

def takecommand():
    #It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        quary = r.recognize_google(audio)
        print(f"User said: {quary}\n")

    except Exception as e:
        print(e)

        print("say that again please...")
        return "None"
    return quary

if __name__ == "__main__":
    wishMe()
    while True:
        quary = takecommand().lower()
        
        #Logic for executing tasks based on quary
        if 'wikipedia' in quary:
            speak('Searching wikipedia...')
            quary = quary.replace("wikipedia","")
            results = wikipedia.summary(quary,sentences=2)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in quary:
            webbrowser.open("youtube.com")
        
        elif 'open google' in quary:
            webbrowser.open("google.com")
        
        elif 'play music' in quary:
            music_dir='c:\\Users\\Krupa\\Music\\Desktop\\music directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play another music' in quary:
            music_dir='c:\\Users\\Krupa\\Music\\Desktop\\music directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in quary:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir,The time is {strTime}")
            speak(f"Sir,The time is {strTime}")

        elif 'who made you' in quary:
            print("I was created by Riddhi patel")
            speak("I was created by Riddhi patel")

        elif 'how are you' in quary:
            print("I don't have feelings but Thanks for asking.")
            speak("I don't have feelings but Thanks for asking.")

        elif 'your name' in quary:
            print("My name is brainspark.")
            speak("My name is brainspark.")

        elif 'about yourself' in quary:
            print("I am brainspark created by Riddhi patel. I am created to assist and interact with users and specialy students.")
            speak("I am brainspark created by Riddhi patel. I am created to assist and interact with users and specialy students.")

        elif 'thank you' in quary:
            print("your welcome. I am always with you.")
            speak("your welcome. I am always with you.")

        elif 'Artificial intelligence' in quary:
            print("Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are designed to think and")
            print("learn like humans. It encompasses various technologies, including machine learning, natural language processing, and")
            print("computer vision, enabling machines to perform tasks such as recognizing speech, analyzing data, and making decisions.")
            print("AI is transforming industries by automating processes, enhancing customer experiences, and providing insights through")
            print("data analysis, thus driving innovation and efficiency.")
            speak("Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are designed to think and")
            speak("learn like humans. It encompasses various technologies, including machine learning, natural language processing, and")
            speak("computer vision, enabling machines to perform tasks such as recognizing speech, analyzing data, and making decisions.")
            speak("AI is transforming industries by automating processes, enhancing customer experiences, and providing insights through")
            speak("data analysis, thus driving innovation and efficiency.")

        elif 'tips for better sleep' in quary:
            print("Here are some tips for better sleep ")
            print("1. Maintain a consistent sleep schedule.")
            print("2. Create a relaxing bedtime routine.")
            print("3. Limit screen time before bed.")
            print("4. Keep your bedroom cool and dark.")
            print("5. Avoid caffeine and heavy meals in the evening.")
            print("6. Get regular exercise, but not too close to bedtime.")
            speak("Here are some tips for better sleep ")
            speak("1. Maintain a consistent sleep schedule.")
            speak("2. Create a relaxing bedtime routine.")
            speak("3. Limit screen time before bed.")
            speak("4. Keep your bedroom cool and dark.")
            speak("5. Avoid caffeine and heavy meals in the evening.")
            speak("6. Get regular exercise, but not too close to bedtime.")

        elif 'weekly workout plan' in quary:
            print("Here is a simple weekly workout plan for you:")
            print("Monday: 30 minutes of cardio (e.g., running or cycling)")
            print("Tuesday: Strength training (upper body)")
            print("Wednesday: Rest or light yoga")
            print("Thursday: 30 minutes of cardio")
            print("Friday: Strength training (lower body)")
            print("Saturday: Full-body workout")
            print("Sunday: Rest or light stretching")
            speak("Here is a simple weekly workout plan for you:")
            speak("Monday: 30 minutes of cardio (e.g., running or cycling)")
            speak("Tuesday: Strength training (upper body)")
            speak("Wednesday: Rest or light yoga")
            speak("Thursday: 30 minutes of cardio")
            speak("Friday: Strength training (lower body)")
            speak("Saturday: Full-body workout")
            speak("Sunday: Rest or light stretching")

        elif 'bye' in quary:
            break