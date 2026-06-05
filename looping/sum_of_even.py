"""sum of even numbers from 10 to 20"""

# 10   11   12  13  14  15  16  17  18  19  20
# num

total = 0

for num in range(10,21):

    if num%2==0:

        total= total+num

print(total)