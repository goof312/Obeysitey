import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
import sys
sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/")
from utilities import InputEnums as en

#inputs
'''
0: Age: Numeric (continuous)
1: Gender: Male, Female; changed to (1,0)
2: Height: Numeric (continuous)
3: Weight: Numeric (continuous) (in kg)
4: CALC: No, Sometimes, Frequently, Always (I do not drink, Sometimes, Frequently, Always) (Consumption of alcohol) changes to (0, 1, 2, 3)
5: FAVC: Yes, No (Frequent consumption of high caloric food) changed to (1, 0)
6: FCVC: 1, 2, 3 (Never, Sometimes, Always) (Consumption of vegetables)
7: NCP: 1, 2, 3 (Between 1 and 2, Three, More than three) (Number of main meals)
8: SCC: Yes, No (Calories consumption monitoring (do you monitor calc)) changed to (1,0)
9: SMOKE: Yes, No changed to (1,0)
10: CH20: 1, 2, 3 (Less than a liter, Between 1 and 2 L, More than 2L)
11: family_history: Yes, No changed to (1,0)
12: FAF: 0, 1, 2, 3 (I do not have, 1 or 2 days, 2 or 4 days, 4 or 5 days) (Physical activity frequency)
13: TUE: 0, 1, 2 (0-2 hours, 3-5 hours, MOre than 5 hours) (Time use technology devices)
14: CAEC: No, Sometimes, Frequently, Always (Consumption of foods between meals) changed to (0, 1, 2, 3)
15: MTRANS: Automobile, Motorbike, Bike, Public_Transportation, Walking changed to (0, 1, 2, 3, 4)

result: NObesity (Target): Insufficient_Weight, Normal_Weight, Overweight_Level_I, Overwieght_Level_II, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III

#'Age','Gender','Height','Weight','CALC','FAVC','FCVC','NCP','SCC','SMOKE','CH2O','family_history_with_overweight','FAF','TUE','CAEC','MTRANS'
test1 = classifier.predict([[23, "Male", 1.65, 49, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation"]])
test1 = classifier.predict([[23, 1, 1.65, 49, 0, 0, 2, 1, 0, 0, 3, 0, 1, 2, 1, 3]])
'''

class Prediction:
    headernames = ['Age','Gender','Height','Weight','CALC','FAVC','FCVC','NCP','SCC','SMOKE','CH2O','family_history_with_overweight','FAF','TUE','CAEC','MTRANS','NObeyesdad']
    #path = "./resources/ObesityDataSet_raw_and_data_sinthetic_PROPERbinned_noheader.csv"
    path = "./resources/ObesityDataSet_raw_and_data_sinthetic_binned_noheader.csv"
    
    result = ""
    X = 0 
    y = 0
    X_train = 0 
    X_test = 0 
    y_train = 0 
    y_test = 0
    y_pred = 0
    classifier = 0
    
    '''
    Initialize Object
    '''
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
        return

    '''
    Void method: Prints Confusion matrix, classification, and accuracy
    '''
    def PrintStats(self): 
        print("Confusion Matrix: ")
        print(self.result)
        result1 = classification_report(self.y_test, self.y_pred)
        print("Classification Report: ",)
        print (result1)
        result2 = accuracy_score(self.y_test,self.y_pred)
        print("Accuracy: ",result2)
        return

    '''
    Parameter: list values containing (in order)
        'Age','Gender','Height','Weight','CALC','FAVC','FCVC','NCP','SCC','SMOKE','CH2O','family_history_with_overweight','FAF','TUE','CAEC','MTRANS'
    Returns:
        string of result
    '''
    def Predict(self, arrayVals):
        arrayVals = self.__convertInputs(arrayVals)
        print(" ".join(map(str, arrayVals)))
        test1 = self.classifier.predict([arrayVals])
        return test1[0] #Returns string of result
    
    #Private method to convert input array
    def __convertInputs(self, arr):
        indGender = 1; indCALC = 4; indFAVC = 5; indSCC = 8; indSmoke = 9; indHistory = 11; indCAEC = 14; indTrans = 15
        arr[indGender] = en.Gender[arr[indGender].lower()]
        print(arr[indGender])
        arr[indCALC] = en.CALC[arr[indCALC].lower()]
        arr[indFAVC] = en.YesNo[arr[indFAVC].lower()]
        arr[indSCC] = en.YesNo[arr[indSCC].lower()]
        arr[indSmoke] = en.YesNo[arr[indSmoke].lower()]
        arr[indHistory] = en.YesNo[arr[indHistory].lower()]
        arr[indCAEC] = en.CAEC[arr[indCAEC].lower()]
        arr[indTrans] = en.MTRANS[arr[indTrans].lower()]
        
        return arr

#####Implementation
#--------------------predictionModel = Prediction()

#--------------------predictionModel.PrintStats()
#SAMPLE PREDICTION AND INPUT
#--------------------print(predictionModel.Predict([23, "Male", 1.65, 60, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation"]))

######input format 
#[23, "Male", 1.65, 60, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation"]
#input order
#'Age','Gender','Height','Weight','CALC','FAVC','FCVC','NCP','SCC','SMOKE','CH2O','family_history_with_overweight','FAF','TUE','CAEC','MTRANS'



###############IGNORE THIS v
#if no enum
#print(predictionModel.Predict([23, 1, 1.65, 60, 0, 0, 2, 1, 0, 0, 3, 0, 1, 2, 1, 3]))

#If using ProperBinned csv
#print(predictionModel.Predict([2, 1, 1, 2, 0, 0, 2, 1, 0, 0, 3, 0, 1, 2, 1, 3]))



