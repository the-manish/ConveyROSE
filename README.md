# Rose -A Smart Voice Assistant

Rose is a Python-based voice assistant that can perform various tasks, such as playing music, providing information from Wikipedia, searching the web, and more.

## Features

- **Voice Recognition**: Uses Google's Speech Recognition to understand voice commands.
- **Text-to-Speech**: Utilizes pyttsx3 to convert text responses into speech.
- **Task Automation**: Can play music on YouTube, provide the current time, search the web, and more.
- **Web Browsing**: Can open specified websites based on user commands.
- **Language Translation**: Can translate text to English using Google Translate.
- **Calculations**: Can perform basic mathematical calculations.

## Getting Started

### Prerequisites

Imports: The script starts by importing several Python libraries, including:

speech_recognition: For recognizing speech input.
googletrans:The googletrans library is a Python wrapper around Google Translate, which is a machine translation service provided by Google.
pyttsx3: A text-to-speech library for generating speech output.
pywhatkit: A library that allows you to perform various actions, like playing YouTube videos.
datetime: For getting the current time.
wikipedia: To retrieve summaries from Wikipedia.
webbrowser:The webbrowser module is a handy tool for simple web-related tasks in Python, such as opening URLs, displaying HTML content, and more.
pyjokes: For telling jokes.
Initialization: It initializes the necessary components, including setting up the text-to-speech engine and configuring its voice.

talk Function: Defines a function called talk that takes a text input and uses the text-to-speech engine to speak the provided text.

take_command Function: This function captures audio from the microphone and uses Google's speech recognition service (recognize_google) to convert the spoken words into text. If the word "alexa" is detected, it removes it from the command and returns the cleaned-up command as text.

run_rose Function: This function is the core of the voice assistant. It calls take_command to get a user command and then processes it based on certain keywords. Depending on the command, it can do the following:

If the command contains "play," it plays a YouTube video using pywhatkit.playonyt.
If the command contains "time," it tells the current time.
If the command contains "date" it tells the current date.
If the command contains "who the heck is," it looks up and speaks a summary of the mentioned person from Wikipedia.
If the command contains "date," it responds with a humorous message.
If the command is "are you single," it responds with a humorous answer.
If the command contains "joke," it tells a joke using pyjokes.get_joke().
If none of the recognized keywords are present, it asks the user to repeat the command.
Main Loop: The script enters an infinite loop (while True) and repeatedly calls run_rose, essentially waiting for voice commands and responding accordingly.


