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
    def train_model(training_dataframe):
        classifier.fit(training_dataframe)

    # TO-DO: Should print out the percentage of precision on the testing data set; waiting for actual data frame (cannot hard-code here)
    def test_model(testing_dataframe):
        classifier.predict(testing_dataframe)

    # Here this function should predict the spam text message: classify it to spam or non-spam
    def predict_spam(spam_text_file):
        classifier.predict(spam_text_file)

    # Here is the constructor to initialize every object
    def __init__(self):
        self.train_model(training_dataframe)
        self.test_model(testing_dataframe)
        self.predict_spam(spam_text_file)