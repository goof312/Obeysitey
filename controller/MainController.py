#!C:\Users\Admin\AppData\Local\Programs\Python\Python312\python

import cgi
import sys
# iba iba tayo dito
sys.path.append("C:/xampp/htdocs/Obeysity/Obeysitey/")
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

cont = Controller()
cont.predict()