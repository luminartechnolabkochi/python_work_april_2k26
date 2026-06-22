class Calculator:

    def add(self,*args):

        return sum(args)
    
  
    

calc_instance = Calculator()

# calc_instance.add(100,200)
# calc_instance.add(100,200,300)
calc_instance.add(100,200,300,400)