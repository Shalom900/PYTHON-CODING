numbers = input("24, 56, 87, 90, 100, 45, 67, 78, 46, 37, 87, 33, 67, 80, 100:  ")
max = numbers
for number in numbers:
    if number > max:
        max = number 
print(max)
