"""Write a Python program to print the first 12 "even" Fibonacci numbers

            Assume the first two Fibonacci numbers to be 1 and 1"""

a = 1
b = 1

i = 0

while i < 12:
    a = a + b
    b = b + a

    if a % 2 == 0:
        i += 1
        print(a)
        
    elif b % 2 == 0:
        i += 1
        print(b)


        
