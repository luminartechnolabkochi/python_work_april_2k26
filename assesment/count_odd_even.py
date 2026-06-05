""" display count of odd , even numbers from 1 to N"""

odd_count,even_count = 0,0

limit = int(input("enter limit..."))

for num in range(1,limit+1):

    if num%2==0:

        even_count += 1
    
    else:

        odd_count +=1

print("odd count =",odd_count)
print("even count =",even_count)
