import webbrowser
from speech_engine import speak
import urllib.parse

def play_youtube(query: str):
    if not query:
        speak("What should I play?")
        return
    speak(f"Playing {query} on YouTube.")
    q = urllib.parse.quote_plus(query)
    url = f"https://www.youtube.com/results?search_query={q}"
    webbrowser.open(url)
