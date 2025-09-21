# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# prompt the result to the terminal.
# Ask the user if they would like to do another calculation.

def prompt(message):
    print(f'==> {message}')
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def calculator():
    prompt('Welcome to Calculator!\n')
    # Ask the user for the first number
    prompt('What\'s the first number?\n')
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.\n")
        number1 = input()

    prompt("What's the second number?\n")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.\n")
        number2 = input()

    prompt(f'{number1} {number2}\n')
    prompt("""What operation would you like to perform?\n
       1) Add 2) Subtract 3) Multiply 4) Divide\n""")
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4\n')
        operation = input()


    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)




    prompt(f'The result is: {output}\n')

    prompt('Would you like to perform another calculation?\n If so enter y \nIf your done press enter.\n')


    re_start = input()

    if re_start == 'y':
        calculator()
    else:
        prompt('Thanks for using the calculator, have a great day!\n')

calculator()