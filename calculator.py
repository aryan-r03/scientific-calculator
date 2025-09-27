import numpy as np

width = 180

print("\n" + "  Calculator  ".center(width, "=") + "\n")
print("  Select operation : \n".center(width))
print("1. Addition".center(width))
print("2. Subtraction".center(width))
print("3. Multiplication".center(width))
print("4. Division".center(width))
print("5. Power (x^y)".center(width))
print("6. Square Root".center(width))
print("7. Cube Root".center(width))
print("8. Logarithm (base 10)".center(width))
print("9. Natural Logarithm (ln)".center(width))

while True:
    print("\n\033[34m ")
    print("Enter choice (0-9) : \n".center(width))
    choice = int(input("\033[3m".ljust(width-87)))
    print("\033[0m")

    if choice == 1:
        print(f"You choose to \033[3m\033[34m'Add'\033[0m\n".center(width+13))
        a = float(input("\nEnter first number  : "))
        b = float(input("\nEnter second number : "))
        print("----------------------------------------------------------------")
        print(f"Sum is = \033[32m {a + b} \033[0m")
        print("----------------------------------------------------------------")

    elif choice == 2:
        print(f"You choose to \033[3m\033[34m'Substract'\033[0m\n".center(width+10))
        a = float(input("\nEnter first number  : "))
        b = float(input("\nEnter second number : "))
        print("----------------------------------------------------------------")
        print(f"Difference is of = \033[32m {a - b} \033[0m")
        print("----------------------------------------------------------------")

    elif choice == 3:
        print(f"You choose to \033[3m\033[34m'Multiply'\033[0m\n".center(width+10))
        a = float(input("\nEnter first number  : "))
        b = float(input("\nEnter second number : "))
        print("----------------------------------------------------------------")
        print(f"Result = \033[32m {round((a * b), 3)} \033[0m")
        print("----------------------------------------------------------------")

    elif choice == 4:
        print(f"You choose to \033[3m\033[34m'Divide'\033[0m\n".center(width+10))
        a = float(input("\n Enter numerator  : "))
        b = float(input("\nEnter denominator : "))
        if b != 0:
            print("----------------------------------------------------------------")
            print(f"Result = \033[32m {round((a / b), 2)} \033[0m")
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            print("Error! Division by zero.")
            print("----------------------------------------------------------------")

    elif choice == 5:
        print(f"You choose to \033[3m\033[34m'Check Exponential value'\033[0m\n".center(width+15))
        a = float(input("\n  Enter base   : "))
        b = float(input("\nEnter exponent : "))
        print("----------------------------------------------------------------")
        print(f"Exponential value is = \033[32m {round((a ** b), 2)} \033[0m")
        print("----------------------------------------------------------------")

    elif choice == 6:
        print(f"You choose to \033[3m\033[34m'Check Square Root'\033[0m\n".center(width+15))
        a = float(input("\nEnter number : "))
        if a >= 0:
            print("----------------------------------------------------------------")
            print(f"Square Root is = \033[32m{round(np.sqrt(a), 2)}\033[0m")
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            print("Error! Square root of negative number not possible.")
            print("----------------------------------------------------------------")

    elif choice == 7:
        print(f"You choose to \033[3m\033[34m'Check Cube Root'\033[0m\n".center(width+15))
        a = float(input("\nEnter number : "))
        if a >= 0:
            print("----------------------------------------------------------------")
            print(f"Cube Root is = \033[32m{round(np.cbrt(a), 2)}\033[0m")
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            print("Error! Cube root of negative number not possible.")
            print("----------------------------------------------------------------")

    elif choice == 8:
        print(f"You choose to \033[3m\033[34m'To Find Log base-10 value'\033[0m\n".center(width+15))
        a = float(input("\nEnter number : "))
        if a > 0:
            print("----------------------------------------------------------------")
            print(f"Result = \033[32m{round(np.log10(a), 2)}\033[0m")
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            print("Error! Logarithm not defined for non-positive numbers.")
            print("----------------------------------------------------------------")

    elif choice == 9:
        print(f"You choose to \033[3m\033[34m'To Find Natural Log'\033[0m\n".center(width+15))
        a = float(input("\nEnter number : "))
        if a > 0:
            print("----------------------------------------------------------------")
            print(f"Result = \033[32m{round(np.log(a), 2)}\033[0m")
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            print("Error! Natural Log not defined for non-positive numbers.")
            print("----------------------------------------------------------------")

    else:
        print("Invalid choice!")

    print("\n")
    print("Press \033[33m\033[3mEnter\033[0m to calculate again \n".center(width+15))
    retry = input("".center(width-91))
    if retry != "":
        print("\n\033[35m")
        print("Good Bye".center(width))
        print("\n\033[0m")
        break

