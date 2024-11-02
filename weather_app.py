import requests # type: ignore
from datetime import datetime

# Your OpenWeatherMap API key
api_key = "035e68154035049697c3ea7fb7531c20"

# Get city name input from the user
city = input("Enter the city name: ")

# OpenWeatherMap API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# If the city is found, display the data
if data['cod'] == 200:
    # Extract the data
    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']
    weather_description = data['weather'][0]['description']
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Define the risk factor based on wind speed
    if wind_speed > 10:
        risk = "High"
    else:
        risk = "Normal"

    # Print the result
    print(f"City: {city}")
    print(f"Time: {time}")
    print(f"Temperature: {temperature}°C")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather Description: {weather_description}")
    print(f"Risk: {risk}")

else:
    print("City not found. Please enter a valid city name.")
