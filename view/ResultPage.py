#!C:\Users\jetje\AppData\Local\Programs\Python\Python311\python

import cgi

class MyTestPageView(object):
    def __init__(self, recomendation):
        self.recomendation = recomendation
     
    def viewResultPage(self):
        print("""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    
<style type="text/css">
    #likert { text-align:center; }
    #likert td { width: 70px; }
 </style>
  </head>


  <body class="bg-secondary-subtle">
    <nav class="navbar navbar-expand-lg navbar-light bg-primary">
        <a class="navbar-brand" href="/Obeysitey/Obeysitey/Index.html"style="color: white; margin: 10px;">Obeysitey</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
          <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
            
            <li class="nav-item active">
              <a class="nav-link" href="" style="Color: white; margin-left: 10%;">Home <span class="sr-only"></span></a>
            </li>
          </ul>

        </div>
      </nav>
    <div>
        <center>
            <form action ="MyController.py" method ="post">
            <br>
            <h1>YOUR RESULT</h1>
                
            <blockquote class="blockquote">
            <p>
                  <div class="p-3 bg-info bg-opacity-10 border border-info border-start-0 rounded-end">
                    NObeyesdad: Type of obesity - insufficient_weight, normal_weight, overweight-level_i, overweight-level_ii, obesity_type_i, obesity_type_ii, obesity_type_iii
                  </div>
              """
              + self.recomendation + 
              """
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




""")