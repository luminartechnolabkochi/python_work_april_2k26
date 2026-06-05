# largest number in a digit

number = 108

small = number % 10

while(number!=0):

    digit = number % 10

    if digit<small:

        small = digit

    number = number//10

print(small)