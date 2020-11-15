########################################
# Author: Zixuan Zeng                  #
# Date: 11/2/2020                      #
# SupportVectorMachine.py              #
# This class is implementation of a    #
# Machine Learning algorithm called    #
# Support Vector Machine which can     #
# Transform any dimension of data set  #
# to a higher dimension for more       #
# accurate and easier classification   #
# using so-called 'hyper-plane'.       # 
# This is a part of Phone Spam Detector#
# Project: to aim a better result of   #
# spam detection.                      #
########################################
from sklearn import svm
import pandas as pd

class SupportVectorMachine:

    # Here to declare the variable called classifier which is using SVM from sklearn
    classifier = svm.SVC()

    # The member function to train/learn the algorithm model
    def train_model(self, training_dataframe):
        classifier.fit(training_dataframe)

    # TO-DO: Should print out the percentage of precision on the testing data set; waiting for actual data frame (cannot hard-code here)
    def test_model(self, testing_dataframe):
        classifier.predict(testing_dataframe)

    # Here this function should predict the spam text message: classify it to spam or non-spam
    def predict_spam(self, spam_dataframe):
        classifier.predict(spam_dataframe)

    # Here is the constructor to initialize every object
    def __init__(self):
        data_frame = pd.read_csv('voicemails.csv', usecols= ['voice_text_tfidf', 'directory', 'label'])
        training_dataframe = data_frame.iloc[0:5,['voice_text_tfidf', 'label']]
        testing_dataframe = data_frame.iloc[5:10,['voice_text_tfidf', 'label']]
        spam_dataframe = data_frame.iloc[10:14,['voice_text_tfidf', 'label']]
        self.train_model(training_dataframe)
        self.test_model(testing_dataframe)
        self.predict_spam(spam_dataframe)
