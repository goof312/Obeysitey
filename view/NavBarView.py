#!C:\Users\jolay\AppData\Local\Programs\Python\Python312\python
# C:\Users\jetje\AppData\Local\Programs\Python\Python311\python


import cgi


class MyNavbarView:
    def __init__(self):
        print('<script> console.log("is HERERE"); </script>')
        return

    def NavBar(self):
        return """
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
                        """
