def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 * num2
    return result

def main():
    alpha = 10
    beta = 20
    total = add(alpha, beta)
    print("sum", total)

    diff = sub(alpha, beta)
    print("diff", diff)

# Main starts from here

#print("from calci", __name__)
if __name__ == "__main__":
    main()
   
