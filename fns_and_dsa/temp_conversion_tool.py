# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):

  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
  
  try:
    temperature = float(input("Enter the temperature to convert:"))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()

    if unit == "C":
      converted_temperature = convert_to_fahrenheit(temperature)
      print(f"{temperature:.2f} degrees Celsius is equal to {converted_temperature:.2f} degrees Fahrenheit.")
    elif unit == "F":
      converted_temperature = convert_to_celsius(temperature)
      print(f"{temperature:.2f} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.")
    else:
      raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()