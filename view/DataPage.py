#!C:\Users\jolay\AppData\Local\Programs\Python\Python312\python
# C:\Users\jetje\AppData\Local\Programs\Python\Python311\python


import cgi


class MyDataPageView(object):
    def __init__(self, data):
        self.data = data

    def viewDataPage(self):
        print(
            """
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Data View</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
                    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            </head>

            <body>
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
                                <li class="nav-item ">
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
                            </ul>
                            <form class="form-inline mt-2 mt-lg-0 d-flex" action="MainController.py" method="post" style="margin-bottom: 0;">
                                <input type="submit" class="btn text-white" style="background-color: #418cfd;" name="TAKE"
                                    value="Take The Test" />
                            </form>
                        </div>
                    </div>
                </nav>

                <h1 class="display-5 text-center mt-5">Obesity Data Set</h1>
                <div class="container mt-5">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th scope="col">id</th>
                                <th scope="col">Age</th>
                                <th scope="col">Gender</th>
                                <th scope="col">Height</th>
                                <th scope="col">Weight</th>
                                <th scope="col">CALC</th>
                                <th scope="col">FAVC</th>
                                <th scope="col">FCVC</th>
                                <th scope="col">NCP</th>
                                <th scope="col">SCC</th>
                                <th scope="col">SMOKE</th>
                                <th scope="col">CH2O</th>
                                <th scope="col">Family History</th>
                                <th scope="col">FAF</th>
                                <th scope="col">TUE</th>
                                <th scope="col">CAEC</th>
                                <th scope="col">MTRANS</th>
                                <th scope="col">NObeyesdad</th>
                            </tr>
                        </thead>
                        <tbody>
                        """)
                        
                        
        for row in self.data:
            print("<tr>")
            print("<th scope='row'>", row["id"],"</th>")
            print("<td>" , row["age"], "</td>")
            print("<td>" ,row["gender"], "</td>")
            print("<td>" ,row["height"], "</td>")
            print("<td>" ,row["weight"], "</td>")
            print("<td>" ,row["calc"], "</td>")
            print("<td>" ,row["favc"], "</td>")
            print("<td>" , row["fcvc"], "</td>")
            print("<td>" ,row["ncp"], "</td>")
            print("<td>" ,row["scc"], "</td>")
            print("<td>" ,row["smoke"], "</td>")
            print("<td>" ,row["ch2o"], "</td>")
            print("<td>" ,row["family_history_with_overweight"], "</td>")
            print("<td>" , row["faf"], "</td>")
            print("<td>" ,row["tue"], "</td>")
            print("<td>" ,row["caec"], "</td>")
            print("<td>" ,row["mtrans"], "</td>")
            print("<td>" ,row["NObeyesdad"], "</td>")
            print("</tr>")
        print(
                    """
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """
        )
    
