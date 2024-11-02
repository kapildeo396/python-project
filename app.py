from flask import Flask, render_template, request  # type: ignore
import requests  # type: ignore
from datetime import datetime
import os
import logging  # Importing logging module

# Setting up logging configuration
logging.basicConfig(filename='error.log', level=logging.DEBUG)

app = Flask(__name__)

# OpenWeatherMap API key
api_key = "035e68154035049697c3ea7fb7531c20"

@app.route('/')
def home():
    try:
        # Printing the current working directory for debugging
        print("Current working directory:", os.getcwd())
        logging.debug("Navigating to home page.")  # Log message
        return render_template('index.html')
    except TemplateNotFound:
        return "<h1>Template Not Found</h1>", 404

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
<<<<<<< HEAD
            logging.debug(f"Weather data retrieved: {weather_data}")  # Log the weather data
=======
>>>>>>> 0cd190137897d103c945c4b23a6789643dd0a9d1
            return render_template('weather.html', weather=weather_data)
        else:
            error_message = "City not found. Please enter a valid city name."
            logging.error(f"City not found error for city: {city}")  # Log the error
            return render_template('weather.html', error=error_message)

    return render_template('weather.html')

# Retrieve the port number from the "PORT" environment variable; default to 10000 if not set
port = int(os.environ.get("PORT", 10000))
if __name__ == '__main__':
<<<<<<< HEAD
    logging.info(f"Starting app on port {port}")  # Log app start
    app.run(host='0.0.0.0', port=port, debug=True)



=======
    app.run(debug=True)
>>>>>>> 0cd190137897d103c945c4b23a6789643dd0a9d1
