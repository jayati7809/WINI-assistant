import speech_recognition as sr
from speech_engine import speak

recognizer = sr.Recognizer()

def listen(timeout: int = 5, phrase_time_limit: int = 6) -> str:
    """
    Listen from the default microphone and return recognized text (or None).
    timeout: max seconds waiting for phrase to start
    phrase_time_limit: max seconds of phrase
    """
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.6)
            print("Listening...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    except sr.WaitTimeoutError:
        print("Listen: timeout waiting for phrase.")
        return None
    except Exception as e:
        print("Listen error:", e)
        speak("Microphone error.")
        return None

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Recognition: did not understand audio.")
        return None
    except sr.RequestError as e:
        print("Recognition request failed:", e)
        speak("Speech recognition service error.")
        return None
