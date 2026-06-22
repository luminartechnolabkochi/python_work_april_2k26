
# ExpenseTrcaker[name,phone,email,transactions:[{},{}],add_transactions(),list_transactions(),summary()]

# object oriented programming features [inheritance,polymorphism,encapsulation,abstraction]
class DietLens:
   

    def __init__(self,name,age,weight,height,gender):

        self.name = name

        self.age = age

        self.height = height

        self.weight = weight

        self.gender = gender

        self.food_logs =list()

    def add_food_log(self,name=None,calorie=None,meal_type=None):
        
        self.food_logs.append({"name":name,"calorie":calorie,"meal_type":meal_type})

    
    def list_food_logs(self):

        print(self.food_logs)

    def summary(self):

        all_calories = [log["calorie"] for log in self.food_logs]

        print("total calorie",sum(all_calories))

        meal_summary ={}

        for log in self.food_logs:

            meal_type = log["meal_type"]

            calorie  = log["calorie"]

            if meal_type in meal_summary:

                meal_summary[meal_type]+=calorie
            else:
                meal_summary[meal_type]=calorie

        print("meal type summary",meal_summary)

           



diet_lense_instance = DietLens("aravind",22,85,175,"male")

diet_lense_instance.add_food_log(name="puttu",calorie=180,meal_type="break_fast")
diet_lense_instance.add_food_log(name="puttu",calorie=180,meal_type="break_fast")
diet_lense_instance.add_food_log(name="puttu",calorie=180,meal_type="break_fast")
diet_lense_instance.add_food_log(name="fried rice",calorie=180,meal_type="lunch")
diet_lense_instance.add_food_log(name="fried rice",calorie=180,meal_type="lunch")
diet_lense_instance.add_food_log(name="fried rice",calorie=180,meal_type="lunch")

diet_lense_instance.list_food_logs()

diet_lense_instance.summary()









