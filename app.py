from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Your OpenWeatherMap API key
api_key = "035e68154035049697c3ea7fb7531c20"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            temperature = data['main']['temp']
            wind_speed = data['wind']['speed']
            weather_description = data['weather'][0]['description']
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Define the risk factor based on wind speed
            if wind_speed > 10:
                risk = "High"
            else:
                risk = "Normal"

            weather_data = {
                'city': city,
                'temperature': temperature,
                'wind_speed': wind_speed,
                'description': weather_description,
                'time': time,
                'risk': risk
            }

            return render_template('weather.html', weather=weather_data)
        else:
            error_message = "City not found. Please enter a valid city name."
            return render_template('weather.html', error=error_message)

    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)

