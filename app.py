from flask import Flask, render_template, request # type: ignore
import requests # type: ignore
from datetime import datetime

app = Flask(__name__)

# OpenWeatherMap API key
api_key = "035e68154035049697c3ea7fb7531c20"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    city = request.form.get('city') if request.method == 'POST' else request.args.get('city')
    
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            temperature = data['main']['temp']
            wind_speed = data['wind']['speed']
            weather_description = data['weather'][0]['description']
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Determine risk factor based on wind speed
            risk = "High" if wind_speed > 10 else "Normal"

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
