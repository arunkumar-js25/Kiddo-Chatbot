import os
import random

import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import speech_recognition as sr

from BotScripts.BotConfiguration import *


# Understand user speech
def Listen():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.

        audio = r1.listen(source, phrase_time_limit=10)  # listen to the source , time_limit [5 secs]
        try:
            result = r1.recognize_google(audio)  # use recognizer to convert our audio into text part.
            # print("You said : {}".format(result))
            # WriteToFile('test.txt',result)
        except:
            result = "Sorry could not recognize your voice"
            # print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly
        return result


def talk(speech):
    # num to rename every audio file
    # with different name to remove ambiguity
    global count
    count = str(random.randrange(1, 1000)) + str(random.randrange(1, 1000))
    # print("-->", speech)
    toSpeak = gTTS(text=speech, lang='en', slow=False)
    # saving the audio file given by google text to speech

    try:
        file = os.getcwd() + config['path']['talkAudio'] + "talk" + count + ".mp3"
        toSpeak.save(file)
    except:
        file = os.getcwd() + config['path']['talkAudio'] + "talk" + count + str(random.randrange(1, 1000)) + ".mp3"
        toSpeak.save(file)

        # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)

# define the audio file
def ReadAudio(Filename):
    audio_file = sr.AudioFile(Filename)
    r = sr.Recognizer()
    with audio_file as source:
       r.adjust_for_ambient_noise(source)
       audio = r.record(source)
    result = r.recognize_google(audio)
    return result