from math import sqrt

def Discriminant():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    discriminant = pow(b, 2) - (4 * a * c)
    return print(discriminant)


Discriminant() 
