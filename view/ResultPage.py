#!C:\Users\User\AppData\Local\Programs\Python\Python310\python


import cgi
from view import NavBarView as nbv


class MyTestPageView(object):
    nv = ""
    def __init__(self, recomendation):
        self.nv = nbv.MyNavbarView()
        self.recomendation = recomendation

    def viewResultPage(self):
        print(
            """
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Result Page</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                
            <style type="text/css">
                #likert { text-align:center; }
                #likert td { width: 70px; }
            </style>
            </head>


            <body class="bg-secondary-subtle">
            """ + self.nv.NavBar() + """
                <div>
                    <center>
                        <form action ="MainController.py" method ="post">
                        <br>
                        <h1>YOUR RESULT</h1>
                    </center>
                        <blockquote class="blockquote">
                        <p>
                            <div class="p-3 bg-info bg-opacity-10 border border-info rounded ms-5 me-5 ps-5 pe-5">
                                
                      
                      """
        )

        print(self.recomendation)
           
        print(
            """
                  </div>
            </p>
            <br>
            <br>
            </blockquote>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <input type="submit" class="btn btn-primary btn-lg" name="back" value="BACK HOME">
            <input type ="submit" class="btn btn-primary btn-lg" name ="TAKE" value = "TEST AGAIN"/>
            </form>
            
    </div>

  </body>
</html>




"""
        )
