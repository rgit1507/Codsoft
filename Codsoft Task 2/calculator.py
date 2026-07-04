def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("[ERROR] Invalid input! Please enter a valid number.")

def main():
    while True:
        print("\n" + "="*30)
        print("         SIMPLE CALCULATOR")
        print("="*30)
        print("Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        print("="*30)

        choice = input("Choose an option (1-5): ").strip()

        if choice == '5':
            print("\nGoodbye! Thank you for using the calculator.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("[ERROR] Invalid choice. Please choose a number between 1 and 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            # Format the output to look clean (avoid trailing .0 for integers)
            num1_str = int(num1) if num1.is_integer() else num1
            num2_str = int(num2) if num2.is_integer() else num2
            result_str = int(result) if isinstance(result, float) and result.is_integer() else result

            print(f"\nResult: {num1_str} {operation} {num2_str} = {result_str}")

        except ValueError as e:
            print(f"\n[ERROR]: {e}")

if __name__ == "__main__":
    main()
