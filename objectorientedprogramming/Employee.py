
class Employee:

    name:str

    designation:str

    salary:int

    gender:str


    def __init__(self,name,desig,sal,gender):

        self.name = name

        self.designation = desig

        self.salary = sal

        self.gender = gender

    def display_attrs(self):

        print(self.name,self.designation,self.salary,self.gender)


emp1 = Employee("rohan","qa",56000,"male")

emp2 = Employee("rohan","qa",56000,"male")

emp1.display_attrs()


        
