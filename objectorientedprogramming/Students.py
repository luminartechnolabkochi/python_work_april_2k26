


class Student:

    name:str

    roll_number:int

    course:str

    def __init__(self,name,roll,course):

        self.name = name

        self.roll_number = roll

        self.course = course

    def display_attrs(self):

        print(self.name,self.roll_number,self.course)



student_instance = Student("ajmal","1234","django")# object1





student_instance.display_attrs()


# constructor is a special method 
# automatically invoked during object creation
# name of constructor __init__()
# constructor is used for initializing attributes of object
