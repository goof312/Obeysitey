#!C:\Users\jolay\AppData\Local\Programs\Python\Python312\python
print("Content-Type: text/html")
print()     
import cgi
import sys




form = cgi.FieldStorage()

#so these are data we posted from index 
getALL=form.getvalue("ALL")
searchName=form.getvalue("name")
takeTestBtn=form.getvalue("TAKE")

#so these are data we posted from HTML Design MyAddRecordBoostrap
sendTestBtn=form.getvalue("send")
backHomefromBootStrapDesign=form.getvalue("back")

postedID=form.getvalue("studid")
postedName=form.getvalue("studname")
postedAge=form.getvalue("age")
postedDegree=form.getvalue("degree")

# posted test values ================================================================
posted_Age = form.getvalue("age")
posted_Gender = form.getvalue("gender")
posted_Height = form.getvalue("height")
posted_Weight = form.getvalue("weight")
posted_CALC = form.getvalue("CALC")
posted_FAVC = form.getvalue("FAVC")
posted_FCVC = form.getvalue("FCVC")
posted_NCP = form.getvalue("NCP")
posted_SCC = form.getvalue("SCC")
posted_SMOKE = form.getvalue("SMOKE")
posted_CH20 = form.getvalue("CH2O")
posted_family_history = form.getvalue("family_history")
posted_FAF = form.getvalue("FAF")
posted_TUE = form.getvalue("TUE")
posted_CAEC = form.getvalue("CAEC")
posted_MTRANS = form.getvalue("MTRANS")



if str(getALL)!="None":

    #controller asks model to show all records
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")
    from MyQueries import MyQuery1
    
    query1 = MyQuery1()
    results= query1.showAll()
    
    #controller updates the view of data obtained from the model
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/view/")
    from MyViews import MyView1

    view1=MyView1(results)
    view1.viewAll()

    
if str(searchName)!="None":
    
    #controller asks model to show all records
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")
    from MyQueries import MyQuery2
    
    query2 = MyQuery2(searchName)
    results= query2.searchN()
    
    #controller updates the view of data obtained from the model
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/view/")
    from MyViews import MyView2
   
    view1= MyView2(results)
    view1.viewSearched()


# take test button ===============================================================
if str(takeTestBtn)!="None":
    #controller updates the view of addRecord
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/view/")
    from TestPage import MyTestPageView
    view1 = MyTestPageView()
    view1.viewAddRecordTestpage()

# submit test =====================================================================
if str(sendTestBtn)!="None":
    '''
    #controller asks model to perform add record
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")
    from MyQueries import MyAddRecord
    try:
    # Your existing code here...
        myaddrec = MyAddRecord(postedID,postedName,postedDegree,postedAge)
        result=myaddrec.addRec()
    except mysql.connector.Error as e:
        print("Error:", e)
  '''
    form_data = [
        posted_Age,
        posted_Gender,
        posted_Height,
        posted_Weight,
        posted_CALC,
        posted_FAVC,
        posted_FCVC,
        posted_NCP,
        posted_SCC,
        posted_SMOKE,
        posted_CH20,
        posted_family_history,
        posted_FAF,
        posted_TUE,
        posted_CAEC,
        posted_MTRANS
        ]
    

    print('<script> console.log("is here"); </script>')
    print('<script> console.log("is hergegee"); </script>')
    
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/utilities/")
    import PredictionModel

    tryInput = [23, "Male", 1.65, 60, "No", "No", 2, 1, "No", "No", 3, "No", 1, 2, "Sometimes", "Public_Transportation"]
    print('<script> console.log("is after prediction model import"); </script>')

    pred = PredictionModel.Prediction()
    
    predResult = pred.Predict(tryInput)
    print(predResult)

    print('<script> console.log("is HERHERHEHREJRHEJRHSKJ HFAKJ"); </script>')

    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")
    import MyQueries
    myrecomendation = MyQueries.GetMYrecomendation(predResult)
    results = myrecomendation.getRec()

    print(results)
    #controller updates the view back to addRecord
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/view/")
    from ResultPage import MyTestPageView
    viewResult = MyTestPageView("<div>"+ "sd" + "</div>")
    viewResult.viewResultPage()
    
if str(backHomefromBootStrapDesign)!="None":

    #controller asks updates design back to index or main
    redirectURL = "http://localhost/Obeysitey/Obeysitey/Index.html"
    print ('<script type="text/javascript">window.location ="' + redirectURL + '";</script>')
    print("Petmalu")
   
   


    


    
    




    

