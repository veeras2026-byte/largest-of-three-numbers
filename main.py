# Program to Find the Largest of Three Numbers
# This program takes three numbers as input and displays the largest one

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the three numbers using conditional statements
if num1 >= num2 and num1 >= num3:
    # num1 is greater than or equal to both num2 and num3
    largest = num1
elif num2 >= num1 and num2 >= num3:
    # num2 is greater than or equal to both num1 and num3
    largest = num2
else:
    # num3 must be the largest
    largest = num3

# Display the result
print(f"\nThe largest of the three numbers is: {largest}")
