#!/usr/bin/python3

##########################################
#  Chris Li                              #
#  11/10/20 1.0: File Creation and added #
#                                        #
#                                        #
#  This file contains all the necessary  #
#  tools to classify our data using      #
#  the sklearn library.                  #
#                                        #
#                                        #
#                                        # 
##########################################

import pandas as p
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

my_csv = p.read_csv('attempt.csv', names=['Data', 'File', 'Status'])

#print( my_csv.head( len(my_csv) ) )

#Change status' to 0s and 1s
my_csv.loc[my_csv['Status']=='Good', 'Status'] = 1
my_csv.loc[my_csv['Status']=='Bad', 'Status'] = 0

#print( my_csv.head( len(my_csv) ) )

my_csv_x = my_csv['Data']
my_csv_y = my_csv['Status']

my_cv = CountVectorizer()

x_train, x_test, y_train, y_test =train_test_split(my_csv_x, my_csv_y, test_size = 0.2, random_state = 4)
xtrain_cv = my_cv.fit_transform(x_train)

a=xtrain_cv.toarray()

#print(my_cv.inverse_transform(a[3]))
