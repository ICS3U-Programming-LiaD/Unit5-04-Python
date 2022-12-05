#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Dec 1st, 2022
# This program is a calculator
# you can use '+' '-' '/' and '*'


def calculate(math_operation, first_number, second_number):

    # Determines what operation the program does based on user input
    if math_operation == "+":
        output = first_number + second_number
    elif math_operation == "-":
        output = first_number - second_number
    elif math_operation == "/":
        output = first_number / second_number
    elif math_operation == "*":
        output = first_number * second_number

    return output


def main():
    # getting the operation and two numbers from the user

    math_operation = input("Input the operation you want to perform (+, -, /, *): ")

    if (
        math_operation == "+"
        or math_operation == "-"
        or math_operation == "/"
        or math_operation == "*"
    ):

        # making sure the numbers the user input are valid\
        try:
            first_number = float(input("Enter first number: "))

            try:
                second_number = float(input("Enter second number: "))
                # Call the function to calculate
                result = calculate(math_operation, first_number, second_number)
                # printing the equation and the answer
                print(
                    "{} {} {} = {}".format(
                        first_number, math_operation, second_number, result
                    )
                )

                print("Thanks for playing.")

            except ValueError:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
