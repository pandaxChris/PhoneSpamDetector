#!python3

"""
10/24/20 - Version 1.0 Chris - Added a file converter, voice transcribe through pydub
11/10/20 - V1.1 Chris - Refactored some code to function with other modules
"""
import speech_recognition as sr
from pydub import AudioSegment
import os
import subprocess

#File converter .M4A to .WAV (Apple Voicemails)
def convertM4AtoWAV(filename):
    if(os.path.exists(filename)):
        newFileName = filename
        if(filename.find(".wav") ==  -1 ):
            removedExtension = filename[ : filename.rfind(".")]
            newFileName = removedExtension + ".wav"
            print(newFileName)
        try:
           subprocess.call(['ffmpeg', '-i', filename,  newFileName, "-loglevel", "quiet"])
           return newFileName
        except:
            print("Failed to convert file")
            return None

    else:
        print("File not found")

#Transcribes the file inside the function
#Creates a new file of the filename with [original file name without extension].txt
def transcribeAudio(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as src:
        audio = r.record(src)
        #print(r.recognize_google(audio))
        data = r.recognize_google(audio)
        removedExtension = filename[ : filename.rfind(".wav")]
        newFileName =  removedExtension + ".txt"
        f = open(newFileName, 'w')
        f.write(data)
        f.close()
    
