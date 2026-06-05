
#4 => 1* 2*3 *4 
def factorial(number):

    result = 1

    for i in range(1,number+1):

        result = result*i


    return result


print(factorial(4))

