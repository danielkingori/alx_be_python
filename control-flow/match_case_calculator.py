#num1 = input("Enter the first number:")
#num2 = input("Enter the second number:")
#operation = input("Choose the operation(+,-,*,/):")
#match operation:
#    case "+":
#        result = num1 + num2
#        print("The result is "+ result)
#    case "*":
#        result = num1 * num2
#        print("The result is "+ result)
#


num1 = float(input("Enter the first number:"))  
num2 = float(input("Enter the second number:")) 
operation = input("Choose the operation(+,-,*,/):")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")  
    case "-":
        result = num1 - num2
        print(f"The result is {result}")  
    case "*":
        result = num1 * num2
        print(f"The result is {result}")  
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")  
   # case _:
    #    print("Invalid operation symbol. Please use +, -, * or /.")