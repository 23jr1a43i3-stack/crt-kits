def add(a,b):
    print("addtion of {a} and {b} is {a+b}")
def sub(a,b):
    print("substraction of {a} and {b} is {a-b}")
def multiplication(a,b):
    print("miltiplication of {a} and {b} is {a*b}")
def division(a,b):
    print("division of {a} and {b} is {a/b}")
def reminder(a,b):
    print("reminder  of {a} and {b} is {a%b}")
while True:
    print("1. addition")
    print("2 substraction")
    print("3. multiplication")
    print("4.division")
    print("5.reminder")
    print("6.Exit")
    print("----------------------")
    choice = int(input("Enter choice number"))
    if choice == 0:
        break
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    if choice == 1:
        add(a,b)
    elif  choice == 2:
        sub(a,b)
    elif  choice == 3:
        multiplication(a,b)
    elif  choice == 4:
        division(a,b)
    elif  choice == 5:
        reminder(a,b)
    print("\n")
    


