print("Welcome to Love Calculator!")
name_1 = input("Please Enter Your Name: ")
name_2 = input("Please Enter Their Name: ")

combined_name = name_1 + name_2

lowercase_string = combined_name.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

love = l + o + v + e

# concatenating count of true and love in input string
love_score = str(true) + str(love)

int_love_score = int(love_score)


if (int_love_score < 10) or (int_love_score > 90):
    print(f"Your Love Score is {int_love_score}, You go together like coke and mentos")
elif (int_love_score > 40) and (int_love_score < 50):
    print(f"Your Love Score is {int_love_score}, You are Alright Together")
else:
    print(f"Your Love Score is {int_love_score}")
