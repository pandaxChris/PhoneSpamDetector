#!python3

"""
10/24/20 - Version 1.0 Chris - Added a file converter, voice transcribe through pydub
"""
import speech_recognition as sr
from pydub import AudioSegment
import os
import subprocess

#File converter .M4A to .WAV (Apple Voicemails)
def convertM4AtoWAV(filename):
    if(os.path.exists(filename)):
        removedExtension = filename[ : filename.index(".m4a")]
        newFileName = removedExtension + ".wav"
        try:
           subprocess.call(['ffmpeg', '-i', filename,  newFileName])
           return newFileName
        except:
            print("Failed to convert file")
            return None

    else:
        print("File not found")

#Transcribes the file inside the function
def transcribeAudio(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as src:
        audio = r.record(src)
        print(r.recognize_google(audio))

    
