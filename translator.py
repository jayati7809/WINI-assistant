from googletrans import Translator
from speech_engine import speak

_trans = Translator()

def translate_to_hindi(text: str):
    if not text:
        speak("Please say the sentence to translate to Hindi.")
        return
    try:
        res = _trans.translate(text, dest='hi')
        speak(f"The Hindi translation is: {res.text}")
    except Exception as e:
        print("Translate error:", e)
        speak("Translation failed.")

def translate_to_english(text: str):
    if not text:
        speak("Please say the sentence to translate to English.")
        return
    try:
        res = _trans.translate(text, dest='en')
        speak(f"The English translation is: {res.text}")
    except Exception as e:
        print("Translate error:", e)
        speak("Translation failed.")
