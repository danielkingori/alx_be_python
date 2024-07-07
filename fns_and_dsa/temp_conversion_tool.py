FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius():
    x = int(input("Enter the temperature to convert:"))
    y = (input("Is this temperature in Celsius or Fahrenheit? (C/F):"))
    if y == "F":
        t_in_c = FAHRENHEIT_TO_CELSIUS_FACTOR * x
        print(f"{x}°F is {t_in_c}°C ")
    elif y== "C":
        t_in_f = CELSIUS_TO_FAHRENHEIT_FACTOR * x
        print(f"{x}°c is {t_in_f}°F ")
    else:
        print("Enter a valid selcetion")
        
convert_to_celsius()