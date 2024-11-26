def greaterNumber(a,b):
    if (a>b):
        print("a is greater")
    elif(b>a):
        print("b is greater")
    else:
        print("Both are equal")

num1=float(input("Enter number a : "))
num2=float(input("Enter number b : "))

greaterNumber(num1,num2)