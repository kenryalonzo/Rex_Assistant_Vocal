
import sys
import os
import datetime

import speech_recognition as sr
import pywhatkit as what
import wikipedia
import random


from gtts import gTTS
import pygame
from pygame import mixer

listener = sr.Recognizer()

def talk(text: str, lang: str = "fr", slow: bool = False):
    """
    Crée un fichier audio MP3 à partir du texte et le lit à l'aide de Pygame.

    Args:
        text (str): Le texte à convertir en audio.
        lang (str): La langue du texte (défaut: "fr").
        slow (bool): Si True, la voix sera plus lente (défaut: False).
    """

    # Générer le fichier audio
    tts = gTTS(text=text, lang=lang, slow=slow)
    filename = "voix.mp3"
    tts.save(filename)

    # Initialiser Pygame
    mixer.init()

    # Lire le fichier audio
    mixer.music.load(filename)
    mixer.music.play()

    # Attendre la fin de la lecture
    while mixer.music.get_busy():
        pygame.time.wait(100)

    # Supprimer le fichier audio (optionnel)
    os.remove(filename)

def greetme():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        talk("Bonjour Admin")
    
    if 12 <= current_hour < 18:
        talk("Bon apres-midi Admin")
        
    if current_hour >= 18 and current_hour != 0:
        talk("Bonsoir Admin")

greetme()
talk("Comment tu vas?")

def root_command():
    with sr.Microphone() as source:
        print("listening...")
        listener.pause_threshold = 2
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language = "fr-FR")
        command = command.lower()
        print(command)
        
        if "rex" in command:
            command = command.replace("rex", "")
            print(command)
    return command


def run_Root():
    command = root_command()
    if "musique" in command:
        song = command.replace("musique", "")
        talk("musique en cour ...")
        what.playonyt(song)
        
    elif "heure" in command:
        time = datetime.datetime.now().strftime("%H:%m")
        print (time)
        talk("il est actuellement: " + time, "au Cameroun")
        
    elif "qui est" in command:
        person = command.replace("qui est", "")
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
        talk(info)
        
    elif "sortir avec" in command:
        talk("je suis un peu souffrante en ce moment.")
        
    elif "es tu en couple" in command:
        talk("Non non non, mon coeur est encore a conquerir")
        
    elif "blague" in command:
        jokes = [
            "Que dit une noisette quand elle tombe dans l'eau ? Je me noix.",
            "Comment est-ce que les abeilles communiquent entre elles ? Par -miel.",
            "Quel est l'arbre préféré du chômeur ? Le bouleau.",
            "Qu'est-ce qu'une frite enceinte ? Une patate sautée.",
            " Que dit une mère à son fils geek quand le dîner est servi ? Alt Tab !"
        ]
        talk(random.choice(jokes))
        
    elif "et toi" in command:
        msgs = ["Je fais juste mon truc !", "Je vais bien merci !", "Bien merci !", "Je vais bien et toi?", "T'inquiete pas pour moi tout roule", "Je suis tranquile merci", "Jout beigne", "Je suis pose donc t'inquietes pas", "Je suis au calme"]
        talk(random.choice(msgs))
        
    elif "desactive toi" or "extension" or "Je te rappele" or "vas en veille" in command:
        talk("Ce fut un plaisir d'avoir pu t'aider root rappele-moi quand tu veux ")
        sys.exit()
        
    else:
        talk("Pourais tu repeter, je n'ai pas bien compris")

if __name__ == '__main__':
    while True:
        run_Root()

