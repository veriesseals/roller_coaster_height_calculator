# Roller Coaster Height Calculator
# ---------------------------------------------

# Created blank space for terminal readability
# ---------------------------------------------
term_blank_space = "\n"
print(term_blank_space)


# Print the title of the Calculator
# ---------------------------------------------

print("Welcome to the Roller Coaster Height Calculator")

term_blank_space = "\n"
print(term_blank_space)

# Create variable and input for end user to specify height
# ---------------------------------------------

height = int(input("What is your hight in cm "))

bill = 0


term_blank_space = "\n"
print(term_blank_space)

# Create if/else condition to evaluate height 
# ---------------------------------------------

if height >= 120:
    # print(f"You are {height} cm tall")
    print("You can ride the roller coaster")
    # Enter age if they can ride
    # ---------------------------------------------

    age = int(input("How old are you?: "))
    print(f"You are: {age} years old!")
    # Nested if/else statements
    # ---------------------------------------------
    if age >= 18:
        bill = 12
        print("You are an adult give me $12!")
    elif age > 12 < 18:
        bill = 7
        print("You are young, so you can play me $7")
    else:
        bill = 5
        print("You get the children's price, I guess you can play me $5")

    # Would you like to add a photo
    # ---------------------------------------------
    
    term_blank_space = "\n"
    print(term_blank_space)

    print("How about buying a photo today?")
    
    term_blank_space = "\n"
    print(term_blank_space)

    would_you_like_photo = input("Would you like a photo? (Enter: y or n) ")
    print(would_you_like_photo)

    if would_you_like_photo == "y":
        print("Please pay $3: ")
        bill += 3 # Add $3 to the bill or total. Or bill = bill + 3
        print(f"Your total bill is: ${bill}")
    elif would_you_like_photo == "n":
        print("Thank you, no charge: ")
    else:
        print("Thank you for your visit")

    
    # ---------------------------------------------

else:
    print(f"You are {height} cm tall. There is a minimum of 120cm")
    print("Sorry you have to grow taller before you can ride")
