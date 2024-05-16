import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

#path = "ObesityDataSet_raw_and_data_sinthetic_binned_noheader.csv"

#inputs
'''
Age: Numeric (continuous)
Gender: Male, Female; changed to (1,0)

Height: Numeric (continuous)
Weight: Numeric (continuous) (in kg)
CALC: No, Sometimes, Frequently, Always (I do not drink, Sometimes, Frequently, Always) (Consumption of alcohol) changes to (0, 1, 2, 3)
FAVC: Yes, No (Frequent consumption of high caloric food) changed to (1, 0)
FCVC: 1, 2, 3 (Never, Sometimes, Always) (Consumption of vegetables)
NCP: 1, 2, 3 (Between 1 and 2, Three, More than three) (Number of main meals)
SCC: Yes, No (Calories consumption monitoring (do you monitor calc)) changed to (1,0)
SMOKE: Yes, No changed to (1,0)
CH20: 1, 2, 3 (Less than a liter, Between 1 and 2 L, More than 2L)
family_history: Yes, No changed to (1,0)
FAF: 0, 1, 2, 3 (I do not have, 1 or 2 days, 2 or 4 days, 4 or 5 days) (Physical activity frequency)
TUE: 0, 1, 2 (0-2 hours, 3-5 hours, MOre than 5 hours) (Time use technology devices)
CAEC: No, Sometimes, Frequently, Always (Consumption of foods between meals) changed to (0, 1, 2, 3)
MTRANS: Automobile, Motorbike, Bike, Public_Transportation, Walking changed to (0, 1, 2, 3, 4)

NObesity (Target): Insufficient_Weight, Normal_Weight, Overweight_Level_I, Overwieght_Level_II, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III


#'Age','Gender','Height','Weight','CALC','FAVC','FCVC','NCP','SCC','SMOKE','CH2O','family_history_with_overweight','FAF','TUE','CAEC','MTRANS'
test1 = classifier.predict([[23, "Male", 1.65, 49, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation"]])

test1 = classifier.predict([[23, 1, 1.65, 49, 0, 0, 2, 1, 0, 0, 3, 0, 1, 2, 1, 3]])

'''


class Prediction:
    headernames = ['Age','Gender','Height','Weight','CALC','FAVC','FCVC','NCP','SCC','SMOKE','CH2O','family_history_with_overweight','FAF','TUE','CAEC','MTRANS','NObeyesdad']
    #path = "ObesityDataSet_raw_and_data_sinthetic_PROPERbinned_noheader.csv"
    path = "ObesityDataSet_raw_and_data_sinthetic_binned_noheader.csv"
    
    result = ""
    X = 0 
    y = 0
    X_train = 0 
    X_test = 0 
    y_train = 0 
    y_test = 0
    y_pred = 0
    classifier = 0
    
    def __init__(self):
        dataset = pd.read_csv(self.path, names=self.headernames)
        dataset.head() #organic data

        self.X = dataset.iloc[:, :-1].values
        self.y = dataset.iloc[:, 16].values

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.30)

        self.classifier = GaussianNB()
        self.classifier.fit(self.X_train, self.y_train) 

        self.y_pred = self.classifier.predict(self.X_test)
        self.result = confusion_matrix(self.y_test, self.y_pred)

    def PrintStats(self): #just for debugging
        print("Confusion Matrix: ")
        print(self.result)
        result1 = classification_report(self.y_test, self.y_pred)
        print("Classification Report: ",)
        print (result1)
        result2 = accuracy_score(self.y_test,self.y_pred)
        print("Accuracy: ",result2)

    def Predict(self, arrayVals):
        test1 = self.classifier.predict([arrayVals])
        return test1
        

predictionModel = Prediction()
#'Age','Gender','Height','Weight','CALC','FAVC','FCVC','NCP','SCC','SMOKE','CH2O','family_history_with_overweight','FAF','TUE','CAEC','MTRANS'

predictionModel.PrintStats()
print(predictionModel.Predict([23, 1, 1.65, 60, 0, 0, 2, 1, 0, 0, 3, 0, 1, 2, 1, 3]))
#print(predictionModel.Predict([2, 1, 1, 2, 0, 0, 2, 1, 0, 0, 3, 0, 1, 2, 1, 3]))



