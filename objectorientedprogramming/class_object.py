

# Vehicle [name,brand,price,fuel_type, start(),accelerate(),stop()]


class Vehicle:

    name:str

    brand:str

    price:int

    fuel_type:str

    def start(self):

        print("vehicle starting....")

    def accelerate(self):

        print("vehicle accelerate .......")

    def stop(self):

        print("vehicle stop")


# object_name = classNmae()

pulsar = Vehicle()

passion_pro = Vehicle()

pulsar.start()
passion_pro.start()




