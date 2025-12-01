import psutil
from speech_engine import speak

def battery_status():
    try:
        batt = psutil.sensors_battery()
        if batt:
            percent = batt.percent
            plugged = batt.power_plugged
            speak(f"Battery is at {percent} percent. Power plugged in: {plugged}.")
        else:
            speak("Battery information is not available.")
    except Exception as e:
        print("Battery error:", e)
        speak("Could not get battery status.")

def internet_speed():
    speak("Internet speed check is not enabled in this build.")
