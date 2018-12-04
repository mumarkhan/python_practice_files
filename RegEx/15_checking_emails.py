import re

# \f    formfeed
# \n    newline
# \r    carriage return
# \v    vertical tab



# while using "-" symbol in regular expression not for range 
# just as a symbol put it at the end of choice list
# like
# [\w.+%-]


emails = "ab@gmail.com ab @gmail.com fd@.com"
regex_email = "[\w.+%-]{2,20}@[a-zA-Z0-9.-]{2,20}.[a-zA-Z]{2,3}"

print("Number of emails found:\t", len(  re.findall(regex_email, emails) ))

