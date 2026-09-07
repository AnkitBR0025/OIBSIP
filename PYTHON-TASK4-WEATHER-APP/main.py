import requests

API_KEY = "1cec2ae116576852eecdf4c133a4f81f"


def main():
    print("\n------ WEATHER APP-------")

    while True:
        city = ask_city_name()
        data = fetch_weather(city)

        if data is not None:
            print_weather(data)

        answer = input("\nCheck another city? (y/n): ")
        if answer.lower() != "y":
            print("\nGoodbye!")
            break


def ask_city_name():
    while True:
        city = input("\nEnter city name: ")
        city = city.strip()

        if city == "":
            print("City name can't be empty. Try again.\n")
        else:
            return city


def fetch_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {"q": city,"appid": API_KEY,"units": "metric"}

    
    try:
        response = requests.get(url, params=params, timeout=5)
    except requests.exceptions.Timeout:
        print("\nRequest timed out. Check your internet connection and try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("\nCould not connect. Check your internet connection.")
        return None

    status = response.status_code

    if status == 200:
        # success! give back the data
        return response.json()

    elif status == 404:
        print("\nCity not found. Check the spelling and try again.")
        return None

    elif status == 401:
        print("\nInvalid API key. Check your API_KEY value.")
        return None

    else:
        print("\nSomething went wrong. Status code: ", status)
        return None


def print_weather(data):
    city_name = data["name"]
    temp_c = data["main"]["temp"]
    temp_f = (temp_c * 9 / 5) + 32
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
   
    print("\n        Weather in", city_name)
    print("-" * 35)
    print("Temperature: ", round(temp_c, 1), " °C /", round(temp_f, 1), " °F")
    print("Condition: ", condition.title())
    print("Humidity: ", humidity, "%")
    print("Wind Speed: ", wind_speed, "m/s")
    print("-" * 35)


main()