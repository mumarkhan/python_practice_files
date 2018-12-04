import re


str = '123 1234 12345 123456 1234567'
# finding series of digits with in a specific range
# like in our case it is series may contain 4, 5, 6 or 7 number of digits
print("Matches", len(  re.findall("\d{4,7}", str)  ))
