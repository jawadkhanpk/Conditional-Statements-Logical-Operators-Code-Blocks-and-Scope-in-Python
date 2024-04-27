# Flowchart for this program is attached in comment section of commit

# Logic:
# if height >= 120cm, if yes can ride, if not then can't ride
# if yes check using nested if,
# 12 under ticket must be $5,
# between 12-18 ticket must be $7,
# 18 over ticket must be $12
# if wants photo taken add $5 to the bill

print("Welcome to a Rollercoaster!")
height = int(input("Please Enter Your Height: "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please Enter Your Age: "))
    if age < 12:
        bill = 5
        print("Childs Tickets are $5")
    elif age < 18:
        bill = 7
        print("Youth Tickets are $7")
    else:
        bill = 12
        print("Adults Tickets are $12")

    wants_photo = input("Do You Want a Photo Taken? Y or N ")
    if wants_photo == "Y" or "y":
        # Add $3 to their bill
        bill += 3
    print(f"Your Final Bill is ${bill}")

else:
    print("You can't ride the rollercoaster!")
