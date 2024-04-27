# Syntax
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do this


# Logic:
# if height >= 120cm, if yes can ride, if not then can't ride
# if yes check using nested if,
# 12 under ticket must be $5,
# between 12-18 ticket must be $7,
# 18 over ticket must be $12

print("Welcome to a Rollercoaster!")
height = int(input("Please Enter Your Height: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please Enter Your Age: "))
    if age < 12:
        print("Please pay $5")
    elif age < 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You can't ride the rollercoaster!")
