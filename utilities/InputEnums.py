#!C:\Users\User\AppData\Local\Programs\Python\Python310\python

from enum import IntEnum

class Gender(IntEnum):
    male = 1
    female = 0
    
class CALC(IntEnum):
    no = 0
    sometimes = 1
    frequently = 2
    always = 3

class YesNo(IntEnum):
    yes = 1
    no = 0

class CAEC(IntEnum):
    no = 0
    sometimes = 1
    frequently = 2
    always = 3
    
class MTRANS(IntEnum):
    automobile = 0
    motorbike = 1
    bike = 2
    public_transportation = 3
    walking = 4

#throw this
class FAVC(IntEnum):
    yes = 1
    no = 0
    
class SCC(IntEnum):
    yes = 1
    no = 0

class Smoke(IntEnum):
    yes = 1
    no = 0