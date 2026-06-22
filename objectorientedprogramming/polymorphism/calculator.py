


class Calculator:

     def eval(self,*args,**kwargs):
          
          if kwargs["operand"]=="+":
               
               print(sum(args))
        
          elif kwargs["operand"]=="*":
               
               result = 1
               
               for num in args:
                    
                    result = result * num

               print(result)

          elif kwargs["operand"] == "min":

              return min(args)
               
calc_instance = Calculator()

calc_instance.eval(10,20,30,40,operand="+")
calc_instance.eval(10,20,30,40,operand="*")
calc_instance.eval(10,20,30,40,operand="min")
calc_instance.eval(10,20,30,40,operand="max")

