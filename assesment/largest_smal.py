

number = int(input("enter number ....."))

large = 0

small = number % 10

while(number!=0):

    digit =  number % 10

    if digit> large:

        large = digit

    if digit<small:

        small = digit

    number = number // 10

print("large",large)

print("small",small)