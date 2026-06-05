#Armstrong number 

number = int(input("enter  number..... "))

number_copy = number

digit_count = 0

while(number!=0):

    digit = number % 10

    digit_count+=1

    number = number//10

total = 0 
while(number_copy!=0):

    digit = number_copy % 10

    expo = digit ** digit_count

    total = total + expo

    number_copy = number_copy // 10

print(total)







