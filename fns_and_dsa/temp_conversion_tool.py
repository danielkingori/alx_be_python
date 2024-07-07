FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius():
    x = int(input("Enter the temperature to convert:"))
    y = int(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))
    if y == "F":
        print(f"{x}")
        
convert_to_celsius()
        
    