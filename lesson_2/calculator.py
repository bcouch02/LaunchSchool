
def prompt(message): 
    print(f'==> {message}')
    
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False
        
        
print('Welcome to the Calculator!')

prompt("What's the First Number?")
first_number = input()

while invalid_number(first_number):
    prompt("Hmm... that doesn't look like a valid number.")
    first_number = input()

prompt("What's the Second Number?")
second_number = input()

while invalid_number(second_number):
    prompt("Hmm... that doesn't look like a valid number.")
    second_number = input()
    
prompt('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt("You must chose 1, 2, 3, or 4.")
    operation = input()

match operation:
    case '1': #1 represents addition
        output = int(first_number) + int(second_number)
    case '2': #2 represents subtraction
        output = int(first_number) - int(second_number)
    case '3': #3 represents multiplication
        output = int(first_number) * int(second_number)
    case '4': #4 represents division
        output = int(first_number) / int(second_number)

prompt(f"The result is: {output}")