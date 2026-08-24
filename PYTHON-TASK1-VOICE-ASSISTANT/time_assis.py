import datetime
from voiceReader import speak


def tell_time():
 
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")
