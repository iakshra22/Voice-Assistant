# 🎙️ Voice Assistant in Python

Welcome to your very own **Voice-Controlled AI Assistant**, built using Python!  
It can interact with you using your microphone, respond using text-to-speech, and carry out useful commands like searching the web, adjusting volume, telling jokes, and more.

---

## 💡 Features

- 🎧 **Voice-controlled interface**
- 🔍 Search on **Wikipedia** 
- 🌐 Open websites like **Google**, **YouTube**, **Instagram**, and **ChatGPT**
- 🔊 Adjust system **volume** (up, down, mute, unmute, full)
- 💡 Adjust **brightness** (if supported by OS/hardware)
- 😂 Tell random **jokes** using `pyjokes`
- ⏰ Tell the **current time**
- 💬 Responds to greetings

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Libraries:**
  - `pyttsx3` – text-to-speech
  - `speech_recognition` – voice input
  - `wikipedia` – search and fetch summaries
  - `pyautogui` – simulate keyboard keys (volume, brightness)
  - `pyjokes` – generate random jokes
  - `datetime` – time-based greetings and clock
  - `webbrowser` – open web pages 

---

## ⚙️ Setup Instructions

1. **Install the dependencies:**

   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia pyautogui pyjokes pyaudio
   ```

   > **Note:** If you face issues with `pyaudio`, use:
   > - On Windows: `pip install pipwin` then `pipwin install pyaudio`
   > - On Mac/Linux: You may need to install portaudio via Homebrew or apt.

2. **Make sure you have a microphone and speaker connected.**

3. **Run the script:**

   ```bash
   python your_assistant_script.py
   ```

---

## 🎙️ How to Use

Once the script runs:

- The assistant greets you based on time of day.
- You can **speak** commands like:
  - “Open Google”
  - “Search Python on Wikipedia”
  - “Volume up”
  - “Tell me a joke”
  - “What time is it?”
- To stop it, simply close the terminal or stop the script manually.

---

## 🤖 Sample Commands

| Command              | What It Does                       |
|----------------------|------------------------------------|
| "Open Google"        | Launches google.com in browser     |
| "Wikipedia Python"   | Reads summary of Python from Wiki  |
| "Volume up/down"     | Adjusts your system volume         |
| "Mute" / "Unmute"    | Mutes or unmutes audio             |
| "Tell me a joke"     | Responds with a funny joke         |
| "Current time"       | Speaks current system time         |

---

## 📌 Notes

- Works best in a quiet environment for accurate voice recognition.
- This is a console-based assistant, no GUI involved.
- Brightness control may not work on all systems (depends on OS support).

---

## 📎 Thankyou so much:

Feel free to use, share, and improve this voice assistant. Contributions are welcome!

