#!usr/bin/python3

##########################################
#  Chris Li                              #
#  11/10/20 1.0: File Creation and added #
#                                        #
#                                        #
#  This file contains functions to help  #
#  convert our files for usage in our    #
#  machine learning                      #
#                                        # 
#  For simplicity of this module, we     #
#  chose to ignore input validation      #
#                                        #
#                                        #
##########################################

import os
import csv
import subprocess

def transcribeDirectory(myDir='.'):
	voicemails = os.listdir(myDir)
	toConvert = ['./conv.py']

	for item in voicemails:
		if(item[item.rfind('.'):] == '.mp3'):
			continue
		file_no_ext= myDir + item[:item.rfind('.')]
		if(item.lower().find('.m4a') > -1 or item.lower().find('.wav') > -1 and not os.path.exists(file_no_ext+'.txt')):
			toConvert.append('./Voicemails/' + item)

	print("Transcribing directory: " + myDir)

	subprocess.call(toConvert)

	print("Done transcribing the directory: " + myDir)


#Get a CSV of all our data
#Outputs a file with each row following the format:
#[Data in File, fileName, 'Good'/'Bad']
def getCSVofData(myDir='.', outputFile = 'default.csv'):
	
	if(outputFile.rfind('.csv') == -1):
		exit()

	filesInDir = os.listdir(myDir)
	myData = []

	for item in filesInDir:
		if(item.lower().rfind('.txt') > -1):
			myData.append(myDir + item)
	print(myData)
	with open(outputFile, 'w') as csvfile:
		myWriter = csv.writer(csvfile)
		myWriter.writerow(['Message', 'Directory', 'Status'])
		for item in myData:
			f = open(item, 'r')
			status = ""
			data = f.read() 			#All the data in the files are stored in one line
			f.close()

			if(item.find('legit')>-1):
				status = "Good"
			else:
				status = "Bad"

			myWriter.writerow( [ data, item, status ] )

		csvfile.close()



#transcribeDirectory('./Voicemails/')
#getCSVofData('./Voicemails/', 'voicemails.csv')
