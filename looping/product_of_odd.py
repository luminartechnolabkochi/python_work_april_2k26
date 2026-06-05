"""display product of odd numbers from 10 to 20"""

product = 1

for num in range(10,21):

    if num%2==1:

        product = product * num

print(product)

