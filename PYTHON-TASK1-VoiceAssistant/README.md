Voice Assistant (Python)

A simple voice assistant I made in Python. It listens through the microphone figures out what I said and replies loud. Nothing complicated. No AI model behind it simple keyword matching.

## What it does

- Listens through the microphone and changes speech to text

- Says a greeting when I say "hello"

- Tells the time when I ask for it

- Tells the date when I ask for it

- Searches Google for whatever topic I say and also prints the search query + URL in the terminal so I can see it without switching windows

- If it doesn't understand what I said it asks me to repeat of crashing or staying silent

## Files

```

main.py -> run this one. Has the main loop that listens and decides what to do

voiceReader.py -> speak() and listen_voice(). The mic input and voice output

time_assis.py -> tell_time()

date_assis.py -> tell_date()

websearch.py -> search_web_direct(). Opens the browser and prints the query in terminal

```

I split it into files instead of one big script so each part is easy to find and edit on its own.

## How to run it

1. Make sure you have these installed:

```

pip install SpeechRecognition pyttsx3 pyaudio

```

(PyAudio can be hard to install on Windows. If it fails use an environment with an older or stable Python version, that usually fixes it.)

2. Run:

```

python main.py

```

3. It'll say "Voice Assistant activated" and "Say Hello Start". After that just talk normally.

## Example things you can say

- "hello"

- "whats the time"

- "whats the date"

- "search for laptops under 50000"

- "search" (it'll ask you what to search for then listen again)

- "stop" / "exit" / "quit" to close it

## How the command matching works

It's not NLP. It just checks if certain words appear anywhere in what you said. For example if the sentence has "time" in it it runs `tell_time()`. That's why it's simple to read. Also why it won't understand every possible way of phrasing a request.

## Known limitations

- Needs an internet connection (speech recognition and search both need it)

- Only understands one command at a time not -step sentences

- If two keywords are in the same sentence (, like "time" and "date" together) it'll only catch whichever `elif` comes first

- Mic quality and background noise affect how well it recognizes speech