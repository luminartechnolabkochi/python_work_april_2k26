
"""
self is a keyword used to refer current class instance 

super() is a function used to refer parent class
"""

class Fruit:

    name:str

    def __init__(self,name):

        self.name = name


class Apple(Fruit):


    shape:str

    color:str

    taste:str

    def __init__(self, name,shape,color,taste):#"apple","round","red","sweet")

        super().__init__(name)

        self.shape = shape

        self.color = color

        self.taste = taste

    def display_apple(self):

        print(self.name ,self.shape,self.color,self.taste)

apple_instance = Apple("apple","round","red","sweet")

apple_instance.display_apple()







# Fruits [name]=> Apple[shape,taste,color]



        