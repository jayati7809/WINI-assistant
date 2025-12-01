# WINI-assistant
🧠 WINI – Desktop Voice Assistant (Offline AI Assistant)

WINI is a fully offline, modular, Python-based voice assistant that can listen, talk, and perform real desktop tasks such as opening apps, fetching weather, taking screenshots, searching Google, playing YouTube, managing reminders, and much more.

It uses SpeechRecognition for listening and pyttsx3 for speaking — no internet required for voice output.

⭐ Features
🎤 Voice Input

Continuous microphone listening

Handles background noise

Fast speech-to-text conversion

Simple, natural voice commands

🔊 Voice Output (Offline TTS)

Uses pyttsx3 with SAPI5

Female voice preference

Smooth, non-blocking audio

No freezing or overlapping

💻 Desktop Automation

Open apps (Notepad, Chrome, Calculator, etc.)

Take screenshots

Show system information

Get date & time

Run Google searches

Play YouTube videos

🌦 Weather Support

Real-time weather using OpenWeather API

City-based temperature, humidity, and condition

📝 Reminder System

Time-based reminders

Countdown reminders

Persistent memory

🌎 Other Tools

Text translation

Location fetching


📁 Project Structure
WINI Assistant/
│
├── main.py
├── listener.py
├── speech_engine.py
├── commands.py
├── apps.py
├── google_search.py
├── weather.py
├── reminder.py
├── screenshot.py
├── system_info.py
├── translator.py
├── location.py
├── wake.py
├── memory.py
│
├── wini_memory.json
├── requirements.txt
└── README.md



2️⃣ Create a virtual environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🌦 4️⃣ Add Your Weather API Key

Create an account at OpenWeatherMap:
https://home.openweathermap.org/users/sign_up

Then open weather.py and paste your API key:

API_KEY = "YOUR_API_KEY_HERE"

🚀 Running WINI

Start the assistant with:

python main.py


You will hear:

Wini: I am online. How can I help you?


WINI immediately begins listening.

🎙️ Sample Voice Commands
🖥️ System Control

“Open Notepad”

“Launch Chrome”

“Take a screenshot”

“Show system information”

🌦 Weather

“What’s the weather in Delhi?”

“Tell me today’s temperature”

🔍 Internet Search

“Search Google for Python tutorials”

“Play lo-fi music on YouTube”

⏰ Reminders

“Remind me to drink water at 5 PM”

“Set a reminder after 10 minutes”

🌍 Other Commands

“Translate hello to Hindi”

“Where am I located?”

🛠️ Customizing App Paths

In apps.py:

APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome":r"chrome.exe",
    "edge": r"msedge.exe"
}
You can add more:

"vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
"word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"

🧠 How WINI Speaks (TTS Engine)

WINI uses a threaded speech engine:

Safe background speaking

Uses a queue

No overlapping voices

No blocking the assistant

So WINI can listen while talking.

🤝 Contributing

Pull requests are welcome!
You can improve modules, add new commands, or enhance UI.

Modular & clean codebase
