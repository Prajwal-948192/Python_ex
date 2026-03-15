"""Create a "multiply()" function that takes "num1" and "num2" as parameters

            It should return the product of "num1" and "num2"

            Make sure the function behaves as mentioned below :

            >>> multiply()              # returns  1
            1
            >>> multiply(10)         # returns  10
            10
            >>> multiply(10, 2)     # returns  20
            20
            >>>
            """

def multiply(num1 = 1, num2 = 1):
    res = num1 * num2
    return res

print(multiply(1))
print(multiply(10))
print(multiply(10, 2))
