#!C:\Users\Admin\AppData\Local\Programs\Python\Python312\python

import cgi
import sys
import mysql.connector

# iba iba ata tayo dito
sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/")
from utilities import PredictionModel as PM
from model import MyQueries as MQ


class Controller:
    predictionModel = ""
    form = ""
    AddRec = ""
    GetRec = ""

    def __init__(self):
        self.predictionModel = PM.Prediction()
        self.form = cgi.FieldStorage()
        return

    # view ------------------------------
    def get_Input(self):
        '''
        u_Age = self.form.getvalue("u_Age")
        u_Gender = self.form.getvalue("u_Gender")
        u_Height = self.form.getvalue("u_Height")
        u_Weight = self.form.getvalue("u_Weight")
        u_CALC = self.form.getvalue("u_CALC")
        u_FAVC = self.form.getvalue("u_FAVC")
        u_FCVC = self.form.getvalue("u_FCVC")
        u_NCP = self.form.getvalue("u_NCP")
        u_SCC = self.form.getvalue("u_SCC")
        u_SMOKE = self.form.getvalue("u_SMOKE")
        u_CH20 = self.form.getvalue("u_CH20")
        u_family_history = self.form.getvalue("u_family_history")
        u_FAF = self.form.getvalue("u_FAF")
        u_TUE = self.form.getvalue("u_TUE")
        u_CAEC = self.form.getvalue("u_CAEC")
        u_MTRANS = self.form.getvalue("u_MTRANS")
        '''
        u_Age = 23
        u_Gender = "Male"
        u_Height = 1.65
        u_Weight = 60
        u_CALC = "No"
        u_FAVC = "No"
        u_FCVC = 2
        u_NCP = 1
        u_SCC = "No"
        u_SMOKE = "No"
        u_CH20 = 3
        u_family_history = "No"
        u_FAF = 1
        u_TUE = 2
        u_CAEC = "Sometimes"
        u_MTRANS = "Public_Transportation"
        return [u_Age, u_Gender, u_Height, u_Weight, u_CALC, u_FAVC, u_FCVC, u_NCP, u_SCC, u_SMOKE, u_CH20, u_family_history, u_FAF, u_TUE, u_CAEC, u_MTRANS]

    def predict(self):
        # self.predictionModel.PrintStats()
        inputs = self.get_Input()
        result = self.predictionModel.Predict(inputs)
        return(result)
    
    # model -----------------------------
    def insertRecord(self, result):
        inputs = self.get_Input()

        try:
            self.AddRec = MQ.AddRecord(*inputs, result)
            self.AddRec.addRecord()
            print("Added Record")
        except mysql.connector.Error as e:
            print("Error:", e)

    def getRecomendation(self, category):
        myrecomendation = MQ.GetMYrecomendation(category)
        results = myrecomendation.getRec()
        print(results)
        # send sa views

# sunod-sunod
cont = Controller()
a = cont.predict()
print("Result: " + a)
cont.insertRecord(a)
cont.getRecomendation(a)

'''
arr = ['1', 2, 3, "33"]
print(arr)
print(*arr)
'''