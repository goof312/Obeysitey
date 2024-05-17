#!C:\Users\Admin\AppData\Local\Programs\Python\Python312\python

import cgi
import sys
import mysql.connector

# iba iba tayo dito
sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/")
from utilities import PredictionModel as PM
from model import MyQueries as MQ


class Controller:
    predictionModel = ""
    form = ""
    AddRec = ""

    def __init__(self):
        self.predictionModel = PM.Prediction()
        self.form = cgi.FieldStorage()
        pass

    def predict(self):
        self.predictionModel.PrintStats()
        # kuha pa ng input sa views
        #SAMPLE PREDICTION AND INPUT
        print(self.predictionModel.Predict([23, "Male", 1.65, 60, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation"]))
    
    # view ------------------------------
    def get_Input(self):
        pass

    def return_Prediction(self):
        # call views na magpapakita ng result
        pass
    
    # model -----------------------------
    def insertRecord(self):
        try:
            # Your existing code here...
            self.AddRec = MQ.AddRecord(23, "Male", 1.65, 60, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation", "Insufficient_Weight")
            self.AddRec.addRecord()
            print("Nadaan dito")
        except mysql.connector.Error as e:
            print("Error:", e)
    
    def get(self):
        # view all inputs
        pass


    



cont = Controller()
cont.predict()
cont.insertRecord()