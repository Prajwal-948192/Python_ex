a = 1
b = 1
print(a)
print(b)
count = 0 
while count < 5:
    res = a + b

    a = b
     
    b = res
    
    print(b)
    count = count + 1
