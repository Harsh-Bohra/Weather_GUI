# main_weather.py

import requests

def get_weather_report(city="London"):
    api_key = "8f341a6ec3db92356322d68b9b4441e4"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_report = (
            f"Weather report for {data['name']}:\n"
            f"Temperature: {data['main']['temp']}°C\n"
            f"Condition: {data['weather'][0]['description'].capitalize()}"
        )
        return weather_report
    else:
        return "Failed to fetch weather data"

if __name__ == "__main__":
    print(get_weather_report())
