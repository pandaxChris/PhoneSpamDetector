#!python3

#test code for transcribe.py


import my_transcribe as t


myFile = t.convertM4AtoWAV("voicemail-446.m4a")
if(myFile is not None):
    t.transcribeAudio(myFile)

