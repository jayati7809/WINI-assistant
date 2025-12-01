import requests
from speech_engine import speak

def get_location():
    try:
        r = requests.get("https://ipinfo.io/json", timeout=6)
        if r.status_code == 200:
            data = r.json()
            city = data.get("city")
            region = data.get("region")
            country = data.get("country")
            speak(f"You appear to be in {city}, {region}, {country}.")
        else:
            speak("I couldn't determine your location.")
    except Exception as e:
        print("Location error:", e)
        speak("Unable to get location.")
