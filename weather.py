import requests
from speech_engine import speak
OPENWEATHER_API_KEY = "002a7317d5901f8fc69bed340596fc10" 
def get_weather(city: str):
    city = (city or "").strip()
    if not city:
        speak("Please provide a city name.")
        return
    if not OPENWEATHER_API_KEY:
        speak("Weather feature requires an OpenWeatherMap API key. Add it to weather.py to enable this feature.")
        return
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        r = requests.get(url, timeout=8)
        if r.status_code != 200:
            speak("I couldn't fetch the weather for that city.")
            return
        data = r.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        speak(f"The weather in {city} is {desc} with a temperature of {temp} degrees Celsius.")
    except Exception as e:
        print("Weather error:", e)
        speak("Failed to get weather.")
