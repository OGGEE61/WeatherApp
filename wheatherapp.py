import requests
import datetime

api_key = 'e8081ab0568ec8b77c4318ba87cece26'

user_input = input("Enter the city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}").json()

if weather_data['cod'] == '404':
    print('City not found')
else:
    weather = weather_data['weather'][0]['main']
    temp = round(weather_data['main']['temp'])
    sunrise = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'] )
    sunset = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    
# Extract only the time portion
sunrise_time = sunrise.time()
sunset_time = sunset.time()


print(f'The weather in {user_input} is {weather} and the temperature is {temp} degrees Celcius.')
print(f'Sunrise is at {sunrise_time} and sunset is at {sunset_time}.')