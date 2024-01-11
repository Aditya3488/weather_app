import requests
import tkinter as tk
from tkinter import ttk

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def fetch_weather():
    city = city_entry.get()
    api_key = api_key_entry.get()
    
    weather_data = get_weather(api_key, city)

    if weather_data['cod'] == '404':
        result_label.config(text="City not found. Please check the city name.")
    else:
        temperature_celsius = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']

        result_label.config(text=f"Weather in {city}:\nTemperature: {temperature_celsius:.2f}°C\nDescription: {weather_description}")

# Create the main window
app = tk.Tk()
app.title("Weather App")

# Create and pack widgets
api_key_label = ttk.Label(app, text="Enter API Key:")
api_key_label.pack(pady=5)

# Replace 'YOUR_API_KEY' with your actual API key
api_key_entry = ttk.Entry(app, show="*")
api_key_entry.insert(0, 'd56fa90b8c60ae34c405449b6691068d')  # Insert your API key here
api_key_entry.pack(pady=5)

city_label = ttk.Label(app, text="Enter City:")
city_label.pack(pady=5)

city_entry = ttk.Entry(app)
city_entry.pack(pady=5)

fetch_button = ttk.Button(app, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

result_label = ttk.Label(app, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
app.mainloop()
