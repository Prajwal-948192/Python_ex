def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 * num2
    return result

# Main starts from here

alpha = 10
beta = 20
total = add(alpha, beta)
print("sum", total)

diff = sub(alpha, beta)
print("diff", diff)

eng1 = 250 #runs
ind1 = 220
eng2 = 180

total_eng = add(eng1, eng2)
ind2 = sub(total_eng , ind1)
target = add(ind2, 1)

print("runs to win:", target)

veg = 120 #rupees
fruits = 45
total_cash = 200

total_cost = add(veg, fruits)
balance = sub(total_cash, total_cost)

print("amount to be returned:", balance)
