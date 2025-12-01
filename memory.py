import json
from pathlib import Path
from speech_engine import speak

DATA_FILE = Path("wini_memory.json")

def _load():
    if not DATA_FILE.exists():
        return {}
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except:
        return {}

def _save(data):
    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def remember(key: str, value: str):
    data = _load()
    data[key] = value
    _save(data)
    speak(f"I will remember that {key} is {value}.")

def recall(key: str):
    data = _load()
    val = data.get(key)
    if val:
        speak(f"{key} is {val}.")
    else:
        speak(f"I don't have anything stored for {key}.")
