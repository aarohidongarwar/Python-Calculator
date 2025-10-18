while True:
    print()
    print("Python Calculator")
    print("=" * 20)
    print()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # List of valid operations
    valid_operators = ['+', '-', '*', '/', '**', 'all', 'sqrt', 'root', 'abs', '%']

    # Keep asking for a valid operator
    operator = input("Enter an operation (+, -, *, /, **, all, sqrt, root, abs, %): ")
    while operator not in valid_operators:
        print("Invalid Operator! Please try again.")
        operator = input("Enter an operation (+, -, *, /, **, all, sqrt, root, abs, %): ")

    print("You chose:", operator)
    print()

    # Perform selected operation
    if operator == '+':
        print(f"{num1} + {num2} = {num1 + num2}")

    elif operator == '-':
        print(f"{num1} - {num2} = {num1 - num2}")

    elif operator == '*':
        print(f"{num1} * {num2} = {num1 * num2}")

    elif operator == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by Zero!")

    elif operator == '**':
        print(f"{num1} ** {num2} = {num1 ** num2}")

    # Perform all operations
    elif operator == 'all':
        print("Performing all operations:")
        print(f"Addition: {num1 + num2}")
        print(f"Subtraction: {num1 - num2}")
        print(f"Multiplication: {num1 * num2}")
        if num2 != 0:
            print(f"Division: {num1 / num2}")
        else:
            print("Division: Cannot divide by Zero!")
        print(f"Exponentiation: {num1 ** num2}")

    # Square roots using power operator
    elif operator == 'sqrt':
        print(f"Square root of {num1} = {num1 ** 0.5}")
        print(f"Square root of {num2} = {num2 ** 0.5}")

    # Any root (e.g., cube root)
    elif operator == 'root':
        root = float(input("Enter the root value (e.g., 3 for cube root): "))
        print(f"{num1} to the power of (1/{root}) = {num1 ** (1 / root)}")
        print(f"{num2} to the power of (1/{root}) = {num2 ** (1 / root)}")

    # Absolute value using conditional
    elif operator == 'abs':
        abs1 = num1 if num1 >= 0 else -num1
        abs2 = num2 if num2 >= 0 else -num2
        print(f"Absolute value of {num1} = {abs1}")
        print(f"Absolute value of {num2} = {abs2}")

    # Modulus operation
    elif operator == '%':
        print(f"{num1} % {num2} = {num1 % num2}")

    print()
    reset = input("Press 'C' to calculate again. Press any other key to exit! ")
    if reset.lower() != 'c':
        print()
        print("GOODBYE!")
        print()
        break
