size =  int(input("Enter the size of the pattern:"))

x = 0
while x < size:
    for y in range(1, size+1):
        print("*", end="")
    print()
    x += 1