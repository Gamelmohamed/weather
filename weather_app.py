from tkinter import *
import tkinter as tk
import requests

api_key = "30d4741c779ba94c470ca1f63045390a"  

def get_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        temperature = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather_result = f'Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'

        return weather_result

    except requests.exceptions.RequestException as e:
        return f'Error fetching data: {e}'

def search_weather():
    city = entry.get()
    result = get_weather(api_key, city)
    result_label.config(text=result)

weather = tk.Tk()
weather.title("weather_app")
weather.minsize(width=800, height=500)


location = tk.Label(weather, text="location :    ")
location.grid(row=0, column=1)

entry_frame = tk.Frame(weather, padx=30, pady=30)
entry_frame.grid(row=0, column=2, sticky="N")

entry = tk.Entry(entry_frame, width=30)
entry.pack()

btn = Button(weather, text="search", relief=tk.RAISED, padx=10, pady=5, command=search_weather)
btn.grid(row=0, column=3)

result_label = tk.Label(weather, text="")
result_label.grid(row=1, column=1, columnspan=3, sticky="W")



weather.mainloop()
