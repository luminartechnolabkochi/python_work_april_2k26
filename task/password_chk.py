

"""
Ask the user to enter a password.
   Display "Valid password" if its length is at least 8 characters, otherwise "Too short".
"""


password = input("enter password..") #pwd

if len(password) <8:

    print("Too short")

else:

    print("Valid password")
