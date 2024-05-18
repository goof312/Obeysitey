#!C:\Users\jetje\AppData\Local\Programs\Python\Python311\python

print('<script> console.log("start"); </script>')

import cgi

class MyTestPageView(object):
     
    def viewAddRecordTestpage(self):
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


.radzize{
   transform: scale(2);
   width: 20px;
   height: 30px;
   margin-inline: 50px;
}
</style>
</head>


<body class="bg-secondary-subtle">
    <nav class="navbar navbar-expand-lg navbar-light bg-primary">
        <a class="navbar-brand" href="#"style="color: white; margin: 10px;">Obeysitey</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        
            <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                    <li class="nav-item active">
                        <a class="nav-link" href="/Obeysitey/Obeysitey/Index.html" style="Color: white; margin-left: 10%;">Home <span class="sr-only"></span></a>
                    </li>
                </ul>

            </div>
    </nav>
              
    <div class="container d-flex-justify-content-center">
        <center>
            <form action ="/Obeysitey/Obeysitey/controller/MyController.py" method ="post">
            <br>
            <h1 style="font-size:50px;">Obesity Test</h1>
            <br>
                
            <div class="p-3 bg-info bg-opacity-10 border border-info border-start-0 rounded-end">
            <p class="lead" style="font-size:30px;">Gender</p>
              
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="radgenderMale" type="radio" name="gender" value="male" checked required/></td>
                    <td><input class="radzize" id="radgenderFemale" type="radio" name="gender" value="female" checked required/></td>
                </tr>
                <tr>
                    <td>Male</td>
                    <td>Female</td>
                </tr>
            </table>
        </div>
    

        
        <br>
        <p class="lead" style="font-size:30px;">Age</p>
        <div class="col-xs-2">
            <input type="number" class="form-control" name="age" placeholder="Type Age" min="0" max="100">
        </div>


        <br>
        <p class="lead" style="font-size:30px;">Height</p>
        <div>		
            <input type="number" class="form-control" name="height" placeholder="Type height (in meters)" min="0" max="3">
        </div>


        <br>
        <p class="lead" style="font-size:30px;">Weight</p>
        <div>		
            <input type="text" class="form-control" name="weight" placeholder="Type Weight (in kg)" min="0" max="700">
        </div>


        <br>
        <p class="lead" style="font-size:30px;">Has a family member suffered or suffers from overweight?</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="historyyes" type="radio" name="family_history" value="Yes" checked required/></td>
                    <td><input class="radzize" id="historyno" type="radio" name="family_history" value="No" checked required/></td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>No</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Frequent consumption of high caloric food</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="FAVCyes" type="radio" name="FAVC" value="Yes" checked required/></td>
                    <td><input class="radzize" id="FAVCno" type="radio" name="FAVC" value="No" checked required/></td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>No</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Frequency of consumption of vegetables</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="fcvcnever" type="radio" name="FCVC" value="1" checked required/></td>
                    <td><input class="radzize" id="fcvcsometimes" type="radio" name="FCVC" value="2" checked required/></td>
                    <td><input class="radzize" id="fcvcalways" type="radio" name="FCVC" value="3" checked required/></td>
                </tr>
                <tr>
                    <td>Never</td>
                    <td>Sometimes</td>
                    <td>Always</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Number of main meals</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="ncp1" type="radio" name="NCP" value="1" checked required/></td>
                    <td><input class="radzize" id="ncp2" type="radio" name="NCP" value="2" checked required/></td>
                    <td><input class="radzize" id="ncp3" type="radio" name="NCP" value="3" checked required/></td>
                </tr>
                <tr>
                    <td>1</td>
                    <td>2</td>
                    <td>3</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Consumption of food between meals</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="caecno" type="radio" name="CAEC" value="No" checked required/></td>
                    <td><input class="radzize" id="caecsometimes" type="radio" name="CAEC" value="Sometimes" checked required/></td>
                    <td><input class="radzize" id="caecfreq" type="radio" name="CAEC" value="Frequently" checked required/></td>
                    <td><input class="radzize" id="caecalways" type="radio" name="CAEC" value="Always" checked required/></td>
                </tr>
                <tr>
                    <td>No</td>
                    <td>Sometimes</td>
                    <td>Frequently</td>
                    <td>Always</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Do you smoke?</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="smokeyes" type="radio" name="SMOKE" value="Yes" checked required/></td>
                    <td><input class="radzize" id="smokeno" type="radio" name="SMOKE" value="No" checked required/></td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>No</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Consumption of water daily</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="CH2Oless" type="radio" name="CH2O" value="1" checked required/></td>
                    <td><input class="radzize" id="CH2Obetween" type="radio" name="CH2O" value="2" checked required/></td>
                    <td><input class="radzize" id="CH2Omore" type="radio" name="CH2O" value="3" checked required/></td>
                </tr>
                <tr>
                    <td>Less than 1 litter</td>
                    <td>Between 1 and 2 litter</td>
                    <td>More than 2 litters</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;"> Calories consumption monitoring</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="SCCyes" type="radio" name="SCC" value="Yes" checked required/></td>
                    <td><input class="radzize" id="SCCno" type="radio" name="SCC" value="No" checked required/></td>
                </tr>
                <tr>
                    <td>Yes</td>
                    <td>No</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Physical activity frequency</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="FAF1" type="radio" name="FAF" value="0" checked required/></td>
                    <td><input class="radzize" id="FAF2" type="radio" name="FAF" value="1" checked required/></td>
                    <td><input class="radzize" id="FAF3" type="radio" name="FAF" value="2" checked required/></td>
                    <td><input class="radzize" id="FAF" type="radio" name="FAF" value="3" checked required/></td>
                </tr>
                <tr>
                    <td>0</td>
                    <td>1 to 2</td>
                    <td>2 to 4</td>
                    <td>4 to 5</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Time using technology devices</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="TUE1" type="radio" name="TUE" value="0" checked required/></td>
                    <td><input class="radzize" id="TUE2" type="radio" name="TUE" value="1" checked required/></td>
                    <td><input class="radzize" id="TUE3" type="radio" name="TUE" value="2" checked required/></td>
                </tr>
                <tr>
                    <td>0 to 2</td>
                    <td>3 to 5</td>
                    <td>>5</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Consumption of alcohol</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="CALCno" type="radio" name="CALC" value="No" checked required/></td>
                    <td><input class="radzize" id="CALCsometimes" type="radio" name="CALC" value="Sometimes" checked required/></td>
                    <td><input class="radzize" id="CALCfreq" type="radio" name="CALC" value="Frequently" checked required/></td>
                    <td><input class="radzize" id="CALCalways" type="radio" name="CALC" value="Always" checked required/></td>
                </tr>
                <tr>
                    <td>No</td>
                    <td>Sometimes</td>
                    <td>Frequently</td>
                    <td>Always</td>
                </tr>
            </table>
        </div> 


        <br>
        <p class="lead" style="font-size:30px;">Transportation used</p>
        <div>
            <table id="likert">
                <tr>
                    <td><input class="radzize" id="MTRANSauto" type="radio" name="MTRANS" value="Automobile" checked required/></td>
                    <td><input class="radzize" id="MTRANSmotor" type="radio" name="MTRANS" value="Motorbike" checked required/></td>
                    <td><input class="radzize" id="MTRANSbike" type="radio" name="MTRANS" value="Bike" checked required/></td>
                    <td><input class="radzize" id="MTRANStranspo" type="radio" name="MTRANS" value="Public_Transportation" checked required/></td>
                    <td><input class="radzize" id="MTRANSwalking" type="radio" name="MTRANS" value="Walking" checked required/></td>
                </tr>
                <tr>
                    <td>Automobile</td>
                    <td>Motorbike</td>
                    <td>Bike</td>
                    <td>Public transportation</td>
                    <td>Walking</td>
                </tr>
            </table>
        </div> 
            <br>

            <input type="submit" class="btn btn-primary btn-lg" name="back" value="BACK HOME" >
            <input type="submit" class="btn btn-primary btn-lg" name="send" value="SEND" >

            <br>
            <br>
            </form>
        </center>
    </div>
    </div>
</body>
</html>


""")