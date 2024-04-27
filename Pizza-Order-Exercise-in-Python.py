# Logic
# Small Pizza is $15
# Medium Pizza is $20
# Large Pizza is $25

# Pepperoni for small pizza is + $2
# Pepperoni for medium or large pizza is + $3

# Extra cheese  for any size pizza is + $1

print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra Cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your Final Bill is: ${bill}")