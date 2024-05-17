#!C:\Users\Admin\AppData\Local\Programs\Python\Python312\python

import cgi
import sys
import mysql.connector

# iba iba tayo dito
sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/")
from utilities import PredictionModel as PM


class Controller:
    predictionModel = ""
    form = ""

    def __init__(self):
        self.predictionModel = PM.Prediction()
        self.form = cgi.FieldStorage()
        pass

    def predict(self):
        self.predictionModel.PrintStats()
        #SAMPLE PREDICTION AND INPUT
        print(self.predictionModel.Predict([23, "Male", 1.65, 60, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation"]))


    def insertRecord(self):
        sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")
        from MyQueries import AddRecord
        try:
            # Your existing code here...
            myaddrec =AddRecord(23, "Male", 1.65, 60, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation", "Insufficient_Weight")
            result = myaddrec.addRecord()
            print("Nadaan dito")
        except mysql.connector.Error as e:
            print("Error:", e)



cont = Controller()
cont.predict()
cont.insertRecord()