# Weather App (Python + OpenWeatherMap API)

A small command-line tool that shows the current weather for any city you type in — temperature, condition, humidity, and wind speed, pulled live from OpenWeatherMap.

I built this while learning full stack development, mainly to get comfortable working with a real API instead of just static data.

## What it does

- Type in a city name, get the current weather for it
- Shows temperature in both °C and °F
- Also shows condition, humidity, and wind speed
- Doesn't crash if the city name is wrong, the internet drops, or the API key is bad — it just tells you what went wrong and lets you try again
- Lets you check as many cities as you want in one run

## Tech used

- Python 3
- `requests` library for calling the API
- OpenWeatherMap API for the actual weather data

## How to run it

1. Download or clone this repo.
2. Install requests if you don't have it already:
   ```
   pip install requests
   ```
3. Get a free API key from openweathermap.org and put it in the `API_KEY` variable at the top of the file.
4. Run it:
   ```
   python weather_app.py
   ```
5. Enter a city name and it'll print the weather. Type `n` when it asks if you want to check another city.

## Example run

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

## Why I built it this way

I split the code into separate functions (getting the city, fetching the weather, printing it) instead of writing everything in one block, mainly so it's easier to read and easier to fix if something breaks. I also made sure to handle the common failure cases — wrong city name, no internet, bad API key — instead of just letting the program crash, since that's the kind of thing that actually matters in real projects.

## Things I'd add if I kept working on this

- Move the API key out of the code and into an environment variable (right now it's hardcoded, which isn't something you'd want in a real production app)
- Add a multi-day forecast instead of just current weather
- Turn it into a small web app using Flask

