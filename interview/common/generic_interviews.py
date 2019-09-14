"""
This script includes all the functions for generic interviews
"""


def binary_to_decimal(decimal_num: str):
    """
    Converts binary number to decimal number.
    @return: <int> int of the decimal number
    """
    decimal_string = str(decimal_num)
    if len(decimal_string) > 0:
        first = decimal_string[0]
        current = 2**(len(decimal_string) - 1) if first == '1' else 0
        decimal_string = decimal_string[1:]
        return current + binary_to_decimal(decimal_string)
    return 0
