import re


# \w means [a-zA-Z0-9_]   anything from 'a' to 'z' and 'A' to 'Z' and '0' to '9' and '_'
# \w means [^a-zA-Z0-9_]   anything except 'a' to 'z' and 'A' to 'Z' and '0' to '9' and '_' 

phone = '412-521-613'

# you may enter \d instead of \w as in our case all three
# chracters are digits
# {3} is checking the series of digits should have length 3

if re.search("\w{3}-\w{3}-\w{3}", phone):
    print("It's a phone number")


# as phone numbers don't contain alphabets so its better to use
# \d instead of \w

if re.search("\d{3}-\d{3}-\d{3}", phone):
    print("It's a phone number")

