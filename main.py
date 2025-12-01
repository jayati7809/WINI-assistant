from listener import listen
from speech_engine import speak, speak_now, start_tts_worker
from commands import tell_time, tell_date, tell_joke
from youtube_player import play_youtube
from google_search import google_search
from wiki_search import wiki_search
from weather import get_weather
from translator import translate_to_hindi, translate_to_english
from memory import remember, recall
from reminder import set_reminder, check_reminders
from alarm import set_alarm
from apps import open_app
from screenshot import take_screenshot
from system_info import battery_status, internet_speed
from location import get_location
from chathandeler import answer_question
from autorestart import restart_delay

import threading
import time
import sys
import traceback

# Start with a blocking greeting so you can hear it immediately
speak_now("Wini is now online. How can I help you?")

# start TTS worker that handles all future speech calls safely
start_tts_worker()

# Reminder checker thread (non-blocking)
def reminder_worker(stop_event):
    while not stop_event.is_set():
        try:
            check_reminders()
        except Exception:
            pass
        time.sleep(20)

stop_event = threading.Event()
threading.Thread(target=reminder_worker, args=(stop_event,), daemon=True).start()

def process_command(command):
    if not command:
        return

    cmd = command.lower()

    # CORE
    if "time" in cmd:
        tell_time(); return
    if "date" in cmd:
        tell_date(); return
    if "joke" in cmd:
        tell_joke(); return

    # MULTIMEDIA
    if cmd.startswith("play "):
        play_youtube(cmd.replace("play ", "", 1).strip()); return

    # SEARCH
    if "search" in cmd:
        google_search(cmd.replace("search", "").strip()); return
    if "wikipedia" in cmd or cmd.startswith("who is") or cmd.startswith("what is"):
        # pass the full command to wiki handler
        wiki_search(cmd); return

    # WEATHER
    if "weather" in cmd:
        speak("Which city?")
        city = listen()
        if city:
            get_weather(city)
        else:
            speak("I did not hear the city name.")
        return

    # TRANSLATION
    if "translate" in cmd and "hindi" in cmd:
        speak("Tell me the sentence.")
        text = listen()
        if text:
            translate_to_hindi(text)
        else:
            speak("I did not hear any sentence.")
        return
    if "translate" in cmd and "english" in cmd:
        speak("Tell me the sentence.")
        text = listen()
        if text:
            translate_to_english(text)
        else:
            speak("I did not hear any sentence.")
        return

    # MEMORY
    if "remember that" in cmd:
        try:
            phrase = cmd.replace("remember that", "").strip()
            key, value = phrase.split(" is ", 1)
            remember(key.strip(), value.strip())
        except Exception:
            speak("Say it like: remember that my name is Jayati.")
        return
    if cmd.startswith("what is") or cmd.startswith("who is"):
        key = cmd.replace("what is", "").replace("who is", "").strip()
        recall(key); return

    # REMINDERS
    if "remind me" in cmd or "set reminder" in cmd:
        speak("Please say the reminder like: remind me at 19:30 to call mom")
        rem = listen()
        if rem:
            set_reminder(rem)
        else:
            speak("I did not hear the reminder.")
        return
    if "alarm" in cmd:
        speak("Tell me the time like 19:30")
        atime = listen()
        if atime:
            set_alarm(atime)
        else:
            speak("I did not hear the alarm time.")
        return

    # APPS & SYSTEM
    if cmd.startswith("open "):
        open_app(cmd.replace("open ", "", 1).strip()); return
    if "screenshot" in cmd:
        take_screenshot(); return
    if "battery" in cmd:
        battery_status(); return
    if "internet speed" in cmd or "speed test" in cmd:
        internet_speed(); return
    if "location" in cmd or "where am i" in cmd:
        get_location(); return

    # GPT / Q&A
    if cmd.startswith("ask ") or cmd.startswith("question "):
        q = cmd.replace("ask ", "").replace("question ", "").strip()
        if q:
            answer_question(q)
        return

    # EXIT
    if "stop" in cmd or "exit" in cmd or "bye" in cmd:
        speak("Goodbye!")
        sys.exit(0)

    # DEFAULT: try chathandeler
    answered = answer_question(command)
    if not answered:
        speak("I did not understand that. Please say it again.")

def main_loop():
    while True:
        try:
            command = listen()
            process_command(command)
        except KeyboardInterrupt:
            speak("Shutting down.")
            break
        except Exception as e:
            print("MAIN ERROR:", e)
            speak("Oops, I had an error. Restarting now.")
            traceback.print_exc()
            restart_delay(2)

if __name__ == "__main__":
    main_loop()
