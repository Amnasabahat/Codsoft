# Get user input for the operation
print("Enter operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

operation = input("Please enter the number corresponding to your chosen operation: ")

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculation based on the chosen operation
if operation == '1':
    result = num1 + num2
elif operation == '2':
    result = num1 - num2
elif operation == '3':
    result = num1 * num2
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

# Display the result
print("Result:", result)
