import requests
import json

# Get the user's current location using their IP address
ip_response = requests.get('https://ipapi.co/json/')
ip_data = json.loads(ip_response.text)
latitude = ip_data['latitude']
longitude = ip_data['longitude']

# Retrieve the weather data for the user's current location
api_key = 'fd1b8dc0034a6eeb2ae08bdc1e359d56'
weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
weather_response = requests.get(weather_url)
weather_data = json.loads(weather_response.text) #We use the json.loads() method to parse the JSON-formatted string into a Python dictionary

#print(weather_response.text) #this is for if you want to see the dictionary

#Parse the weather data using JSON
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
description = weather_data['weather'][0]['description']


# Display the weather data using print statements
print(f'Temperature: {temperature}°C')
print(f'Humidity: {humidity}%')
print(f'Wind Speed: {wind_speed} km/h')
print(f'Description: {description}')
