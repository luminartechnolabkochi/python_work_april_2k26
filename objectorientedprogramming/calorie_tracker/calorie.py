#create a simple crud application of CalorieTracker application
# -should have  {id:,title:,meal_type,calorie}
# add_foodlog()
# list_foodlog()
# retrive_foodlog()
# update_foodlog()
# destroy_foodlog()
# add = > post => create
# list => get
# detail => retrieve
# update => put
# remove => delete 

class CalorieTracker:

    def __init__(self):

        self.foodlogs = []

    def post(self,**log):

        self.foodlogs.append(log)

        print("food log added successfully....")

    def get(self):

        print(self.foodlogs)

    def retrieve(self,id=None):

        data = [f for f in self.foodlogs if f["id"]==id][0]

        print(data)

    def put(self,id=None,**logs):

        food = [f for f in self.foodlogs if f["id"] == id][0]

        food.update(logs)

        print("food has been updated")

    def delete(self,id=None):

        food = [f for f in self.foodlogs if f.get("id")==id][0]

        self.foodlogs.remove(food)

        print("the food is deleted ")


# Task for monday
# UsedVehicle_crud {id,name,owner_type,running_km,codition,location,model}
# Expense_crud
# Leads_crud {id,name,contact_info,course,status,source}
# mysql
# streamlit

# streamlit=>python=>mysql [project]

# git and github