########################################
# Author: Zixuan Zeng                  #
# Date: 11/2/2020                      #
# NaturalLanguageProcessing.py         #
# This class is implementation of a    #
# NLP processing including tagging     #
# stop words in english, extracting    #
# features and finally compute the     #
# term-frequency-inverse-document-     #
# frequency for later classification   #
# use.                                 #
########################################

import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import os

class NaturalLanguageProcessing:

    # Here is the main function to call:
    def nlp():
        dir_file = os.getcwd() # returns path to current directory
        files_dir = os.listdir(dir_file)  # list of files in current directory
        text_files = [f for f in files_dir if f.endswith('txt')]
        phone_call_file = text_files[0]
        fid = open(phone_call_file)
        phone_call_df = pd.read_fwf(phone_call_file)  # Pandas Data frame function: read fixed-width text file
        voicemail_df = pd.read_csv('voicemails.csv', usecols= ['voice_text', 'directory', 'label'])
        # Now use CountVectorizer to create vactor space model for each phone call text:
        vect = CountVectorizer(stop_words = 'english',lowercase = True, max_features = 1000)
        counter = vect.fit_transform(voicemail_df["voice_text"])
        transf  = TfidfTransformer(norm = 'l2', sublinear_tf = True)
        tf_idf = transf.fit_transform(counter)  # matrix representation of each phone call text as a tf-idf vector

    # Here is the constructor:
    def __init__(self):
        self.nlp()