from datetime import datetime
from speech_engine import speak
import random

def tell_time():
    now = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}.")

def tell_date():
    today = datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {today}.")

def tell_joke():
    jokes = [
        "Why did the computer show up at work late? It had a hard drive.",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the developer go broke? Because he used up all his cache."
    ]
    speak(random.choice(jokes))
