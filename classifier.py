#!/usr/bin/python3

##Just some random code to play around with our data on nb/svm and learn how to use
#Not implemented in the program model that we wrote

from numpy import mean
import pandas as p
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import svm, naive_bayes
from sklearn.metrics import accuracy_score

my_csv = p.read_csv('voicemails.csv', names=['voice_text_tfidf', 'directory', 'label'])

#Change status' to 0s and 1s
my_csv.loc[my_csv['label']=='Good', 'label'] = 0
my_csv.loc[my_csv['label']=='Bad', 'label'] = 1

#print(my_csv)
my_csv_x = my_csv['voice_text_tfidf']
my_csv_y = my_csv['label']
x_train, x_test, y_train, y_test = train_test_split(my_csv_x, my_csv_y, test_size = 0.2)
y_train = y_train.astype(int)
y_test=y_test.astype(int)

#Fit the model with data
tfid_vec = TfidfVectorizer(stop_words='english', use_idf=True)
#x_test=x_test[:len(x_test)-1]
#y_test=y_test[:len(y_test)-1]
tfid_vec.fit(x_train)

train_x_tfidf= tfid_vec.transform(x_train)
test_x_tdidf = tfid_vec.transform(x_test)

#########Naive Bayes attempt#########
n = naive_bayes.MultinomialNB()
n.fit(train_x_tfidf, y_train)

n_pred = n.predict(test_x_tdidf)
acc = accuracy_score(n_pred, y_test, normalize=False)
print("Naive Bayes accuracy: " + str(acc * 100))
#print(accuracy_score(n_pred, y_test) * 100)

########Below is SVM code#############

svm = SVC()  #RBF kernel
svm.fit(train_x_tfidf, y_train)

svm_pred = svm.predict(test_x_tdidf)

if(svm_pred.all()==[1]):
	print("Spam")

print("SVM accuracy: " + str(accuracy_score(svm_pred, y_test)* 100) + "%")



"""
accuracies = []

for i in range(1000):
	x_train, x_test, y_train, y_test = train_test_split(my_csv_x, my_csv_y, test_size = 0.5)
	test_x_tdidf = tfid_vec.transform(x_test)
	accuracies.append(svm.predict(test_x_tdidf))


print("Our average over running randomized testing in 1000 runs is: "  + str(mean(accuracies)))

"""
