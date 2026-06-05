
# class dict:

    #def keys(slef) return all keys
    #def values(self) return all values
    #def items(self)return key,value


# I => 1 , V =>5, X=>10,L=>50,C=>100,D=>500,m=>1000


roman={
    "I":1,
    "V":5,
    "X":10,
    "L":50
}

print(roman["I"])
roman["C"]= 100

roman["D"] = 500

roman["M"] = 1000


print("keys")
for k in roman.keys():

    print(k)


print("values")
for v in roman.values():

    print(v)

print("key and value")
for k,v in roman.items():

    print(k,v)
