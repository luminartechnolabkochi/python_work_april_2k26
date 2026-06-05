

ds_students=["abin","hari","revin","helvin","sreerag"]

da_students= ["kishore","jiny","hari","jhon","revin"]

# display common students


ds_set = set(ds_students)

da_set = set(da_students)

common_students = ds_set.intersection(da_set)

print(common_students)