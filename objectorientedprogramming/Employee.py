

class Employee:

    name:str

    designation:str

    salary:int

    gender:str


    def set_attrs(self,name,desig,sal,gender):

        self.name = name

        self.designation = desig

        self.salary = sal

        self.gender = gender

    def display_attrs(self):

        print(self.name,self.designation,self.salary,self.gender)



emp1 = Employee()

emp2 = Employee()

emp1.set_attrs("rohan","qa",56000,"male")

emp2.set_attrs("anal","devop",56000,"male")

emp1.display_attrs()


        

