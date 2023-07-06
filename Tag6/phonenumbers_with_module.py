import phonenumbers
from phonenumbers_list import numbers, din_numbers

def is_valid(number):
    try:
        parsed_number = phonenumbers.parse(number, "DE")
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

valid = []
invalid = []
for number in numbers: # din_numbers:
    if is_valid(number):
        valid.append(number)
    else:
        invalid.append(number)

print("Valid:  ", valid)
print("Invalid:", invalid)
