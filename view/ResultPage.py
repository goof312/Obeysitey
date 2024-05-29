#!C:\Users\jolay\AppData\Local\Programs\Python\Python312\python
# C:\Users\jetje\AppData\Local\Programs\Python\Python311\python


import cgi


class MyTestPageView(object):
    def __init__(self, recomendation):
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
    <nav class="navbar navbar-expand-lg " style="background-color: #0d6efd;">
        <div class="container-fluid">
            <a class="navbar-brand text-white" href="#">Obeysitey</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item" style="decoration: none;">
                        <form action="MainController.py" method="post" style="margin-bottom: 0;">
                            <input name="back" type="submit" class="nav-link active text-white" aria-current="page"
                                value="Home" />
                        </form>
                    </li>
                    <li class="nav-item">
                        <form action="MainController.py" method="post" style="margin-bottom: 0;">
                            <input name="dataList" type="submit" class="nav-link active text-white" aria-current="page"
                                value="Data" />
                        </form>

                    </li>
                    <li class="nav-item">
                        <form action="MainController.py" method="post" style="margin-bottom: 0;">
                            <input name="dataset" type="submit" class="nav-link active text-white" aria-current="page"
                                value="About" />
                        </form>

                    </li>
                </ul>
                <form class="form-inline mt-2 mt-lg-0 d-flex" action="MainController.py" method="post" style="margin-bottom: 0;">
                    <input type="submit" class="btn text-white" style="background-color: #418cfd;" name="TAKE"
                        value="Take The Test" />
                </form>
            </div>
        </div>
    </nav>
    <div>
        <center>
            <form action ="MainController.py" method ="post">
            <br>
            <h1>YOUR RESULT</h1>
                
            <blockquote class="blockquote">
            <p>
                  <div class="p-3 bg-info bg-opacity-10 border border-info border-start-0 rounded-end">
                    
                      
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
            </center>
    </div>

  </body>
</html>




"""
        )
