"""
class set:

    def union(self,set)
    def intersection(self,set)
    def difference(self,set)
    def is_subset()
    def is_superset()


"""

set_a = {10,20,30,40}
set_b = {30,40,100,200}

print(set_a.issuperset(set_b))

print(set_b.issubset(set_a))

union_set = set_a.union(set_b)

print("union set",union_set)

intersection_set = set_a.intersection(set_b)

print("intersection set",intersection_set)

difference_set = set_a.difference(set_b)

print("difference set",difference_set)