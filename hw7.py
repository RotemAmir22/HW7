########################################################
# Intro to CS - Assignment 7
# replace the exception raising in each function with your solution
################### GOOD LUCK ##########################
########################################################

########################################################
# Q1:
########################################################
# 1
import math
from functools import reduce


def get_months_under_limit(monthly_shopping_costs, monthly_limit):
    """
    gets a dict of months and expenses per month and returns the months that their sum of expense is lower than the
    monthly limit
    :param monthly_shopping_costs: dict of expenses
    :param monthly_limit: maximum expenses allowed each month
    :return: which months are under the limit
    """
    return list(filter(lambda key: reduce(lambda value1, value2: value1 + value2,
                                          monthly_shopping_costs[key]) <= monthly_limit, monthly_shopping_costs))


# 2
def sum_under_limit_number_of_purchases(monthly_shopping_costs, max_number_of_purchases):
    """
    gets s dict and calculates the sum of all the values if the length of all the values is under the max number of
    purchases
    :param monthly_shopping_costs: dict of expenses per month
    :param max_number_of_purchases: maximum number of purchases each month
    :return: sum of expenses if no month exceeded the max number of purchases
    """
    return reduce(lambda value3, value4: value3 + value4,
                  (list(map((lambda key: reduce(lambda value1, value2: value1 + value2, monthly_shopping_costs[key])
                  if len(monthly_shopping_costs[key]) <= max_number_of_purchases
                  else math.inf * (-1)), monthly_shopping_costs))))


# 3
def verify_monthly_monotonic_growing_expenses(monthly_shopping_costs):
    """
    checks if the expenses are monotonic in each month, if they all are returns True and if not False
    :param monthly_shopping_costs: dictionary of expense per month
    :return: True if all expenses are monotonic
    """
    return all(list(map(lambda key:
                        True if monthly_shopping_costs[key] == sorted(monthly_shopping_costs[key])
                        else False, monthly_shopping_costs)))


# 4
def divide_monthly_bills(apartment_bills, bob_weekly_income):
    """
    gets a dictionary of apartment bills and returns which attendant pays for the bill according to:
    if the sum of the specific bill is lower or equals bobs salary, then bob pays for it, else Alice pays
    :param apartment_bills: dictionary of bills (key = type, value= amount to pay)
    :param bob_weekly_income: bobs income
    :return: who pays which bill
    """
    return ", ".join(list(map(lambda key:
                              f'Bob: {key}' if
                              reduce(lambda value1, value2: value1 + value2, apartment_bills[key]) <= bob_weekly_income
                              else f'Alice: {key}', apartment_bills)))


########################################################
# Q2:
########################################################
# 1
def add(num1, num2):
    """
    get two numbers and returns the sum of them
    :param num1: one num
    :param num2: two num
    :return: sum
    """
    return num1 + num2


def mul(num1, num2):
    """
        get two numbers and returns the multiplication of them
        :param num1: one num
        :param num2: two num
        :return: multiplication
        """
    return num1 * num2


def operations_parser_function(code):
    """
    gets a given code and returns the right operation (add or multiply)
    if the code sum is 1 returns add, else mul
    :param code: two number (0 or 1)
    :return: return the right function
    """
    return add if ord(code[0]) + ord(code[1]) == 97 else mul


# 2
def binary_code_compiler(lines_of_code_triplets, value_parser, operations_parser):
    """
    gets a list of codes abd translates it to: two numbers and an operation to apply on them.
    :param lines_of_code_triplets: code to evaluate and return requested calculation
    :param value_parser: function that calculates the numbers, but if wrong, returns line error
    :param operations_parser: evaluates which operation to use, if there is an error, return line error
    :return: either sum of the calculations/ index line of error/ Value Error/ TypeError
    """
    ans = 0
    for index in range(len(lines_of_code_triplets)):
        try:
            if lines_of_code_triplets[index][0][0] == '0':  # checks flag then evaluates number
                num1 = value_parser(lines_of_code_triplets[index][0])  # if cant then raises ValueError
            else:
                return f'{index}'
            if lines_of_code_triplets[index][2][0] == '0':  # checks flag then evaluates number
                num2 = value_parser(lines_of_code_triplets[index][2])  # if cant then raises ValueError
            else:
                return f'{index}'
        except ValueError as e:  # catches only Value error
            return f'{index}'
        try:
            if lines_of_code_triplets[index][1][0] == '1':  # checks flag then evaluates operation
                operator = operations_parser(lines_of_code_triplets[index][1][1:])  # if cant then raises TypeError
            else:
                return f'{index}'
            ans += operator(num1, num2)
        except TypeError as e:  # catches only Type error
            return f'{index}'
    return ans
