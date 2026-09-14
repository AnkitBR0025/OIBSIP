import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        speak("I am sorry, I did not catch that. Could you please repeat it?")
        return None

    except sr.RequestError:
        speak("My speech service is currently down.")
        return None
