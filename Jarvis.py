from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def talk(text):
     engine.say(text)
     engine.runAndWait()

def take_command():
     try:
        with sr.Microphone() as source:
           print("listening...")
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower()
           if 'Jarvis' in command:
             command = command.replace('Jarvis','')
             print(command)
        
     except:
             print("Sorry....Did'nt recognize you sir")
     return command



def run_jarvis():
     command = take_command()
     print(command)
     if 'play' in command:
          song = command.replace('play','')
          talk('Playing'+ song)
          pywhatkit.playonyt(song)
     
     elif 'time' in command:
          time = datetime.datetime.now().strftime('%I:%M:%p')
          talk('Current time is '+ time)

     elif 'tell me something about' in command:
          person = command.replace('Tell me something about','')
          info = wikipedia.summary(person,1)
          print(info)
          talk('According to wikipedia'+ info)

     elif 'date' in command:
          talk('Sorry I am busy a little bit')
     elif 'Are you single' in command:
          talk('Sorry Sir, I am in a relationship with wifi right now')
     elif 'Do you know me' in command:
          talk('Yes Sir....Your name is Arjun and you are very nice')   
     else:
          talk('Please repeat the command....did not get you sir') 
    
while True:
    run_jarvis()          

