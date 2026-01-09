# Ask the user for their age
# input() function always returns data as a string, even if user types a number 
age = input("Enter your age: ")

# Convert the string input to an integer so we can perform arithmetic
age = int(age) # Now age is a number (integer), not a string

# Calculate the age for next year and convert it back to a string
# str() is used here so we can combine the number with text in print
print("Next year you will be " + str(age+1))
# Output example if user enters 20:
# "Next year you will be 21"