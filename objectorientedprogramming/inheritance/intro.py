"""
child class acquire the properties and methods from parent class

"""

class Parent:

    def car(self):

        print("glanza")



class Child(Parent):

    def scooter(self):

        print("activa")

child_instance = Child()

child_instance.scooter()

child_instance.car()
