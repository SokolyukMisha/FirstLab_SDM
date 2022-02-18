from math import sqrt
import sys
import re


def InteractiveGetValues():
    a = float(input("a = "))
    if a == 0:
        print("a can't be zero")
        InteractiveGetValues()
        return
    b = float(input("b = "))
    c = float(input("c = "))
    return Solve(a, b, c)


def Solve(a, b, c):
    print(f"({a}) x^2 + ({b}) x + ({c}) = 0")
    d = pow(b, 2) - (4 * a * c)
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


def CheckForPatterns(values):
    is_match = bool(re.match("^\d+\.?\d*\s\d+\.?\d*\s\d+\.?\d*\n", (values)))
    if not is_match:
        print("Invalid file format")
        sys.exit(1)


def NonInteractiveGetValues():
    path_input = input("Enter the file name\n>> ")
    file = open(path_input, "r")
    values = file.read()
    CheckForPatterns(values)
    value_list = values.split()
    convertedValuesList = []
    try:
        for item in value_list:
            convertedValuesList.append(float(item))
    except:
        print("Invalid values")
        sys.exit(1)
    return convertedValuesList


def Interactive():
    InteractiveGetValues()


def NonInteractive():
    a, b, c = NonInteractiveGetValues()
    if a == 0:
        print("a can't be zero")
        NonInteractive()
        return
    Solve(a, b, c)


if __name__ == "__main__":
    while True:
        _input = int(input("Choose the option: \n1.Interactive\n2.Non-interactive\n3.Exit\n>"))
        if _input == 1:
            InteractiveGetValues()
        elif _input == 2:
            NonInteractive()
        elif _input == 3:
            quit()
        elif print("please, choose from 1 to 3"):
            continue
