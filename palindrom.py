# x = input("Enter the any value or string:- ")

# r = x[::-1]

# if x==r :
#     print("palindrome")
# else:
#     print("not palindrome")

number = int(input("Enter any number:- "))
rev=0
num = number
while (number>0):
    i= number % 10
    rev = rev * 10 + i
    number = number //10

if num == rev :
    print("number is palindrome")
else:
    print("number is not palindrome")