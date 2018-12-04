import re

str = '11abcd3434'
# finding specific digit series having specific length like
# in our case it is 4
print("Matches", len(  re.findall("\d{4}", str)  ))
