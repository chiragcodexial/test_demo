birth_year = input("Enter your birth year: ")
age = 2022 - int (birth_year)
print(age)
print ("You too old to ride a bike")

import math

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    return x / y

# Function to calculate square root
def sqrt(x):
    return math.sqrt(x)

# Function to calculate power
def power(x, y):
    return x ** y

# Main function
def main():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Square root")
    print("6.Power")

    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        # If user selects square root or power, take input of only one number
        if choice == '5' or choice == '6':
            num1 = float(input("Enter a number: "))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print("Square root of", num1, "=", sqrt(num1))

        elif choice == '6':
            power_num = float(input("Enter power: "))
            print(num1, "^", power_num, "=", power(num1, power_num))
    else:
        print("Invalid Input")

# Run the main function
if __name__ == '__main__':
    main()

print("Your code is finished")
