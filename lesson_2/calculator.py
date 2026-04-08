print('Welcome to the Calculator!')

# Ask the user for the first number
print("What's the First Number?")
first_number = input()

# Ask the user for the second number
print("What's the Second Number?")
second_number = input()

# Print the numbers back to the user
print(f'{first_number} {second_number}')

#ask for the operation
print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':
  output = int(first_number) + int(second_number)
elif operation == '2': #2 represents subtraction
  output = int(first_number) - int(second_number)
elif operation == '3': #3 represents multiplication
  output = int(first_number) * int(second_number)
else: #4 represents division
  output = int(first_number) / int(second_number)


print(f"The result is: {output}")


# PSUEDOCODE
# START
# GET NUMBER1 = USER INPUT
# GET NUMBER2 = USER INPUT
# ADD NUMBER1 AND NUMBER2
# PRINT RESULT
# END

# PSUEDOCODE
# START
# GET Take a list of strings
# SET Iteration = 0
# WHILE Iteration < LENGTH OF LIST
#   Connect the strings together
#   INCREMENT Iteration
# PRINT RESULT
# END