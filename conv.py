#!/usr/bin/python3

import sys
import os
import subprocess
import csv
import speech_recognition as sr
from pydub import AudioSegment
import my_transcribe as t

#script to convert and transcribe multiple files at a time.
#no error checking was added to subject to vulernabilities and exceptions

def convertAndTranscribe():
    createdFiles = []
    for f in sys.argv:
        if( f.find(".py") > -1): #ignore method + script name
            continue
        else:
            myFile = f
            if(f.find(".m4a") > -1 or f.find('.mp3') > -1):
                print("Converting " + f + " . . .")
                myFile = t.convertM4AtoWAV( f )
                createdFiles.append(myFile)
            print(" ==== Finished converting " + f + " to .wav ====")
            if(myFile is not None):
                print("Transcribing " + f + " . . .")
                t.transcribeAudio(myFile) 
                print(" ==== Finished transcribing. ====")

    cleanupFiles(createdFiles)

def cleanupFiles(arr):
    for i in arr:
        os.remove(i)



convertAndTranscribe()

