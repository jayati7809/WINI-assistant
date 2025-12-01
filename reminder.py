import json
from pathlib import Path
from datetime import datetime
from speech_engine import speak

REM_FILE = Path("wini_reminders.json")

def _load():
    if not REM_FILE.exists():
        return []
    try:
        return json.loads(REM_FILE.read_text(encoding="utf-8"))
    except:
        return []

def _save(reminders):
    REM_FILE.write_text(json.dumps(reminders, ensure_ascii=False, indent=2), encoding="utf-8")

def set_reminder(text: str):
    """
    Expected format e.g. "remind me at 19:30 to call mom" or "at 19:30 do call mom"
    For simplicity, we look for HH:MM in the text.
    """
    if not text:
        speak("I did not hear the reminder.")
        return
    import re
    m = re.search(r'([01]?\d|2[0-3]):([0-5]\d)', text)
    if not m:
        speak("Please include a time like 19:30.")
        return
    t = m.group(0)
    message = text.replace(t, "").replace("at", "").replace("to", "").strip()
    reminders = _load()
    reminders.append({"time": t, "message": message})
    _save(reminders)
    speak(f"Reminder set at {t} to {message}")

def check_reminders():
    reminders = _load()
    if not reminders:
        return
    now = datetime.now().strftime("%H:%M")
    others = []
    for r in reminders:
        if r.get("time") == now:
            msg = r.get("message") or "You asked me to remind you."
            speak(f"Reminder: {msg}")
        else:
            others.append(r)
    _save(others)
