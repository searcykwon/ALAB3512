num_1 = input("Enter a number: ")
num_2 = input("Enter a number: ")

if not num_1.isdigit() or not num_2.isdigit():
    print("At least one of the inputs is not a valid digit number!")
else:
    num_1 = int(num_1)
    num_2 = int(num_2)

    operator = input("Choose an operation (+, -, *, /): ")
    if operator not in ["+", "-", "*", "/"]: 
        print("Error: Please enter a valid operator (+, -, *, /).")
    elif operator == "+":
        result = num_1 + num_2
        print(f"{num_1} + {num_2} = {result}")
    elif operator == "-":
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}")
    elif operator == "*":
        result = num_1 * num_2
        print(f"{num_1} * {num_2} = {result}")
    elif operator == "/":
        if num_2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result}")