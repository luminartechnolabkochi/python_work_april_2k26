"""
8. ATM Withdrawal System
   User has a balance of 10000. Allow withdrawals until balance becomes zero or user exits. Display remaining balance after each transaction.


"""




balance =  10000


while(True):

    amount = int(input("enter amount you want to withdraw"))

    if amount>balance:

        print("insufficient balance")

        break

    balance = balance-amount

    print("your aval bal is",balance)

# string 

# functions
