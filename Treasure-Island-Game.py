# Flowchart for this program is added in comment section of this commit

print("Welcome to Treasure Island, Your Mission is to Find a Treasure")

left_or_right = input("Would You Like to go 'Left' or 'Right' ").lower()

if left_or_right == "left":
    swim_or_wait = input("Would You Like to 'Swim' or 'Wait' ").lower()
    if swim_or_wait == "wait":
        door = input("Which Door You Would Like to Open? 'Red', 'Blue' or 'Yellow' ")
        if door == "red" or door == "blue":
            print("Game Over!")
        else:
            print("Congratulations You Have Found the Treasure! ")
    else:
        print("Game Over!")
else:
    print("Game Over!")
