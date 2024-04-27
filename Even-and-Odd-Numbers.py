# Python Program to check weather input number is even of odd

number = int(input("Please enter the number to check whether it is even or odd: "))

if number % 2 == 0:
    print(f"{number} is an even number!")
else:
    print(f"{number} is an odd number!")
