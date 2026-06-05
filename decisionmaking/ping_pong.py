
"""
number = ?

display PING if number / by 3
display PONG if number / by 5
display PINGPONG if number / by 15
invalid number otherwise


"""

number = int(input("enter number.."))#25


if number%15==0:#==0

    print("PING PONG")

elif number%5==0:

    print("PONG")

elif number%3==0:

    print("PING")

else:

    print("inavlid number")