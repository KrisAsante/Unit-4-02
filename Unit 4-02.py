# Created by: Chris Asante
# Created on: 28-March-2019
# Created for: ICS3U
# Daily Assignment – Unit 4-02
# This is a program that rounds off decimals

def calculate_decimal(number, decimal_points):

    answer = number * (10 ** decimal_points)
    answer_2 = answer + 0.5
    answer_3 = int(answer_2)
    final_answer = answer_3 / (10 ** decimal_points)
    print (final_answer)

user_number = float(input("Enter the decimal number: "))
user_decimal_points = int(input("Enter how many decimal points you want to round off to: "))
calculate_decimal(user_number, user_decimal_points)
