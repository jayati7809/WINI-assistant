import pyautogui
from datetime import datetime
from pathlib import Path
from speech_engine import speak

def take_screenshot():
    try:
        p = Path("screenshots")
        p.mkdir(exist_ok=True)
        fname = p / f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        img = pyautogui.screenshot()
        img.save(str(fname))
        speak(f"Saved screenshot as {fname.name}.")
    except Exception as e:
        print("Screenshot error:", e)
        speak("I could not take the screenshot.")
