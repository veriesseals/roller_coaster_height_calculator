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
    print("You can ride the roller coaster")
else:
    print("Sorry you have to grow taller before you can ride")
