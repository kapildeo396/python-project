from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Function to fetch weather data by city
def fetch_weather_by_city(city):
    api_key = "035e68154035049697c3ea7fb7531c20"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        # Check for valid response
        if response.status_code == 200:
            return data
        else:
            return {"error": "City not found or invalid response"}
    
    except Exception as e:
        print(f"Error fetching weather data by city: {e}")
        return {"error": "Error fetching weather data"}

# Function to fetch weather data by coordinates
def fetch_weather_by_coordinates(lat, lon):
    api_key = "035e68154035049697c3ea7fb7531c20"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        # Check for valid response
        if response.status_code == 200:
            return data
        else:
            return {"error": "Coordinates not found or invalid response"}
    
    except Exception as e:
        print(f"Error fetching weather data by coordinates: {e}")
        return {"error": "Error fetching weather data"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if city:
        # Fetch weather by city name
        weather_data = fetch_weather_by_city(city)
    elif lat and lon:
        # Fetch weather by coordinates
        weather_data = fetch_weather_by_coordinates(lat, lon)
    else:
        return jsonify({"error": "City or coordinates required"}), 400
    
    # Check if there is an error in the response
    if 'error' in weather_data:
        return jsonify({"error": weather_data['error']}), 404
    
    # Extract relevant data
    main = weather_data['main']
    wind = weather_data['wind']
    weather_description = weather_data['weather'][0]['description']
    
    formatted_data = {
        'name': weather_data['name'],
        'dt': weather_data['dt'],
        'main': {
            'temp': main['temp'],
            'feels_like': main['feels_like'],
            'humidity': main['humidity'],
            'pressure': main['pressure']
        },
        'wind': {
            'speed': wind['speed']
        },
        'weather': weather_description,
        'clouds': weather_data['clouds']
    }
    
    return jsonify(formatted_data)

if __name__ == "__main__":
    app.run(debug=True)

