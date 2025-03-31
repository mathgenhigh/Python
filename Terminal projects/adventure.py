name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it's has come to an end and you can geo left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river and you can walk around it or swim across. Type 'walk' to walk and 'swim' to swim")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You got back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)? ")

        if answer == "yes":
            print("You talked to a stranger and they gave you money. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")  

print("Thank you for trying", name, ".") 
