

credit_score=int(input("enter credit score."))#320

# range()

if credit_score in range(300,580):

    print("poor")

elif credit_score in range(580,670):

    print("FAIR")

elif credit_score in range(670,740): 

    print("GOOD")

elif credit_score in range(740,800):

    print("VERY GOOD")

elif credit_score in range(800,851):

    print("EXCELLENT")

else:

    print("inavlid credit score")