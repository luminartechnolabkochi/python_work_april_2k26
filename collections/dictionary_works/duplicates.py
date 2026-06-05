
"""
collections
list and methods
dictionry methods
"""

nums =[10,11,12,11,13,14,15]


number_count = {}

for num in nums:

    number_count[num] = nums.count(num)

for k,v in number_count.items():

    if v>1:

        print(k)