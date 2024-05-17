#!C:\Users\Admin\AppData\Local\Programs\Python\Python312\python


import mysql.connector

class MyConnection():   
       
        def __init__(self, host, user, pwd,dbase):    
                self.host = host
                self.user = user
                self.port = 3306
                self.pwd = pwd
                self.dbase = dbase
                
        def connect(self): 
                mydb = mysql.connector.connect(host=self.host,
                                               port= self.port,
                                               user=self.user,
                                               passwd=self.pwd,
                                               database=self.dbase)
                return mydb