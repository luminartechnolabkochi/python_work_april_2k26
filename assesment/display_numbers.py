"""print all numbers from 1 to N divisible by 5"""

n = int(input("enter number.."))
for num in range(1,n+1):

    if num%5==0:

        print(num)