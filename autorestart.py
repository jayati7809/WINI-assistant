
import time
import os
import sys
from speech_engine import speak

def restart_delay(seconds: int = 2):
    speak(f"Restarting in {seconds} seconds.")
    time.sleep(seconds)
    # Simple restart
    python = sys.executable
    os.execv(python, [python] + sys.argv)
