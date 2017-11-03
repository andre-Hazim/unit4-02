# Created by : Andre Hazim and Ray Octavious
# Created on : 30 Oct. 2017
# Created for : ICS3UR
# Rounds a number to user input decimal places

def user_round_number(number_to_round, number_round_by):
    number_to_round = long(number_to_round * 10 ** number_round_by)
    number_to_round = number_to_round + 0.5
    number_to_round = int(number_to_round)
    number_to_round = number_to_round / 10 ** number_round_by
    number_to_round = float(number_to_round)
    print number_to_round
round_number = raw_input("Enter a number with decimals")
round_number = float(round_number)
rounder_number = raw_input("Enter how many decimals you want")
rounder_number = float(rounder_number)
user_round_number(round_number, rounder_number)
