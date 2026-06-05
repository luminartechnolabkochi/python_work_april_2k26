#collections


numbers = [1,2,3,2,4]

max_frequent_count = numbers.count(numbers[0])

max_frequent_number = numbers[0]


for num in numbers:

    if numbers.count(num) > max_frequent_count:

        max_frequent_count = numbers.count(num)

        max_frequent_number = num

print(max_frequent_number,"=mode==")









# display mean
# display median
# display mode

# =====mean=======

sum = 0

for num in numbers:

    sum +=num
mean = sum/len(numbers)

print("==========mean :",mean,"==========")


#======median=====================

numbers.sort()

# [10,11,12,7,8,9,10,11,15,16]
#   0  1 2 3  4 5  6  7  8  9

length = len(numbers)-1

mid = length //2

print("median:",numbers[mid])