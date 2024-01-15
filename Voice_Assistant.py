import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio)
            print("User:", query)
            return query.lower()

        except sr.UnknownValueError:
            print("Sorry, I did not hear your request. Can you repeat?")
            return None

    def execute(self, command):
        if "hello" in command:
            self.speak("Hello! How can I assist you today?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            self.speak(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.speak(f"Today's date is {current_date}")

        elif "search" in command:
            search_query = command.replace("search", "")
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            self.speak(f"Searching the web for {search_query}")

        else:
            self.speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    assistant = VoiceAssistant()

    while True:
        command = assistant.listen()

        if command:
            assistant.execute(command)