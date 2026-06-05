

import random

db_number = random.randint(1,10)

attempt_count = 0

while(True):

    if attempt_count==3:

        print("failed to guess the number")

        break
    attempt_count = attempt_count+1
    
    user_input = int(input("guess a number"))

    if user_input == db_number:

        print("yeah....won!!!!")

        break

    print("please try again")

