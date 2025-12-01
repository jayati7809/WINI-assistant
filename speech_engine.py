import pyttsx3
import threading
import queue
import time

# ------
# Single threaded design:
#    speak_now(): blocking TTS for startup (called BEFORE worker starts)
#   start_tts_worker(): starts worker that is the only thread calling engine.runAndWait()
#    speak(): non-blocking (queue) to be used while worker runs.
# ----

_engine = None
_tts_queue = queue.Queue()
_worker_started = False
_worker_thread = None

def _init_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init('sapi5')
        _engine.setProperty('rate', 160)
        _engine.setProperty('volume', 1.0)
        # Try to select a female voice if present
        voices = _engine.getProperty('voices')
        for v in voices:
            name = (v.name or "").lower()
            if any(x in name for x in ("female", "zira", "heera", "samantha")):
                _engine.setProperty('voice', v.id)
                break

def speak_now(text: str):
    """
    Blocking TTS call. Use at startup BEFORE starting the background worker.
    """
    if not text:
        return
    _init_engine()
    try:
        print("Wini:", text)
        # ensure engine has clean state
        _engine.stop()
        _engine.say(text)
        _engine.runAndWait()
    except Exception as e:
        print("TTS ERROR (speak_now):", e)

def _tts_worker():
    global _engine
    while True:
        text = _tts_queue.get()
        if text is None:
            # sentinel - continue (or break if you want graceful shutdown)
            _tts_queue.task_done()
            continue
        try:
            # Reset audio channel before speaking to avoid routing issues
            _engine.stop()
            _engine.say(text)
            _engine.runAndWait()
        except Exception as e:
            print("TTS ERROR (worker):", e)
        _tts_queue.task_done()

def start_tts_worker():
    """
    Start the background TTS worker thread. Call this once AFTER speak_now() at startup.
    """
    global _worker_started, _worker_thread
    if _worker_started:
        return
    _init_engine()
    _worker_thread = threading.Thread(target=_tts_worker, daemon=True)
    _worker_thread.start()
    _worker_started = True
    # small delay to allow thread to boot
    time.sleep(0.05)

def speak(text: str):
    """
    Non-blocking speak. Put text into the worker queue.
    """
    if not text:
        return
    if not _worker_started:
        # As fallback, do immediate speak (safe at startup before worker)
        speak_now(text)
        return
    print("Wini:", text)
    _tts_queue.put(text)
