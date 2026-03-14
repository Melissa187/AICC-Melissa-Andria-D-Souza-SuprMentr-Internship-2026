#3.Sum until the user stops.
total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break
    
    total += num

print("Sum is:", total)
