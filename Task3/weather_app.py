import requests

# Helper to handle the API connection and data display
def get_weather():
    # Unique API Key from OpenWeatherMap
    api_key = "ab96fc08699e15df1510c69d5c7cdfa6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    print("-" * 50)
    print("      Welcome to My Basic Weather App!      ")
    print("-" * 50)

    # Getting the city name from the user
    city = input("Which city's weather would you like to check? ").strip()

    if not city:
        print("Oops! You didn't enter a city name. Please try again.")
        return

    # Preparing the URL with metric units for Celsius
    # 'q' is for city name, 'appid' is for our key
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    try:
        # Making the actual request to the OpenWeather server
        response = requests.get(complete_url)
        data = response.json()

        # '200' means everything went well
        if data["cod"] == 200:
            main_data = data["main"]
            weather_info = data["weather"][0]
            
            temp = main_data["temp"]
            humidity = main_data["humidity"]
            description = weather_info["description"]

            # Displaying the results in a clean format
            print("\n" + "=" * 50)
            print(f"Current Weather in {city.capitalize()}:")
            print(f"  > Temperature: {temp}°C")
            print(f"  > Humidity:    {humidity}%")
            print(f"  > Condition:   {description.capitalize()}")
            print("=" * 50)
            print("Stay safe and have a great day!")
            
        else:
            # This handles cases where the city name might be spelled wrong
            print(f"\nSorry, I couldn't find '{city}'. Is the spelling correct?")

    except requests.exceptions.ConnectionError:
        print("\nConnection Error: Please check your internet and try again.")
    except Exception as e:
        print(f"\nSomething went wrong: {e}")

if __name__ == "__main__":
    get_weather()