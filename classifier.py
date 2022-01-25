# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:40:42 2021

TEAM 1
"""
#author : Mugdha

"""
script for demonstrating grid search to set the parameters of a classifier
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from nltk.corpus import stopwords
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import csv 
from sklearn.model_selection import train_test_split
import pandas as pd

text=[]
jobtitle=[]
text_output=[]

# Reading the Job titles and text from the respective csv
# Open the file in 'r' mode, not 'rb'
csv_file = open('data_scientist.csv','r')
csv_reader= csv.reader(csv_file)
next(csv_reader)

# Split columns while reading
for a, b in csv.reader(csv_file, delimiter=','):
    # Append each variable to a separate list
    jobtitle.append('Data Scientist')
    text.append(b)
    
csv_file1 = open('software_engineer.csv','r')
csv_reader= csv.reader(csv_file1)
next(csv_reader)

# Split columns while reading
for c, d in csv.reader(csv_file1, delimiter=','):
    # Append each variable to a separate list
    jobtitle.append('Software Engineer')
    text.append(d)

# Place the Test csv for testing the classfier here
csv_file3 = open('test.csv','r')
for a in csv.reader(csv_file3, delimiter=','):
    # Append each variable to a separate list
    text_output.append(''.join(a))

#For training and testing on available scrapped data, splitting the scrapped data 
jobtitle_train, jobtitle_test, text_train, text_test = train_test_split(jobtitle,text)


#Build a counter based on the training dataset
counter = CountVectorizer(stop_words=stopwords.words('english'))
counter.fit(text_train)

#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(text_train)#transform the training data
counts_test = counter.transform(text_test)#transform the testing data

#transform the external testing data from line 47 csv
counts_output_test = counter.transform(text_output)

KNN_classifier=KNeighborsClassifier()
LREG_classifier=LogisticRegression(solver='liblinear')
DT_classifier = DecisionTreeClassifier()

predictors=[('knn',KNN_classifier),('lreg',LREG_classifier),('dt',DT_classifier)]

VT=VotingClassifier(predictors)


#=======================================================================================
#build the parameter grid
KNN_grid = [{'n_neighbors': [1,3,5,7,9,11,13,15,17], 'weights':['uniform','distance']}]

#build a grid search to find the best parameters
gridsearchKNN = GridSearchCV(KNN_classifier, KNN_grid, cv=5)

#run the grid search
gridsearchKNN.fit(counts_train,jobtitle_train)

#=======================================================================================

#build the parameter grid
DT_grid = [{'max_depth': [3,4,5,6,7,8,9,10,11,12],'criterion':['gini','entropy']}]

#build a grid search to find the best parameters
gridsearchDT  = GridSearchCV(DT_classifier, DT_grid, cv=5)

#run the grid search
gridsearchDT.fit(counts_train,jobtitle_train)

#=======================================================================================

#build the parameter grid
LREG_grid = [ {'C':[0.5,1,1.5,2],'penalty':['l1','l2']}]

#build a grid search to find the best parameters
gridsearchLREG  = GridSearchCV(LREG_classifier, LREG_grid, cv=5)

#run the grid search
gridsearchLREG.fit(counts_train,jobtitle_train)

#=======================================================================================

VT.fit(counts_train,jobtitle_train)

#use the VT classifier to predict
predicted=VT.predict(counts_test)


#print the accuracy for scrapped testing data
print (accuracy_score(predicted,jobtitle_test))


#Using VT classifier to predict the external testing data
predicted_output = VT.predict(counts_output_test)

#creating a csv for the predicted Job titles for external testing data
submission = pd.DataFrame({'Predicted Job Title': predicted_output})
submission.to_csv('Project_Predicted_Job_Title.csv',index=False)



