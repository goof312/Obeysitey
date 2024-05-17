#!C:\Users\User\AppData\Local\Programs\Python\Python310\python

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
 </style>
  </head>


  <body class="bg-secondary-subtle">
    <nav class="navbar navbar-expand-lg navbar-light bg-primary">
        <a class="navbar-brand" href="#"style="color: white;">(Logo) Obesitey</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
          <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
            <li class="nav-item active">
              <a class="nav-link" href="#" style="Color: white">Home <span class="sr-only"></span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" style="Color: white">Test</a>
            </li>
          </ul>

        </div>
      </nav>
    <div>
        <center>
            <form action ="controller/MyController.py" method ="post">
            <br>
            <h1>Lorem Ipsum</h1>
                
<p>
    <div class="p-3 bg-info bg-opacity-10 border border-info border-start-0 rounded-end">
        Gender</p>
        <div>
                <table id="likert">
                    <tr>
                        <td><input id="radgenderMale" type="radio" name="gender" value="male" /></td>
                        <td><input id="radgenderFemale" type="radio" name="gender" value="female" /></td>
                    </tr>
                    <tr>
                        <td>Male</td>
                        <td>Female</td>
                    </tr>
                </table>
        </div>  

        
<br>
<p>Age</p>
<div>
    <input type="text" class="form-control" name="age" placeholder="Type Age">
</div>


<br>
<p>Height</p>
<div>		
        <input type="text" class="form-control" name="height" placeholder="Type height (in meters)">
</div>


<br>
<p>Weight</p>
<div>		
        <input type="text" class="form-control" name="weight" placeholder="Type Weight (in kg)">
</div>


<br>
<p>Has a family member suffered or suffers from overweight?</p>
<div>
        <table id="likert">
            <tr>
                <td><input id="historyyes" type="radio" name="family_history_with_overweight" value="yes" /></td>
                <td><input id="historyno" type="radio" name="family_history_with_overweight" value="no" /></td>
            </tr>
            <tr>
                <td>Yes</td>
                <td>No</td>
            </tr>
        </table>
</div> 


<br>
<p>Frequent consumption of high caloric food</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="FAVCyes" type="radio" name="FAVC" value="yes" /></td>
            <td><input id="FAVCno" type="radio" name="FAVC" value="no" /></td>
        </tr>
        <tr>
            <td>Yes</td>
            <td>No</td>
        </tr>
    </table>
</div> 


<br>
<p>Frequency of consumption of vegetables</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="fcvcnever" type="radio" name="FCVC" value="never" /></td>
            <td><input id="fcvcsometimes" type="radio" name="FCVC" value="sometimes" /></td>
            <td><input id="fcvcalways" type="radio" name="FCVC" value="always" /></td>
        </tr>
        <tr>
            <td>Never</td>
            <td>Sometimes</td>
            <td>Always</td>
        </tr>
    </table>
</div> 


<br>
<p>Number of main meals</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="ncp1" type="radio" name="NCP" value="1" /></td>
            <td><input id="ncp2" type="radio" name="NCP" value="2" /></td>
            <td><input id="ncp3" type="radio" name="NCP" value="3" /></td>
            <td><input id="ncp4" type="radio" name="NCP" value="4" /></td>
        </tr>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
        </tr>
    </table>
</div> 


<br>
<p>Consumption of food between meals</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="caecno" type="radio" name="CAEC" value="no" /></td>
            <td><input id="caecsometimes" type="radio" name="CAEC" value="sometimes" /></td>
            <td><input id="caecfreq" type="radio" name="CAEC" value="frequently" /></td>
            <td><input id="caecalways" type="radio" name="CAEC" value="always" /></td>
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
<p>Do you smoke?</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="smokeyes" type="radio" name="SMOKE" value="yes" /></td>
            <td><input id="smokeno" type="radio" name="SMOKE" value="no" /></td>
        </tr>
        <tr>
            <td>Yes</td>
            <td>No</td>
        </tr>
    </table>
</div> 


<br>
<p>Consumption of water daily</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="CH2Oless" type="radio" name="CH2O" value="less than 1 litter" /></td>
            <td><input id="CH2Obetween" type="radio" name="CH2O" value="between 1 and 2" /></td>
            <td><input id="CH2Omore" type="radio" name="CH2O" value="more than 2 litters" /></td>
        </tr>
        <tr>
            <td>Less than 1 litter</td>
            <td>Between 1 and 2 litter</td>
            <td>More than 2 litters</td>
        </tr>
    </table>
</div> 


<br>
<p> Calories consumption monitoring</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="SCCyes" type="radio" name="SCC" value="yes" /></td>
            <td><input id="SCCno" type="radio" name="SCC" value="no" /></td>
        </tr>
        <tr>
            <td>Yes</td>
            <td>No</td>
        </tr>
    </table>
</div> 


<br>
<p>Physical activity frequency</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="FAF1" type="radio" name="FAF" value="1" /></td>
            <td><input id="FAF2" type="radio" name="FAF" value="2" /></td>
            <td><input id="FAF3" type="radio" name="FAF" value="3" /></td>
            <td><input id="FAF" type="radio" name="FAF" value="4" /></td>
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
<p>Time using technology devices</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="TUE1" type="radio" name="TUE" value="1" /></td>
            <td><input id="TUE2" type="radio" name="TUE" value="2" /></td>
            <td><input id="TUE3" type="radio" name="TUE" value="3" /></td>
        </tr>
        <tr>
            <td>0 to 2</td>
            <td>3 to 5</td>
            <td>>5</td>
        </tr>
    </table>
</div> 


<br>
<p>Consumption of alcohol</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="CALCno" type="radio" name="CALC" value="no" /></td>
            <td><input id="CALCsometimes" type="radio" name="CALC" value="sometimes" /></td>
            <td><input id="CALCfreq" type="radio" name="CALC" value="frequently" /></td>
            <td><input id="CALCalways" type="radio" name="CALC" value="always" /></td>
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
<p>Transportation used</p>
<div>
    <table id="likert">
        <tr>
            <td><input id="MTRANSauto" type="radio" name="MTRANS" value="automobile" /></td>
            <td><input id="MTRANSmotor" type="radio" name="MTRANS" value="motorbike" /></td>
            <td><input id="MTRANSbike" type="radio" name="MTRANS" value="bike" /></td>
            <td><input id="MTRANStranspo" type="radio" name="MTRANS" value="public_transportation" /></td>
            <td><input id="MTRANSwalking" type="radio" name="MTRANS" value="walking" /></td>
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



        </div>
            <br>
            </form>
            </center>
    </div>





  </body>
</html>




""")