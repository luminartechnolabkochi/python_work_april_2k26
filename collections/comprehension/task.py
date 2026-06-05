

expenses =[12000,13000,11000,14000,8000,7000]

# display exepnses > 12000

expe_filter = [exp for exp in expenses if exp>12000]

print(expe_filter)

words=["hello","hai","python","program"]

length_filter = [w for w in words if len(w) > 4]

print(length_filter)
