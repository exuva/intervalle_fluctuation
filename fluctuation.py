import math
def calc():
    print("fluctuation")
    # fibre neutre
    p = float(input("proposition theorique: "))
    n = float(input("effectif echentillon: "))

    In1 = (p-1.96*((math.sqrt(p*(1-p)))/math.sqrt(n)))
    In1 = round(In1,2)

    In2 = (p+1.96*((math.sqrt(p*(1-p)))/math.sqrt(n)))
    In2 = round(In2, 2)

    print("I",n,"=","[",In1,";",In2,"]")
    print(" ")
    In1r = In1 * 100 
    In1r = round(In1r,0)
    In2r = In2 * 100
    In2r = round(In2r,0)
    print("donc dans 95""%""des cas, la frequence observer de p (f) sera comprise entre ",In1r,"%" "et",In2r,"%")
calc()