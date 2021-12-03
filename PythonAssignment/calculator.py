# python calculator program

# Addition
def add(num1, num2):
    return num1 + num2

# Substraction

def sub(num1, num2):
    return num1 - num2

#Multiplication
def mul(num1, num2):
    return num1 * num2

# Division

def div(num1, num2):
    return num1 / num2

# Power
def power(num1, num2):
    return num1 ** num2

print("Please select options below.\n"\
        "1. Add\n"\
        "2. Subtract\n"\
        "3. Multiply\n"\
        "4. Divide\n"\
        "5. Power\n")

# Input from user
choice = int(input("enter your choice operation."))

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if choice == 1:
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 2:
    print(num_1, "-", num_2, "=", sub(num_1, num_2))


elif choice == 3:
    print(num_1, "*", num_2, "=", mul(num_1, num_2))

elif choice == 4:
    print(num_1, "/", num_2, "=", div(num_1, num_2))

elif choice == 5:
    print(num_1, "**", num_2, "=", power(num_1, num_2))

else:
    print("Invalid choice")
