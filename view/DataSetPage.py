#!C:\Users\jolay\AppData\Local\Programs\Python\Python312\python
# C:\Users\jetje\AppData\Local\Programs\Python\Python311\python


import cgi


class MyDataSetPageView(object):
    def __init__(self):
        return

    def viewDataPage(self):
        print(
            """
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>About</title>
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
                                <li class="nav-item">
                        <form action="controller/MainController.py" method="post" style="margin-bottom: 0;">
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

                <div class="container mt-5 mb-5">

                <h1 class="display-5 text-center mt-5">Obesity</h1>
                <p class="text-justify">

</br>
                Obesity, which causes physical and mental problems, is a global health problem with serious consequences. The prevalence of obesity is increasing steadily, and therefore, new research is needed that examines the influencing factors of obesity and how to predict the occurrence of the condition according to these factors.
</br>
                <a href="https://www.semanticscholar.org/paper/Estimation-of-Obesity-Levels-with-a-Trained-Neural-Ya%C4%9F%C4%B1n-G%C3%BCl%C3%BC/2c1eab51db154493d225c8b86ba885bbaf147a2c">"https://www.semanticscholar.org/paper/Estimation-of-Obesity-Levels-with-a-Trained-Neural-Ya%C4%9F%C4%B1n-G%C3%BCl%C3%BC/2c1eab51db154493d225c8b86ba885bbaf147a2c" </a>
</br></br>
                <h4> Dataset Information </h4>
                </br>
                This dataset include data for the estimation of obesity levels in individuals from the countries of Mexico, Peru and Colombia, based on their eating habits and physical condition. The data contains 17 attributes and 2111 records, the records are labeled with the class variable NObesity (Obesity Level), that allows classification of the data using the values of Insufficient Weight, Normal Weight, Overweight Level I, Overweight Level II, Obesity Type I, Obesity Type II and Obesity Type III. 77% of the data was generated synthetically using the Weka tool and the SMOTE filter, 23% of the data was collected directly from users through a web platform.
                </br></br>
                Gender: Feature, Categorical, "Gender"</br>
                Age : Feature, Continuous, "Age"</br>
                Height: Feature, Continuous</br>
                Weight: Feature Continuous</br>
                family_history_with_overweight: Feature, Binary, " Has a family member suffered or suffers from overweight? "</br>

                FAVC : Feature, Binary, " Do you eat high caloric food frequently? "</br>
                FCVC : Feature, Integer, " Do you usually eat vegetables in your meals? "</br>
                NCP : Feature, Continuous, " How many main meals do you have daily? "</br>
                CAEC : Feature, Categorical, " Do you eat any food between meals? "</br>
                SMOKE : Feature, Binary, " Do you smoke? "</br>
                CH2O: Feature, Continuous, " How much water do you drink daily? "</br>
                SCC: Feature, Binary, " Do you monitor the calories you eat daily? "</br>
                FAF: Feature, Continuous, " How often do you have physical activity? "</br>
                TUE : Feature, Integer, " How much time do you use technological devices such as cell phone, videogames, television, computer and others? "</br>

                CALC : Feature, Categorical, " How often do you drink alcohol? "</br>
                MTRANS : Feature, Categorical, " Which transportation do you usually use? "</br>
                NObeyesdad : Target, Categorical, "Obesity level"</br>

</br>
Source: <a href="https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels/data">https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels/data</a>
</p>


                </div>
        </body>
        </html>
        """
        )
