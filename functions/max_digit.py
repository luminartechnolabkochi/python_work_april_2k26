def max_digit(number):

    result = 0

    while(number!=0):

        digit = number%10

        if digit>result:

            result = digit

        number=number//10


    return result


print(max_digit(90)) 
print(max_digit(340))