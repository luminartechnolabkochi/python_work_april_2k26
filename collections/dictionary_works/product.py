# create a dictionary product with id,title,price,category
# disaply price
# display category


product = {"id":12,"title":"iphone16","price":75000,"category":"mobile"}


for k in product:

    print(k,"=>",product[k])



product["price"]=80000 # update

print(product)

product["brand"]="apple"# add

print(product)