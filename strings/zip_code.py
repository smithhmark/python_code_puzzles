"""
https://www.hackerrank.com/challenges/validating-postalcode/problem
"""
import re

regex_integer_in_range = r"^[123456789]\d{5}$"

regex_alternating_repetitive_digit_pair = r"(?=((\d)\d\2))"

def valid(P):
    if re.match(regex_integer_in_range, P):
        found = re.findall(regex_alternating_repetitive_digit_pair, P)
        print(found)
        if len(found) < 2:
            return True
        else:
            print(len(found))
            print(found)
            print("too many repeats")
    else:
        print("out of range")
    return False
