running = True
while running:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Choose operation (+, -, *, /): ")

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        if number2 == 0:
            result = "Error!!! Division by zero = infinity / undeined "
        else:
            result = number1 / number2
    else:
        result = "Invalid operator"

    print("Result:", result)
    if not input("Do you want to calculate again? (y/n): ").strip().lower() == 'y':
        running = False

print("Calculator closed.")