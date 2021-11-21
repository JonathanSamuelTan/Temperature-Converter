#-----------------------------function
def CtoR(t):
    reamur = 4/5*t
    return reamur

def CtoF(t):
    fahrenhait = 9/5*t + 32
    return fahrenhait

def CtoK(t):
    kelvin = t+273
    return kelvin

def RtoC(t):
    celcius = 5/4*t
    return celcius

def RtoF(t):
    fahrenhait = 9/4*t + 32
    return fahrenhait

def RtoK(t):
    kelvin = RtoC(t)+273
    return kelvin

def FtoC(t):
    celcius = (t-32)*5/9
    return celcius

def FtoR(t):
    reamur = (t-32)*4/9
    return reamur

def FtoK(t):
    kelvin = FtoC(t)+273
    return kelvin

def KtoC(t):
    celcius = t-273
    return celcius

def KtoR(t):
    reamur = CtoR(t-273)
    return reamur

def KtoF(t):
    kelvin = CtoF(t-273)
    return kelvin

#------------------------------------------ Main Program
print("=====Temperature Convertion=====")
From = input("Convert from (celcius,reamur,etc): ")
To   = input ("Convert to: ")
t = float(input("temperature (number only): "))

if(From.casefold()=="celcius"):

    if(To.casefold() == "reamur"):
        print(t," ",From," = ",CtoR(t)," ",To)
    elif(To.casefold() == "fahrenhait"):
        print(t," ",From," = ",CtoF(t)," ",To)
    elif(To.casefold() == "kelvin"):
        print(t," ",From," = ",CtoK(t)," ",To)
    else:
        print("inputs aren`t valid , please try again")

elif(From.casefold()=="reamur"):
    
    if(To.casefold() == "celcius"):
        print(t," ",From," = ",RtoC(t)," ",To)
    elif(To.casefold() == "fahrenhait"):
        print(t," ",From," = ",RtoF(t)," ",To)
    elif(To.casefold() == "kelvin"):
        print(t," ",From," = ",RtoK(t)," ",To)
    else:
        print("inputs aren`t valid , please try again")

elif(From.casefold()=="farenhait"):
   
    if(To.casefold() == "celcius"):
        print(t," ",From," = ",FtoC(t)," ",To)
    elif(To.casefold() == "reamur"):
        print(t," ",From," = ",FtoR(t)," ",To)
    elif(To.casefold() == "kelvin"):
        print(t," ",From," = ",FtoK(t)," ",To)
    else:
        print("inputs aren`t valid , please try again")

elif(From.casefold()=="kelvin"):
    
    if(To.casefold() == "celcius"):
        print(t," ",From," = ",KtoC(t)," ",To)
    elif(To.casefold() == "fahrenhait"):
        print(t," ",From," = ",KtoF(t)," ",To)
    elif(To.casefold() == "reamur"):
        print(t," ",From," = ",KtoR(t)," ",To)
    else:
        print("inputs aren`t valid , please try again")

else:
    print("inputs aren`t Valid, please try again")



    