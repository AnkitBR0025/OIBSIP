import datetime
from voiceReader import speak


def tell_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}.")
