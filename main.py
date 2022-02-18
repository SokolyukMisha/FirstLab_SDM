from math import sqrt

def Discriminant():
    a = float(input("a = "))
    if a == 0:
        print("a can't be zero")
        Discriminant()
        return
    b = float(input("b = "))
    c = float(input("c = "))
    d = pow(b, 2) - (4 * a * c)
    return Solve(a,b,c,d)

def Solve(a, b,c, d):
    print(f"({a}) x^2 + ({b}) x + ({c}) = 0")
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x1 = -(b / (2 * a))
        print("There are 1 root")
        print(f"x = {x1}")
    else:
        print("There are 0 roots")

def Interactive():
        Discriminant()

Interactive()
