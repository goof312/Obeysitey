#!C:\Users\jolay\AppData\Local\Programs\Python\Python312\python
#"C:\Users\MateBook D15\AppData\Local\Programs\Python\Python311\python"
#C:\Users\jetje\AppData\Local\Programs\Python\Python311\python
print("Content-Type: text/html")
print()     

import cgi
import sys
import mysql.connector

sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/")
from utilities import PredictionModel as PM
from model import MyQueries as MQ
from view import TestPage as TP
from view import ResultPage as RP
from view import DataPage as DP
from view import DataSetPage as DSP


form = cgi.FieldStorage()

takeTestBtn = form.getvalue("TAKE")
sendTestBtn = form.getvalue("send")
backBtn = form.getvalue("back")
dataBtn = form.getvalue("dataList")
datasetBtn = form.getvalue("dataset")


class Controller():
    predictionModel = ""
    AddRec = ""
    GetRec = ""

    def __init__(self):
        self.predictionModel = PM.Prediction()
        return

    # view ------------------------------
    def get_Input(self):
        return [
            float(form.getvalue("age")),
            form.getvalue("gender"),
            float(form.getvalue("height")),
            float(form.getvalue("weight")),
            form.getvalue("CALC"),
            form.getvalue("FAVC"),
            int(form.getvalue("FCVC")),
            int(form.getvalue("NCP")),
            form.getvalue("SCC"),
            form.getvalue("SMOKE"),
            int(form.getvalue("CH2O")),
            form.getvalue("family_history"),
            int(form.getvalue("FAF")),
            int(form.getvalue("TUE")),
            form.getvalue("CAEC"),
            form.getvalue("MTRANS")
        ]
    
    def predict(self):
        # self.predictionModel.PrintStats()
        inputs = self.get_Input()
        print('<script> console.log("here"); </script>')

        result = self.predictionModel.Predict(inputs)
        return result
    
    def insertRecord(self, result):
        inputs = self.get_Input()
        try:
            self.AddRec = MQ.AddRecord(*inputs, result)
            self.AddRec.addRecord()
            print('<script> console.log("Added Record"); </script>')
        except mysql.connector.Error as e:
            print("Error:", e)

    def getRecommendation(self, category):
        myrecomendation = MQ.GetMYrecomendation(category)
        results = myrecomendation.getRec()
        #print(results)
        return results
        # send sa views


# main =====================================================================
cont = Controller()

# take test  
if str(takeTestBtn)!="None":
    print('<script> console.log("Test Button is pressed"); </script>') 
    view_TestPage = TP.MyTestPageView()
    view_TestPage.viewAddRecordTestpage()

# submit test 
if str(sendTestBtn)!="None":
    print('<script> console.log("Predict"); </script>')
    prediction = cont.predict()
    print('<script> console.log("Recommend"); </script>')
    recommendation = cont.getRecommendation(prediction)
    print('<script> console.log("Insert"); </script>')
    cont.insertRecord(prediction)

    line = ("".join(map(str, recommendation)))
    line = line.replace(r"\r\n", "")
    line = line.replace(r"\xf0\x9f\x8e\x89", "")
    line = line.replace(r"\xe2\x89\xa5", "")
    line = line.replace("\\'", "'")
    
    viewResult = RP.MyTestPageView(line)
    viewResult.viewResultPage()

# back button
if str(backBtn)!="None":
    redirectURL = "http://localhost/Obeysitey/Obeysitey/home.html"
    print ('<script type="text/javascript">window.location ="' + redirectURL + '";</script>')
    print("Petmalu")

# data button
if str(dataBtn)!="None":
    query1 = MQ.GetAllRecords()
    results= query1.showAll()
    view1=DP.MyDataPageView(results)
    view1.viewDataPage()

if str(datasetBtn) != "None":
    view1=DSP.MyDataSetPageView()
    view1.viewDataPage()






# wala lang
'''
cont = Controller()
a = cont.predict()
print("Result: " + a)
cont.insertRecord(a)
cont.getRecomendation(a)

arr = ['1', 2, 3, "33"]
print(arr)
print(*arr)
'''