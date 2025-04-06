# Roller Coaster Height Calculator
# ---------------------------------------------

# Created blank space for terminal readablility
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
        print("You are an adult give me $12!")
    else:
        print("You are young, I guess you can play me $7")
else:
    print(f"You are {height} cm tall. There is a minimum of 120cm")
    print("Sorry you have to grow taller before you can ride")
