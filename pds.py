#!/usr/bin/python3

##################################################
#	CLI tool for demo							 #
#	What it does								 #
#		Runs NB and SVM on voicemail audio 		 #
#		files to determine if it's a potential	 #
#		phishing voicemail						 #
#												 #
#	How to run:									 #
#		./pds.py								 #
#		Takes one argument at most - string or	 #
#		audio file to test						 #
#		Only works for .m4a, .wav, and .mp3 for  #
#		now.									 #
##################################################

import os, sys
import pandas as p
import subprocess
import my_transcribe as m
from sklearn.svm import SVC
import directorystuff as di 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def pds():
	#check to make sure we have a text file rep of each voicemail file
	vm_dir = os.listdir('./Voicemails')
	for item in vm_dir:
		name_txt = './Voicemails/' + item[:item.rfind('.')] + '.txt'
		if( not os.path.exists(name_txt)):
			print(name_txt)
			print("Missing some files... Converting...")
			di.transcribeDirectory('./Voicemails/')
			break


	#Get csv of our existing text files:
	if(not os.path.exists('voicemails.csv')):
		print("Checking for voicemail csv file...")
		di.getCSVofData('./Voicemails/', 'voicemails.csv')


	my_csv = p.read_csv('voicemails.csv', names=['voice_text_tfidf', 'directory', 'label'])

	#Change labels to 0s and 1s
	my_csv.loc[my_csv['label']=='Good', 'label'] = 0
	my_csv.loc[my_csv['label']=='Bad', 'label'] = 1

	my_csv_x = my_csv['voice_text_tfidf']
	my_csv_y = my_csv['label']
	x_train, x_test, y_train, y_test = train_test_split(my_csv_x, my_csv_y, test_size = 0.5, random_state = 3)
	y_train = y_train.astype(int)
	y_test = y_test.astype(int)

	#Fit the model with data
	tfid_vec = TfidfVectorizer(stop_words='english', use_idf=True)

	tfid_vec.fit(x_train)
	train_x_tfidf= tfid_vec.transform(x_train)
	test_x_tdidf = tfid_vec.transform(x_test)

	#Create our SVM classifier to get an understanding of accuracy
	svm = SVC()
	svm.fit(train_x_tfidf, y_train)

	svm_pred = svm.predict(test_x_tdidf)


	print("Testing accuracy on test data...")
	print("SVM accuracy: " + str(accuracy_score(svm_pred, y_test) * 100) + '%')


	if(len(sys.argv) == 2): #Two arguments, the file + the param
		stringToTest = ""
		extensions = ['.m4a', '.wav', '.mp3']
		if(sys.argv[1][sys.argv[1].rfind('.'):] in extensions): #Eval a file
			evalFile = sys.argv[1]

			#Make sure it's not a text file
			if(sys.argv[1].rfind('txt') == -1):
				subprocess.call(['./conv.py', evalFile])
			#print(evalFile[:evalFile.rfind('.')] + '.txt')
			fileToTest = open(evalFile[:evalFile.rfind('.')] + '.txt', 'r')
			stringToTest = fileToTest.readline()
			fileToTest.close()
		else: #Eval a string -- Escape the punctuation
			if(sys.argv[1].rfind('.txt')):
				stringToTest = open(sys.argv[1],'rb').readLline()
			else:
				stringToTest = sys.argv[1]

		t = tfid_vec.transform([stringToTest])
		result = svm.predict(t)
		if(result == [1]):
			print("Suspicious...")
		else:
			print("Good file")
pds()

