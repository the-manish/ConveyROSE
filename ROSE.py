import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import math


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'rose' in command:
                command = command.replace('rose', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I did not get that. Please repeat.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    return command



def run_rose():
    
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'hi' in command:
        talk('Hello! How can I assist you today?')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        talk(f'Searching for {search_query} on Google.')
        google_search_url = f'https://www.google.com/search?q={search_query}'
        webbrowser.open(google_search_url)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        talk('Today\'s date is ' + date)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'open' in command and 'website' in command:
        # Extract the website name from the command
        website_name = command.replace('open', '').replace('website', '').strip()
        # Map the website name to its URL
        website_urls = {
            'google': 'https://www.google.com',
            'bing': 'https://www.bing.com',
            'linkedin':'https://www.linkedin.com',
            'github':'https://www.github.com',
            # Add more websites as needed
        }
        if website_name.lower() in website_urls:
            webbrowser.open(website_urls[website_name.lower()])
            talk(f'Opening {website_name}.')
        else:
            talk(f'Sorry, I don\'t know how to open {website_name}.')
    elif 'calculate' in command:
        # Extract the mathematical expression
        expression = command.replace('calculate', '').strip()
        try:
            # Evaluate the mathematical expression
            result = eval(expression)
            talk(f'The result of {expression} is {result}.')
        except Exception as e:
            print(f"Error performing calculation: {e}")
            talk("Sorry, I couldn't perform the calculation.")
    
    elif 'translate' in command:
        # Extract the text to be translated
        text_to_translate = command.replace('translate', '').strip()

        # Initialize the Translator
        translator = Translator()

        # Detect the language of the input text
        detected_language = translator.detect(text_to_translate).lang

        # Translate the text to English (you can change 'en' to the desired target language)
        translated_text = translator.translate(text_to_translate, dest='en').text

        talk(f'The detected language is {detected_language}. Translated text: {translated_text}')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('Stopping rose')
        exit()

        
    else:
        talk('Please say the command again.')


while True:
    run_rose()
