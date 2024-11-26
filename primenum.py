x = int(input("Enter any number:-"))

for i in range(2,x):
    if x % i == 0:
        print(x,"is not prime number")
        break
else:
    print(x,"is prime number")