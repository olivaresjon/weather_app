from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
#app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    api_key = 'fd1b8dc0034a6eeb2ae08bdc1e359d56' # Replace with your own API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = json.loads(response.text)
    #print(weather_data)  # print out the weather data

    return render_template('weather.html', location=location, weather_data=weather_data)