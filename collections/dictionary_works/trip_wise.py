

trip = {
    "anal":2000,
    "aravind":1800,
    "aswin":2500,
    "jithish":750
}



trip["rohan"]=500 # add a new key value pair

trip["anal"]+=1000 # update 

for k in trip:

    print(k,"=>",trip[k])

# total expense

total = 0

for k in trip:

    v = trip[k]

    total+=v

print("total expense",total)
