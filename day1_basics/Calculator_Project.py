# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main program loop
while True:
    print("\nSelect operation:")  # Extra line before the operations list
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get user's choice of operation
    choice = input("Enter choice (1/2/3/4/5): ")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4']:
        try:
            # Get user input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the operation
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}\n")  # Add a new line after the result
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}\n")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}\n")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")  # Add a new line after error
    elif choice == '5':
        print("\nExiting the calculator. Goodbye!")  # Extra line before the exit message
        break
    else:
        print("\nInvalid choice! Please choose a valid operation.\n")  # Add a new line after error
