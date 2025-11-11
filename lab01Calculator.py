""" Scientific Calculator - Lab 01
    Programmers: Grace Zhao, Sophia Pappous
    Date: 8/29/24"""

import math

def main():
    # Variables
    previous_calculations = []
    previous_result = 0.0
    sum_of_calculations = 0.0
    number_of_calculations = 0

    current_result = 0.0
    user_selection = 0

    first_operand = 0.0
    second_operand = 0.0

    # Calculator
    while True:
        print("Current Result: ", current_result, "\n")
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program\n"
              "1. Addition\n"
              "2. Subtraction\n"
              "3. Multiplication\n"
              "4. Division\n"
              "5. Exponentiation\n"
              "6. Logarithm\n"
              "7. Display Average\n")
        user_selection = int(input("Enter Menu Selection: "))

        # Test for number 7 and 0 first, because we don't want to ask them for operands when they just want average or exit
        if user_selection == 0:
            print("Thanks for using this calculator. Goodbye!")
            break
        if user_selection == 7:
            if number_of_calculations == 0:
                print("\nError: No calculations yet to average!\n")
                user_selection = int(input("Enter Menu Selection: "))
            else:
                sum_of_calculations = sum(previous_calculations)
                print('The average of the calculations is %.2f \n' %  (sum_of_calculations/number_of_calculations))
                user_selection = int(input("Enter Menu Selection: "))
        # Tests to ensure that the user puts a number within the menu selection
        if user_selection > 7 | user_selection < 0:
            print("Error: Invalid selection!")
            user_selection = int(input("Enter Menu Selection: "))

        # Asks user for two numbers
        first_operand = input("Enter First Operand: ")
        second_operand = input("Enter Second Operand: ")
        print()

        # Code to use previous calculation result
        if first_operand == "RESULT":
            first_operand = previous_result
        else:
            first_operand = float(first_operand)


        if second_operand == "RESULT":
            second_operand = previous_result
        else:
            second_operand = float(second_operand)

        # Decides what to do with the operands
        if user_selection == 1:
            current_result = first_operand + second_operand
        if user_selection == 2:
            current_result = first_operand - second_operand
        if user_selection == 3:
            current_result = first_operand * second_operand
        if user_selection == 4:
            current_result = first_operand / second_operand
        if user_selection == 5:
            current_result = first_operand ** second_operand
        if user_selection == 6:
            current_result = math.log(second_operand, first_operand)

        previous_result = current_result
        previous_calculations.append(current_result)
        number_of_calculations += 1




if __name__ == '__main__':
    main()


