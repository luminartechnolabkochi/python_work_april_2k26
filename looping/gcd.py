

num1 = 48

num2 = 18

smallest_number = num1 if num1<num2 else num2


gcd = 1

for i in range(1,smallest_number+1):

    if num1%i==0 and num2%i==0:

        gcd = i

print(gcd)