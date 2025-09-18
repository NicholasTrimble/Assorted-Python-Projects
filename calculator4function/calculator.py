from art import logo
print(logo)


def addition_calculator(x, y):
    return x + y


def subtraction_calculator(x, y):
    return x - y


def multiplication_calculator(x, y):
    return x * y


def division_calculator(x, y):
    return x / y


print("Welcome to Calculator")
user_input = "y"

while user_input == "y":

    user_input = input("Would you like to do some math? (y or n)?\n")
    user_input = user_input.lower()[0]
    if user_input == "y":
        x = int(input("Please enter a number:\n"))
        calc_sign = input(("Please enter +, -, * or /.\n"))
        y = int(input("Please enter another number:\n"))

        if calc_sign == "+":
            result = addition_calculator(x, y)
            print(f"*****The answer is {result}*****")
        elif calc_sign == "-":
            result = subtraction_calculator(x, y)
            print(f"*****The answer is {result}*****")
        elif calc_sign == "*":
            result = multiplication_calculator(x, y)
            print(f"*****The answer is {result}*****")
        elif calc_sign == "/":
            result = division_calculator(x, y)
            print(f"*****The answer is {result}*****")

    else:
        print("*****Goodbye*****")
        exit()