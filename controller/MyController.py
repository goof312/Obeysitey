#!C:\Users\User\AppData\Local\Programs\Python\Python310\python

print("Content-Type: text/html")
print()     
import cgi
import sys

form = cgi.FieldStorage()

#so these are data we posted from index 
getALL=form.getvalue("ALL")
searchName=form.getvalue("name")
addRecordfromIndex=form.getvalue("TAKE")

#so these are data we posted from HTML Design MyAddRecordBoostrap
addRecordfromBootStrapDesign=form.getvalue("send")
backHomefromBootStrapDesign=form.getvalue("back")

postedID=form.getvalue("studid")
postedName=form.getvalue("studname")
postedAge=form.getvalue("age")
postedDegree=form.getvalue("degree")



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

if str(addRecordfromIndex)!="None":
    #controller updates the view of addRecord
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/view/")
    from TestPage import MyTestPageView
    view1 = MyTestPageView()
    view1.viewAddRecordTestpage()
    
if str(addRecordfromBootStrapDesign)!="None":

    #controller asks model to perform add record
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")
    from MyQueries import MyAddRecord
    try:
    # Your existing code here...
        myaddrec = MyAddRecord(postedID,postedName,postedDegree,postedAge)
        result=myaddrec.addRec()
    except mysql.connector.Error as e:
        print("Error:", e)
  
    #controller updates the view back to addRecord
    sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/view/")
    from TestPage import MyTestPageView
    view1 = MyTestPageView()
    view1.viewAddRecordTestpage()
    
if str(backHomefromBootStrapDesign)!="None":

    #controller asks updates design back to index or main
    redirectURL = "http://localhost/Obeysitey/Obeysitey/Index.html"
    print ('<script type="text/javascript">window.location ="' + redirectURL + '";</script>')
    print("Petmalu")
   
   


    


    
    




    

