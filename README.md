# Python Mini Projects (OIBSIP Internship Tasks)

This repo has 5 small Python projects I built during my internship. Each one was a task on its own, and I picked them to practice different things — speech handling, simple calculations, string/random logic, working with a real API, and finally networking with sockets. None of these use any AI models, they're all plain Python logic, which was kind of the point — I wanted to actually understand what's happening instead of importing something that does the work for me.

## Projects in this repo

1. Voice Assistant
2. BMI Checker
3. Random Password Generator
4. Weather App
5. Real-Time Chat App

---

## 1. Voice Assistant

A simple voice assistant. It listens through the microphone, figures out what I said, and replies out loud. Nothing complicated — no AI model behind it, just simple keyword matching.

**What it does**
- Listens through the microphone and converts speech to text
- Says a greeting when I say "hello"
- Tells the time and date when asked
- Searches Google for whatever topic I say, and also prints the query + URL in the terminal so I can see it without switching windows
- If it doesn't understand, it asks me to repeat instead of crashing or staying silent

**Files**
```
main.py         -> run this one. Main loop that listens and decides what to do
voiceReader.py  -> speak() and listen_voice(). Mic input and voice output
time_assis.py   -> tell_time()
date_assis.py   -> tell_date()
websearch.py    -> search_web_direct(). Opens the browser and prints the query
```
I split it into files instead of one big script so each part is easy to find and edit on its own.

**How to run**
```bash
pip install SpeechRecognition pyttsx3 pyaudio
python main.py
```
(PyAudio can be hard to install on Windows — if it fails, try an environment with an older/stable Python version, that usually fixes it.)

It'll say "Voice Assistant activated" and "Say Hello Start". After that just talk normally — things like "hello", "whats the time", "whats the date", "search for laptops under 50000", or "stop"/"exit"/"quit" to close it.

**How the matching works:** It's not NLP, just checks if certain words appear anywhere in what I said. If the sentence has "time" in it, it runs `tell_time()`. Simple to read, but it also means it won't understand every possible way of phrasing something.

**Known limitations**
- Needs internet (speech recognition and search both need it)
- Only understands one command at a time, not multi-step sentences
- If two keywords are in the same sentence (like "time" and "date" together), it only catches whichever `elif` comes first
- Mic quality and background noise affect recognition

---

## 2. BMI Checker

A simple script to calculate BMI (Body Mass Index) using weight (kg) and height (feet), and show which category you fall into.

**How it works**
1. Enter weight in kg
2. Enter height in feet
3. Height gets converted to meters
4. BMI = weight / (height_in_meters ** 2)
5. Based on the result, shows a category

| BMI Range | Category |
|---|---|
| < 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25 – 29.9 | Overweight |
| 30 and above | Obese |

**How to run**
```bash
python bmi_checker.py
```

**Example**
```
---CHECK YOUR BMI(Body Mass Index)---
Enter your weight in kg: 65
Enter your height in feet: 5.6

Your weight is 65.0 kg and height is 1.71 m.

Result:-
Your BMI is: 22.19
Category: Normal
```

**Tech used:** Python, nothing else.

---

## 3. Random Password Generator

A command-line tool that generates random passwords based on what the user picks. I made this mainly to practice loops, functions, and input validation.

**Features**
- Minimum length of 8 characters — anything less gets rejected
- Choose which character types to include: uppercase, lowercase, numbers, symbols
- At least 2 character types must be selected
- Every selected type is guaranteed to appear in the password
- Handles bad input like letters, blank input, or too-short length
- Keeps running until you say no — no need to restart the script

**How it's structured**
- `get_length()` — asks for password length and checks it's valid
- `get_choices()` — asks which character types to use
- `make_password()` — builds the password and shuffles it
- `main()` — runs everything and handles the "generate again" loop

**How to run**
```bash
python password_generator.py
```
Then enter the length, answer y/n for each character type, and it prints the password. Type `y` to generate another or `n` to exit.

**Example**
```
Enter password length (min 8): 10
Uppercase letters? (y/n): y
Lowercase letters? (y/n): y
Numbers? (y/n): y
Symbols? (y/n): n

Generated Password: aB3fT9mZk2

Generate another password? (y/n): n
Goodbye!
```

**How the password is built:** One character from each selected type gets added first, so every chosen type actually shows up. Then the rest is filled randomly from the full pool, and everything gets shuffled at the end so the order isn't predictable.

**Things I'd add later:** a GUI version with tkinter, copying the password to clipboard, a strength indicator (weak/medium/strong), and swapping `random` for the `secrets` module for actual security use.

**Tech used:** Python, `random`, `string` — no installation needed.

---

## 4. Weather App

A command-line tool that shows the current weather for any city — temperature, condition, humidity, wind speed — pulled live from OpenWeatherMap. I built this while learning full stack development, mainly to get comfortable working with a real API instead of static data.

**What it does**
- Type a city name, get the current weather
- Shows temperature in both °C and °F
- Also shows condition, humidity, and wind speed
- Doesn't crash on a wrong city name, dropped internet, or a bad API key — just tells you what went wrong and lets you try again
- Lets you check as many cities as you want in one run

**How to run**
```bash
pip install requests
```
Get a free API key from openweathermap.org and put it in the `API_KEY` variable at the top of the file, then:
```bash
python weather_app.py
```
Enter a city name, it prints the weather, type `n` when asked to check another city.

**Example**
```
------ WEATHER APP-------

Enter city name: London

        Weather in London
-----------------------------------
Temperature:  18.4  °C / 65.1  °F
Condition:  Scattered Clouds
Humidity:  72 %
Wind Speed:  4.1 m/s
-----------------------------------

Check another city? (y/n):
```

**Why I built it this way:** I split the code into separate functions (getting the city, fetching the weather, printing it) so it's easier to read and fix if something breaks. I also handled the common failure cases — wrong city, no internet, bad key — instead of letting it just crash, since that matters in real projects.

**Things I'd add later:** move the API key into an environment variable instead of hardcoding it, add a multi-day forecast, and maybe turn it into a small Flask web app.

**Tech used:** Python, `requests`, OpenWeatherMap API.

---

## 5. Real-Time Chat App

A two-user command-line chat application using Python sockets and threading.

**Files**
- `server.py` — listens for connections and relays messages between two clients
- `client.py` — connects to the server and lets you send/receive messages

**How it works**
1. Run the server first — it waits for two clients to connect
2. Run the client script twice (two separate terminals) to simulate two users
3. Each client enters a name, then messages from one client show up on the other's screen with a timestamp, like `[14:35] Alice: Hello`
4. If one client disconnects, the other gets notified

**How to run**
```bash
python server.py
```
Then in two more terminals:
```bash
python client.py
```

**Tech used:** Python, `socket`, `threading` — no external libraries.

---

## About this repo

These were all done as individual internship tasks, so each one lives in its own folder with its own script(s) — this README just brings them together in one place. I kept things simple on purpose across all 5: plain Python, clear function names, and enough error handling that they don't just crash on bad input.
