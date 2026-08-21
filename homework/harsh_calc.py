import math

while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. nPr")
    print("9. nCr")
    print("10. Quadratic Equation")
    print("11. Exit")

    choice = input("\nEnter your choice: ")

    # Basic arithmetic
    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", a + b)

        elif choice == "2":
            print("Answer =", a - b)

        elif choice == "3":
            print("Answer =", a * b)

        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero!")
            else:
                print("Answer =", a / b)

        elif choice == "5":
            print("Answer =", a ** b)

    # Square root
    elif choice == "6":
        a = float(input("Enter number: "))

        if a < 0:
            print("Cannot find the square root of a negative number.")
        else:
            print("Answer =", math.sqrt(a))

    # Factorial
    elif choice == "7":
        n = int(input("Enter n: "))

        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Answer =", math.factorial(n))

    # nPr
    elif choice == "8":
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))

        if n < 0 or r < 0 or r > n:
            print("Invalid values. Make sure n >= r >= 0.")
        else:
            answer = math.factorial(n) // math.factorial(n - r)
            print("nPr =", answer)

    # nCr
    elif choice == "9":
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))

        if n < 0 or r < 0 or r > n:
            print("Invalid values. Make sure n >= r >= 0.")
        else:
            answer = math.factorial(n) // (
                math.factorial(r) * math.factorial(n - r)
            )
            print("nCr =", answer)

    # Quadratic equation
    elif choice == "10":
        print("\nFor ax² + bx + c = 0")

        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        if a == 0:
            print("This is not a quadratic equation.")

        else:
            discriminant = b**2 - 4*a*c

            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)

                print("Two real roots:")
                print("x1 =", x1)
                print("x2 =", x2)

            elif discriminant == 0:
                x = -b / (2*a)

                print("One repeated real root:")
                print("x =", x)

            else:
                real = -b / (2*a)
                imaginary = math.sqrt(-discriminant) / (2*a)

                print("Two complex roots:")
                print("x1 =", real, "+", imaginary, "i")
                print("x2 =", real, "-", imaginary, "i")

    # Exit
    elif choice == "11":
        print("Calculator closed.")
        break

    else:
        print("Invalid choice. Please try again.")