
db_user_name = "django@123"

db_password="Password@123"

username = input("enter username")

password = input("enter password")

#disaplay  access granted username and password are correct else access denied 

if db_user_name==username and db_password==password:

    print("access granted>>>")

else:

    print("access denied XXXXXX")