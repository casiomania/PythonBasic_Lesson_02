# Lesson 02 / Homework 02
# The user enters the number of meters from the keyboard.
# Depending on the user's choice, the program converts meters to miles, inches, or yards.

# user enters the number of meters
meters = float(input("Enter number of meters: "))

# choice operation
selection = input("Choose which system to convert to (miles, inches or yards): ")

# convert to miles
miles = meters / 1609.34

# convert to inches
inches = meters * 39.370

# convert to yards
yards = meters * 1.0936

if selection == "miles":
    print("Miles: ", miles)
elif selection == "inches":
    print("Inches: ", inches)
elif selection == "yards":
    print("Yards: ", yards)
else:
    print("Incorrect conversion, please enter correct system, miles, inches or yards.")