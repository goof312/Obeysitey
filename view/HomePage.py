#!C:\Users\User\AppData\Local\Programs\Python\Python310\python

import mysql.connector

import sys
sys.path.append("C:/xampp/htdocs/Obeysitey/Obeysitey/model/")

from MyQueries import *



class MyView1(): 

    def __init__(self,results):    
        self.results = results 
    
    def viewAll(self):
        print("""
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Dropdown
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#">Disabled</a>
                </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                </form>
            </div>
            </nav>
""")
 

class MyView2(): 
    def __init__(self,results):    
        self.results = results 
    def viewSearched(self):
        
        print("<html>")
        print("<body>")
        print("<center>")
        print("<h1>My Sample SEMI-MVC</h1>")
       
        print("<form action='/Obeysitey/Obeysitey/controller/MyController.py' method='post'>")
        print("Enter name: <input type='text' name ='name'>")
        print("<input type ='submit' name ='search' value = 'SEARCH'/>")
        print("</form>")
        
        print("<table border='1'>")
        print("<tr>")
        print("<th>StudID</th>")
        print("<th>Name</th>")
        print("<th>Course</th>")
        print("<th>Address</th>")
        print("</tr>")
       
 
        for row in self.results:
          print("<tr>")
          print("<td>" ,row["StudID"], "</td>")
          print("<td>" ,row["StudName"], "</td>")
          print("<td>" ,row["Course"], "</td>")
          print("<td>" ,row["Age"], "</td>")
          print("</tr>")
            
        
        print("</table>")
        print("</body>")
        print("</center>")
        print("</html>")
 

 



