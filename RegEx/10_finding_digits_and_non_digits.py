import re

str = '11abcd3434'
# finding all digits
digits = re.findall("\d", str)
print(digits)
# getting total number of digits
print(len(digits))
# finding except digits
non_digit = re.findall("\D", str)
print(non_digit)
# getting total number of non digits
print(len(non_digit))

