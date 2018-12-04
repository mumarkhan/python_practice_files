import re

# \f    formfeed
# \n    newline
# \r    carriage return
# \v    vertical tab

# \s means [\f\n\r\t\v] there will be one of these \f or \n or \r or \t ot \v
# \S means [^\f\n\r\t\v] there will not be any one of these \f or \n or \r or \t ot \v

full_name = "John Peter"
if re.search("\w{3,20}\s\w{3,20}", full_name):
    print("It's a valid full name.")
