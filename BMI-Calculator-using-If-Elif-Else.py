# Logic:
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese

height = float(input("Please Enter Your Height: "))
weight = float(input("Please Enter Your Weight: "))

bmi = round(weight) / (height ** 2)

if bmi < 18.5:
    print(f"You BMI is {bmi}, you are under weight!")
elif bmi < 25:
    print(f"You BMI is {bmi}, you are normal weight!")
elif bmi < 30:
    print(f"You BMI is {bmi}, you are over weight!")
elif bmi < 35:
    print(f"You BMI is {bmi}, you are obese!")
else:
    print(f"You BMI is {bmi}, you are clinically obese!")
