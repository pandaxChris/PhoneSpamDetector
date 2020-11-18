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
#		Takes no arguments(ignored if supplied)	 #
#												 #
#												 #
#												 #
##################################################


import os, sys
import conv as con
import pandas as p
import my_transcribe as m
from sklearn.svm import SVC
import directorystuff as di 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def pds():
	if(len(sys.argv[])==3)
	if(not os.path.isdir('./Voicemails')):
		print("No voicemails to test. Exiting...")
		exit(0)

	#check to make sure we have a text file rep of each voicemail file
	vm_dir = os.listdir('./Voicemails')
	for item in vm_dir:
		name_txt = './Voicemails/' + item[:item.rfind('.')] + '.txt'
		if( not os.path.exists(name_txt)):
			print("Checking for files...")
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
	print("SVM accuracy: " + str(accuracy_score(svm_pred, y_test) * 100))


	if(len(sys.argv) == 2): #Two arguments, the file + the param
		stringToTest = ""
		if(sys.argv[1].rfind('.') > -1): #Eval a file
			evalFile = sys.argv[1]

			m.convertM4AtoWAV(evalFile)
			m.transcribeAudio(evalFile)

			fileToTest = open(evalFile[:evalFile.rfind('.')] + '.txt', 'r')
			stringToTest = fileToTest.readline()
			fileToTest.close()
		else: #Eval a string -- Escape the punctuation
			
		result = svm.predict(stringToTest)
		if(result == [1]):
			print("Suspicious...")
		else:
			print("Good file")
pds()

