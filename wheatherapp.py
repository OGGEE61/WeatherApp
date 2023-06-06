import requests

api_key = 'e8081ab0568ec8b77c4318ba87cece26'

user_input = input("Enter the city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&APPID={api_key}").json()
print(weather_data)