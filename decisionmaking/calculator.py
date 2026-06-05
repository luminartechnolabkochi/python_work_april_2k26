

number1  = int(input("enter number1"))

number2  = int(input("enter number2"))

operation = input("Enter operation (+,-,*,/)")

match operation:

    case "+":print(number1 ,"+",number2,"=",number1+number2)#10 + 20 = 30

    case "-":print(f"{number1} - {number2} = {number1-number2}")

    case "*":print(f"{number1} * {number2} = {number1*number2}")

    case "/":print(f"{number1} / {number2} = {number1/number2}")

    case _:print("inavlid")


