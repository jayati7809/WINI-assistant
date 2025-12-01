from speech_engine import speak
from reminder import _load, _save
import json

def set_alarm(time_str: str):
    if not time_str:
        speak("I did not hear the alarm time.")
        return
    # For simplicity reuse reminders storage
    reminders = _load()
    reminders.append({"time": time_str, "message": "Alarm"})
    _save(reminders)
    speak(f"Alarm set at {time_str}")
