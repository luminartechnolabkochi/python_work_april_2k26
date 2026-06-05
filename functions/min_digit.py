


def min_digit(number):

    result= number% 10

    while(number!=0):

        digit = number % 10

        if digit < result:

            result = digit

        number = number//10

    return result


print(min_digit(123))
print(min_digit(564))

#================== Foundation Topics ======================== 
# variables
# data types
# operators
# decisionmaking
# looping
# function
# ================================================
# string
# collections


# foundation Exam => P

# core  => 

# adv