# Lesson 02 / Homework 01
# The user enters three digits from the keyboard. Depending on the user's choice,
# the program displays the maximum of three, the minimum of three, or the arithmetic mean of the three numbers.

# user enter numbers
entered_number = int(input("Enter 3-digit number: "))

# define each number
number_1 = entered_number // 100 % 10
number_2 = entered_number % 100 // 10
number_3 = entered_number % 10

# find minimum
minimum = number_1
if number_2 < minimum:
    minimum = number_2
if number_3 < minimum:
    minimum = number_3

# find maximum
maximum = number_1
if number_2 > maximum:
    maximum = number_2
if number_3 > maximum:
    maximum = number_3

# find avg
average = (number_1 + number_2 + number_3) / 3

# choice operation
selection = input("Select an operation (min, max or avg): ")

# output the selected operation
if selection == "min":
    print("Min: ", minimum)
elif selection == "max":
    print("Max: ", maximum)
elif selection == "avg":
    print("Avg: ", average)
else:
    print("Incorrect operation selection, please enter min, max or avg.")
