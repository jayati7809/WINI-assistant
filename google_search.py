import webbrowser
import urllib.parse
from speech_engine import speak

def google_search(query: str):
    if not query:
        speak("What should I search for?")
        return
    speak(f"Searching Google for {query}.")
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    webbrowser.open(url)
