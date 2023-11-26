import speech_recognition as sr
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

def get_weather(city):
    try:
        # OpenWeatherMap API endpoint for current weather
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}'
        response = requests.get(url)
        weather_data = response.json()

        # Extract relevant weather information
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']

        talk(f'The current weather in {city} is {description}. The temperature is {temperature} degrees Celsius.')
    except Exception as e:
        print(f"Error fetching weather information: {e}")
        talk("Sorry, I couldn't fetch the weather information.")



def run_rose():
    
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
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
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('Stopping rose')
        exit()

        
    else:
        talk('Please say the command again.')


while True:
    run_rose()
