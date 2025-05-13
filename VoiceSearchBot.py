#Open Google Chrome and listen for voice commands to search for something on Google.
# This script uses the SpeechRecognition library to listen for voice commands and Selenium to automate Google searches.
#Listen for you to say something like “search weather today”
#Extract the word(s) after “search”
#Automatically type it into Google and submit the search

import speech_recognition as sr
from selenium import webdriver

class voice:
    
    def _init_(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()
        
    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    
                    if "search" in command:
                        driver = webdriver.Chrome() 
                        driver.get(f"https://www.google.com/search?channel=trow2&client=firefox-b-1-d&q={command.split('search ')[-1]}")
                        
            except sr.UnkownValueError:
                pass
   
listener = voice() 

