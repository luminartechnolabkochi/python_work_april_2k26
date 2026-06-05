

expenses = [870,670,780,1200,1300,1400,870]

total = 0

for exp in expenses:

    total +=exp

print("total exp",total)

avg = total / len(expenses)

print("AVG",avg)

"display expenses where expense > avg expense"

print("exp > avg")
for exp in expenses:

    if exp>avg:

        print(exp)

costly_exp = expenses[0]

for exp in expenses:

    if exp > costly_exp:

        costly_exp = exp

print("costly expense",costly_exp)

min_exp = expenses[0]

for exp in expenses:

    if exp < min_exp:

        min_exp = exp

print("min exp = ",min_exp)
