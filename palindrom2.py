"""
number=int(input("Enter any number:-"))
rev=0
num=number

while number>0:
    i= number % 10
    rev=rev*10+i
    number=number // 10

if rev == num:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
"""

x=input("Enter any word:-")

i=x[::-1]

if x==i:
    print("The word is a palindrome")
else:
    print("not")