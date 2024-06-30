number =  int(input("Enter a number to see its multiplication table:"))

for num in range(1,11):
    result = num * number
    print(f"{num} * {number} = {result}")