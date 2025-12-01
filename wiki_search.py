import wikipedia
from speech_engine import speak

def wiki_search(topic: str):
    topic = (topic or "").strip()
    if not topic:
        speak("What topic on Wikipedia should I search for?")
        return
    try:
        speak(f"Searching Wikipedia for {topic}.")
        summary = wikipedia.summary(topic, sentences=2, auto_suggest=True, redirect=True)
        speak(summary)
    except wikipedia.DisambiguationError as e:
        speak(f"The topic {topic} is ambiguous. Please be more specific.")
    except wikipedia.PageError:
        speak(f"I couldn't find information on Wikipedia for {topic}.")
    except Exception as e:
        print("Wiki error:", e)
        speak("Wikipedia search failed.")
