import subprocess
import os
from speech_engine import speak

COMMON_APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    # "chrome": r"chrome.exe",
    # "edge": r"msedge.exe"
}

def open_app(name: str):
    name = (name or "").lower()
    if not name:
        speak("Which app should I open?")
        return
    exe = COMMON_APPS.get(name)
    if exe:
        try:
            subprocess.Popen([exe])
            speak(f"Opening {name}.")
        except Exception as e:
            print("Open app error:", e)
            speak(f"Could not open {name}.")
    else:
        #  try startfile on Windows 
        try:
            os.startfile(name)
            speak(f"Opening {name}.")
        except Exception:
            speak(f"I don't know how to open {name}.")
