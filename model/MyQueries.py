#!C:\Users\Admin\AppData\Local\Programs\Python\Python312\python




import mysql.connector


import sys
sys.path.append("C:/xampp/htdocs/OBEYSITEY/model/")
from MyConnection import MyConnection


#this is the class to getALL record


class MyQuery1():
    def showAll(self):
        try:
            conn = MyConnection("localhost", "root", "", "db")
            mydb = conn.connect()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute("SELECT * FROM info")
            myresult = mycursor.fetchall()
            return myresult
        except mysql.connector.Error as e:
            print("Error:", e)
            return None

class MyQuery2():
    def __init__(self, name):
        self.name = name

    def searchN(self):
        try:
            conn = MyConnection("localhost", "root", "", "db")
            mydb = conn.connect()
            mycursor = mydb.cursor(dictionary=True)
            sql = "SELECT * FROM info WHERE StudName = %s"
            mycursor.execute(sql, (self.name,))
            myresult = mycursor.fetchall()
            return myresult
        except mysql.connector.Error as e:
            print("Error:", e)
            return None

class MyAddRecord():
    def __init__(self, studid, studname, degree, age):
        self.studid = studid
        self.studname = studname
        self.degree = degree
        self.age = age

    def addRec(self):
        try:
            conn = MyConnection("localhost", "root", "", "db")
            mydb = conn.connect()
            mycursor = mydb.cursor()
            sql = "INSERT INTO info (StudID, StudName, Course, Age) VALUES (%s, %s, %s, %s)"
            val = (self.studid, self.studname, self.degree, self.age)
            mycursor.execute(sql, val)
            mydb.commit()
            result = mycursor.rowcount, "Record Added!"
            return result
        except mysql.connector.Error as e:
            print("Error:", e)
            return None
