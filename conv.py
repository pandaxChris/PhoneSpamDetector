#! python3

import sys
import os
import subprocess
import speech_recognition as sr
from pydub import AudioSegment
import my_transcribe as t

#script to convert and transcribe multiple files at a time.
#no error checking was added to subject to vulernabilities and exceptions

def convertAndTranscribe():
    method = sys.argv[1]
    for f in sys.argv:
        if( f is method ):
            continue
        else:
            myFile = t.convertM4AtoWAV( f ) 
            if(myFile is not None):
                t.transcribeAudio(myFile)

