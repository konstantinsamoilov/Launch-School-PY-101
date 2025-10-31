# Ask user for second number
# Ask user for operation
# Do operation
# Print result

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt("Welcome to Calculator!")

# Ask user for first number
prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Invalid :()")
    number1 = input()

# Ask user for second number
prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Invalid :((()")
    number2 = input()

prompt("""What would you like to do?
1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('Gotta choose 1/2/3/4!')
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

prompt(f"The result is: {output}")