import re
from phonenumbers_list import numbers, din_numbers

#rex = re.compile(pattern = r'^(\+49|0)[ ]?([1-9][0-9]{1,5})?[ ]?((\([0-9]{1,6}\))|([0-9]{1,6}))?[ ]?([0-9]{1,4})([ -][0-9]{1,4}){0,3}$')

number_1 = r"((\+\d{2}\s\d{2,4}\s\d{8})" # +49 31 12345678
number_2 = r"(0\d{3,4}\s\d{5,11}(-\d{2})?)" # 0241 12345-67
number_3 = r"(0\d{3,4}\s\d\s\d{3,9})" # 01234 0 24233243
number_4 = r"(0\d{3,4}\s\d{5,11}))" # 0123 12345678901
number_5 = r"110|112"

rex = re.compile(f"{number_1}|{number_2}|{number_3}|{number_4}|{number_5}")

def is_valid(number):
    return bool(rex.match(number))

valid = []
invalid = []
for number in numbers: # din_numbers:
    if is_valid(number):
        valid.append(number)
    else:
        invalid.append(number)

print("Valid:  ", valid)
print("Invalid:", invalid)
