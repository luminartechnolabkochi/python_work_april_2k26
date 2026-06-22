

class SuperHero:


    def __init__(self,name,powers,universe):

        self.name = name

        self.powers = powers

        self.universe = universe

    def display_attrs(self):

        print(f"name {self.name}  super powers {self.powers} universe {self.universe}")


hero_instance1= SuperHero("minnalmurali","run","basil")

hero_instance1.display_attrs()

