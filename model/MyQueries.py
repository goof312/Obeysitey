#!C:\Users\jetje\AppData\Local\Programs\Python\Python311\python



import mysql.connector
import mysql

import sys
sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")
from MyConnection import MyConnection


# this is the class to getALL record


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


class AddRecord():
    def __init__(self, __age, __gender, __height, __weight, __calc, __favc, __fcvc, __ncp, __scc,
                 __smoke, __ch20, __family_history_with_overweight, __faf, __tue, __caec, __mtrans, __nobeyesdad):
        self.__age = __age
        self.__gender = __gender
        self.__height = __height
        self.__weight = __weight
        self.__calc = __calc
        self.__favc = __favc
        self.__fcvc = __fcvc
        self.__ncp = __ncp
        self.__scc = __scc
        self.__smoke = __smoke
        self.__ch20 = __ch20
        self.__family_history_with_overweight = __family_history_with_overweight
        self.__faf = __faf
        self.__tue = __tue
        self.__caec = __caec
        self.__mtrans = __mtrans
        self.__nobeyesdad = __nobeyesdad

    def addRecord(self):
        try:
            conn = MyConnection("localhost", "root", "", "obesityrecords")
            mydb = conn.connect()
            mycursor = mydb.cursor()
            sql = "INSERT INTO records(age, gender, height, weight, calc, favc, fcvc, ncp, scc, smoke, ch2o, " \
                  "family_history_with_overweight, faf, tue, caec, mtrans, NObeyesdad) VALUES (%s, %s, %s, %s, %s, %s, %s, " \
                  "%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"

            val = (self.__age, self.__gender, self.__height, self.__weight, self.__calc, self.__favc, self.__fcvc,
                   self.__ncp, self.__scc, self.__smoke, self.__ch20, self.__family_history_with_overweight,
                   self.__faf, self.__tue, self.__caec, self.__mtrans, self.__nobeyesdad)
            mycursor.execute(sql, val)
            mydb.commit()
            result = mycursor.rowcount, "Record Added!"
            return result
        except mysql.connector.Error as e:
            print("Error:", e)
            return None

class GetMYrecomendation():
    def __init__(self, __nobeyesdad):
        self.nobeyesdad = __nobeyesdad

    def getRec(self):
        try:
            conn = MyConnection("localhost", "root", "", "obesityrecords")
            mydb = conn.connect()
            mycursor = mydb.cursor(raw=True)
            sql = "SELECT CategoryDes FROM description WHERE Category=%s;"
            mycursor.execute(sql, (self.nobeyesdad,))
            myresult = mycursor.fetchone()
            return  myresult
        except mysql.connector.Error as e:
            print("Error:", e)
            return None





