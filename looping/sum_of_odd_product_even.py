"""
w.a.p to display sum of even numbers and product of odd numbers from 10 to 25
"""

total = 0

product = 1
for num in range(10,26):
    if num%2==0:
        total = total+num
    else:

        product = product * num

print("even sum",total)

print("odd product",product)


