from voiceReader import speak, listen_voice
from time_assis import tell_time
from date_assis import tell_date
from websearch import search_web_direct



if __name__ == "__main__":
    speak("Voice Assistant activated.")
    speak("Say hello to Start")

    
    is_searching = False

    while True:
        command = listen_voice()

        if not command:
            continue


        if is_searching:
            search_web_direct(command)
            is_searching = False
            continue

      
        if "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Have a wonderful day.")
            break

       
        elif "hello" in command:
            speak("Hello there! How can I help you today?")

        elif "date" in command:
            tell_date()

        elif "time" in command:
            tell_time()


        elif "search" in command:
            if "search for" in command:
                query = command.split("search for")[-1].strip()
            else:
                query = command.split("search")[-1].strip()

            if query:
                search_web_direct(query)
            else:
                speak("What would you like me to search for?")
                is_searching = True

        else:
            speak("I heard you, but that task is not in my feature checklist.")

    
